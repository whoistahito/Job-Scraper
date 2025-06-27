"""
jobspy.scrapers.google
~~~~~~~~~~~~~~~~~~~

This module contains routines to scrape Google.
"""

from __future__ import annotations

from datetime import datetime, timedelta
import json
import math
import re
import time
from typing import Tuple, Optional, List, Dict, Any

import httpx
from requests.exceptions import ConnectionError
from urllib3.exceptions import MaxRetryError, ProxyError

from ..proxy_manager import get_proxy_manager
from .constants import headers_jobs, headers_initial, async_param
from .. import Scraper, ScraperInput, Site
from ..utils import (
    create_session,
)
from ..utils import extract_emails_from_text, create_logger, extract_job_type
from ...jobs import (
    JobPost,
    JobResponse,
    Location,
    JobType,
)

logger = create_logger("Google")


class GoogleJobsScraper(Scraper):
    def __init__(
        self, proxies: list[str] | str | None = None, ca_cert: str | None = None
    ):
        """
        Initializes Google Scraper with the Google jobs search url
        """
        site = Site(Site.GOOGLE)
        super().__init__(site, proxies=proxies, ca_cert=ca_cert)

        self.response = None
        self.country = None
        self.session = None
        self.scraper_input = None
        self.jobs_per_page = 10
        self.seen_urls = set()
        self.url = "https://www.google.com/search"
        self.jobs_url = "https://www.google.com/async/callback:550"
        self.proxy_manager = get_proxy_manager()
        self.max_retries = 3
        self.retry_delay = 2

    def scrape(self, scraper_input: ScraperInput) -> JobResponse:
        """
        Scrapes Google for jobs with scraper_input criteria.
        :param scraper_input: Information about job search criteria.
        :return: JobResponse containing a list of jobs.
        """
        self.scraper_input = scraper_input
        self.scraper_input.results_wanted = min(900, scraper_input.results_wanted)

        # Get a working session with proxy
        proxy, response = self.proxy_manager.get_working_proxy(
            'google',
            self.test_proxy_for_google,
            f"{self.scraper_input.search_term} jobs"
        )

        if not response:
            logger.error("Failed to find a working proxy for Google Jobs")
            return JobResponse(jobs=[])

        # Create a session with the working proxy
        self.session = create_session(
            proxies=proxy, ca_cert=self.ca_cert, is_tls=False, has_retry=True
        )

        # Extract initial data from the response we already have
        forward_cursor, job_list = self._extract_initial_cursor_and_jobs(response.text)

        if forward_cursor is None:
            logger.warning(
                "Initial cursor not found, try changing your query or there was at most 10 results"
            )
            return JobResponse(jobs=job_list)

        page = 1

        while (
            len(self.seen_urls) < scraper_input.results_wanted + scraper_input.offset
            and forward_cursor
        ):
            logger.info(
                f"Search page: {page} / {math.ceil(scraper_input.results_wanted / self.jobs_per_page)}"
            )

            # Use retry mechanism for pagination
            for retry in range(self.max_retries):
                try:
                    jobs, forward_cursor = self._get_jobs_next_page(forward_cursor)
                    if jobs:
                        job_list.extend(jobs)
                        break
                except Exception as e:
                    logger.warning(f"Error on page {page}, retry {retry+1}/{self.max_retries}: {e}")
                    if retry == self.max_retries - 1:
                        logger.error(f"Failed to get jobs on page: {page} after {self.max_retries} retries")
                        forward_cursor = None
                        break
                    time.sleep(self.retry_delay)

            if not forward_cursor:
                break

            page += 1

        return JobResponse(
            jobs=job_list[
                scraper_input.offset : scraper_input.offset
                + scraper_input.results_wanted
            ]
        )

    def test_proxy_for_google(self, proxy: Dict[str, str], query: str) -> Optional[httpx.Response]:
        """
        Test if a proxy works with Google search.

        Args:
            proxy: Proxy configuration dictionary
            query: Search query to test

        Returns:
            Response object if successful, None otherwise
        """
        try:
            params = {"q": query, "udm": "8"}
            session = create_session(
                proxies=proxy,
                is_tls=False,
                ca_cert=None,
                has_retry=False,
                clear_cookies=True,
                delay=1
            )

            response = session.get(
                'https://www.google.com/search',
                headers=headers_initial,
                timeout=20,
                params=params
            )

            if response.status_code == 200:
                # Verify we got actual job results
                if "jobs" in response.text.lower() and "callback:550" in response.text:
                    return response

        except Exception as e:
            if not isinstance(e, (ProxyError, MaxRetryError, ConnectionError)):
                logger.debug(f"Proxy test error: {str(e)}")

        return None

    def _extract_initial_cursor_and_jobs(self, html_text: str) -> Tuple[str, list[JobPost]]:
        """Gets initial cursor and jobs from an HTML response"""
        pattern_fc = r'<div jsname="Yust4d"[^>]+data-async-fc="([^"]+)"'
        match_fc = re.search(pattern_fc, html_text)
        data_async_fc = match_fc.group(1) if match_fc else None

        jobs_raw = self._find_job_info_initial_page(html_text)
        if not jobs_raw:
            logger.warning("No jobs found on the initial page")
            return None, []

        jobs = []
        for job_raw in jobs_raw:
            job_post = self._parse_job(job_raw)
            if job_post:
                jobs.append(job_post)

        return data_async_fc, jobs

    def _get_jobs_next_page(self, forward_cursor: str) -> Tuple[list[JobPost], str]:
        """
        Gets jobs from the next page using the forward cursor.

        Args:
            forward_cursor: Cursor for the next page of results

        Returns:
            Tuple of (job_posts, next_cursor)
        """
        params = {"fc": [forward_cursor], "fcv": ["3"], "async": [async_param]}

        for retry in range(self.max_retries):
            try:
                response = self.session.get(
                    self.jobs_url,
                    headers=headers_jobs,
                    params=params,
                    timeout=15
                )

                if response.status_code == 200:
                    return self._parse_jobs(response.text)

                logger.warning(f"Got status code {response.status_code} when fetching next page")

            except Exception as e:
                logger.warning(f"Error fetching next page: {str(e)}")

                # If we've reached the last retry, try with a new proxy
                if retry == self.max_retries - 1:
                    logger.info("Trying with a new proxy...")
                    self.proxy_manager.invalidate_proxy('google')
                    proxy, _ = self.proxy_manager.get_working_proxy(
                        'google',
                        self.test_proxy_for_google,
                        f"{self.scraper_input.search_term} jobs"
                    )

                    if proxy:
                        self.session = create_session(
                            proxies=proxy, ca_cert=self.ca_cert, is_tls=False, has_retry=True
                        )

            time.sleep(self.retry_delay)

        # If we get here, all retries failed
        raise Exception("Failed to get next page of jobs after multiple retries")

    def _parse_jobs(self, job_data: str) -> Tuple[list[JobPost], str]:
        """
        Parses jobs on a page with next page cursor
        """
        start_idx = job_data.find("[[[")
        end_idx = job_data.rindex("]]]") + 3

        if start_idx == -1 or end_idx <= 2:
            logger.warning("Invalid job data format received")
            return [], None

        s = job_data[start_idx:end_idx]

        try:
            parsed = json.loads(s)[0]
        except (json.JSONDecodeError, IndexError) as e:
            logger.error(f"Failed to parse job data: {str(e)}")
            return [], None

        pattern_fc = r'data-async-fc="([^"]+)"'
        match_fc = re.search(pattern_fc, job_data)
        data_async_fc = match_fc.group(1) if match_fc else None

        jobs_on_page = []
        for array in parsed:
            try:
                _, job_data = array
                if not job_data.startswith("[[["):
                    continue

                job_d = json.loads(job_data)
                job_info = self._find_job_info(job_d)

                if not job_info:
                    continue

                job_post = self._parse_job(job_info)
                if job_post:
                    jobs_on_page.append(job_post)

            except Exception as e:
                logger.debug(f"Error parsing job entry: {str(e)}")
                continue

        return jobs_on_page, data_async_fc

    def _parse_job(self, job_info: list) -> Optional[JobPost]:
        """
        Parse job information into a JobPost object

        Args:
            job_info: Raw job information

        Returns:
            JobPost object or None if invalid/duplicate
        """
        try:
            job_url = job_info[3][0][0] if job_info[3] and job_info[3][0] else None

            # Skip duplicates
            if not job_url or job_url in self.seen_urls:
                return None

            self.seen_urls.add(job_url)

            title = job_info[0]
            company_name = job_info[1]
            location = city = job_info[2]
            state = country = date_posted = None

            if location and "," in location:
                parts = [part.strip() for part in location.split(",")]
                if len(parts) >= 2:
                    city = parts[0]
                    state = parts[1]
                    country = parts[2] if len(parts) > 2 else None

            days_ago_str = job_info[12]
            if isinstance(days_ago_str, str):
                match = re.search(r"\d+", days_ago_str)
                days_ago = int(match.group()) if match else None
                date_posted = (datetime.now() - timedelta(days=days_ago)).date() if days_ago else None

            description = job_info[19] if len(job_info) > 19 else ""
            is_remote = any(keyword in description.lower() for keyword in ["remote", "wfh", "work from home"])

            return JobPost(
                id=f"go-{job_info[28]}" if len(job_info) > 28 else f"go-{hash(job_url)}",
                title=title,
                company_name=company_name,
                location=Location(
                    city=city,
                    state=state,
                    country=country
                ),
                job_url=job_url,
                date_posted=date_posted,
                is_remote=is_remote,
                description=description,
                emails=extract_emails_from_text(description),
                job_type=extract_job_type(description),
            )

        except Exception as e:
            logger.debug(f"Error parsing job: {str(e)}")
            return None

    @staticmethod
    def _find_job_info(jobs_data: list | dict) -> list | None:
        """Iterates through the JSON data to find the job listings"""
        if isinstance(jobs_data, dict):
            for key, value in jobs_data.items():
                if key == "520084652" and isinstance(value, list):
                    return value
                else:
                    result = GoogleJobsScraper._find_job_info(value)
                    if result:
                        return result
        elif isinstance(jobs_data, list):
            for item in jobs_data:
                result = GoogleJobsScraper._find_job_info(item)
                if result:
                    return result
        return None

    @staticmethod
    def _find_job_info_initial_page(html_text: str) -> List[List]:
        """
        Extract job information from the initial page HTML

        Args:
            html_text: HTML content of the initial page

        Returns:
            List of job information arrays
        """
        pattern = (
            f'520084652":('
            + r"\[.*?\]\s*])\s*}\s*]\s*]\s*]\s*]\s*]"
        )
        results = []
        matches = re.finditer(pattern, html_text)

        import json

        for match in matches:
            try:
                parsed_data = json.loads(match.group(1))
                results.append(parsed_data)
            except json.JSONDecodeError as e:
                logger.debug(f"Failed to parse match: {str(e)}")

        return results
