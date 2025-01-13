import random
import time
from typing import List, Optional

import pandas as pd
import schedule

from JobSpy.src.jobspy import Site
from JobSpy.src.jobspy import scrape_jobs
from JobSpy.src.jobspy.scrapers.utils import create_logger
from db.database_service import UserManager, UserEmailManager
from email_manager import send_email
from html_render import create_job_card, get_html_template
from llm import validate_job_title
from proxy_scraper import get_valid_proxies

logger = create_logger("main")


def find_jobs(
        site: Site,
        search_term: str,
        location: str,
        job_type: Optional[str],
        proxies: List[str]
) -> pd.DataFrame:
    """
    Find jobs on a site with the given job characteristics and a list of proxies.
    Adjusts search terms for specific job types if needed.
    """
    if job_type == "working student":
        search_term += " " + "Werkstudent"
        job_type = None

    return scrape_jobs(
        site_name=site,
        search_term=search_term,
        job_type=job_type,
        radius=15,
        location=location,
        results_wanted=20,
        hours_old=120,
        country_indeed='germany',
        proxies=proxies,
        enforce_annual_salary=True
    )


def process_site_jobs(
        site: Site,
        search_term: str,
        location: str,
        job_type: Optional[str],
        proxies: List[str]
) -> pd.DataFrame:
    """
    Process job scraping for a single site, retry with different proxies if needed,
    and return a DataFrame with the found jobs.
    """
    max_retries = len(proxies)
    retries = 0

    while retries < max_retries:
        try:
            proxy = proxies[retries]
            return find_jobs(site, search_term, location, job_type, [proxy])
        except Exception as err:
            logger.error(f"Exception while processing {site}: {err}")
            retries += 1
            logger.error(f"Retrying {retries}/{max_retries} with a new proxy...")
            time.sleep(random.uniform(1, 5))  # Wait before retrying
    return pd.DataFrame()  # Return empty DataFrame if all retries fail


def notify_jobs(filtered_jobs: pd.DataFrame, email: str, position: str, location: str) -> bool:
    """
    Send notification email if there are filtered jobs based on refined criteria.
    """
    if not filtered_jobs.empty:
        # Filter and render job listings
        filtered_jobs['has_salary'] = filtered_jobs["min_amount"].notna() | filtered_jobs["max_amount"].notna()
        html_content = ''.join(filtered_jobs.apply(create_job_card, axis=1))
        html_template = get_html_template(html_content, email, position, location)
        send_email(html_template, email, is_html=True)
        return True

    logger.error("No jobs found based on the criteria.")
    return False


def notify_users() -> None:
    """
    Notify all registered users based on their preferences by scraping job sites
    and sending them an email with relevant job opportunities.
    """
    users = UserManager().get_all_users()
    for user in users:
        proxies = get_proxies()
        jobs_df = pd.DataFrame()

        for site in [Site.LINKEDIN, Site.INDEED, Site.GOOGLE]:
            found_jobs = process_site_jobs(site, user.position, user.location, user.job_type, proxies)
            jobs_df = pd.concat([jobs_df, found_jobs], ignore_index=True)
            time.sleep(random.uniform(5, 10))

        if not jobs_df.empty:
            # Remove already sent jobs
            jobs_df = jobs_df[
                ~jobs_df['job_url'].apply(lambda url:
                                          UserEmailManager().is_sent(user.email, url, user.position, user.location)
                                          )
            ]

            filtered_jobs = jobs_df[
                jobs_df['title'].apply(lambda title: validate_job_title(title, user.position))
            ].copy()

            if notify_jobs(filtered_jobs, user.email, user.position, user.location):
                filtered_jobs.apply(
                    lambda row: UserEmailManager().add_sent_email(
                        user.email, row['job_url'], user.position, user.location), axis=1)


def get_proxies() -> List[str]:
    """
    Retrieve a list of valid proxies or raise an exception if insufficient proxies are available.
    """
    proxies = get_valid_proxies(['socks5', 'socks', 'socks4'], 500, 2)
    if not proxies:
        raise Exception("Not enough proxies available.")
    return proxies


if __name__ == "__main__":
    schedule.every().day.at("16:00").do(
        lambda: notify_users())

    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(20)
