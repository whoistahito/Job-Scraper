import random
import time

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


def find_jobs(site, search_term, location, job_type, prox_list):
    if job_type == "Werkstudent":
        search_term = search_term + " " + job_type
        job_type = None
    jobs = scrape_jobs(
        site_name=site,
        search_term=search_term,
        job_type=job_type,
        radius=15,
        location=location,
        results_wanted=20,
        hours_old=120,
        country_indeed='germany',
        proxies=prox_list,
        enforce_annual_salary=True
    )
    return jobs


def process_site_jobs(site, search_term, location, job_type, proxies):
    """Process job scraping for a single site, retry with different proxies if needed, and return a DataFrame."""
    max_retries = len(proxies)
    proxies_iter = iter(proxies)
    retries = 0

    while retries < max_retries:
        try:
            return find_jobs(site, search_term, location, job_type, next(proxies_iter))
        except Exception as err:
            logger.error(f"Exception while processing {site}: {err}")
            retries += 1
            logger.error(f"Retrying {retries}/{max_retries} with a new proxy...")
            time.sleep(random.randint(1, 5))  # Short wait before retrying
    return pd.DataFrame()  # Return an empty DataFrame if all retries fail


def notify_jobs(filtered_jobs, email, position, location):
    """Process job searches across sites and send notification email."""
    if not filtered_jobs.empty:
        # Filter and render job listings
        filtered_jobs['has_salary'] = filtered_jobs["min_amount"].notna() | filtered_jobs["max_amount"].notna()
        html_content = ''.join(filtered_jobs.apply(create_job_card, axis=1))
        html_template = get_html_template(html_content, email, position, location)
        send_email(html_template, email, is_html=True)
        return True
    else:
        logger.error("No jobs found based on the criteria.")
        return False


def notify_users():
    """Notify all users based on their preferences."""
    users = UserManager().get_all_users()
    for user in users:
        proxies = get_proxies()

        jobs_df = pd.DataFrame()

        for site in [Site.LINKEDIN, Site.INDEED, Site.GOOGLE]:
            found_jobs = process_site_jobs(site, user.position, user.location, user.job_type, proxies)
            jobs_df = pd.concat([jobs_df, found_jobs], ignore_index=True)
            time.sleep(random.randint(5, 10))

        if not jobs_df.empty:
            for _, job in jobs_df.iterrows():
                if UserEmailManager().is_sent(user.email, job['job_url'], user.position, user.location):
                    jobs_df.drop(jobs_df[jobs_df['job_url'] == job['job_url']].index, inplace=True)

            filtered_jobs = jobs_df[
                jobs_df['title'].apply(lambda title: validate_job_title(title, user.position))
            ].copy()

            send_succeed = notify_jobs(filtered_jobs, user.email, user.position, user.location)
            if send_succeed:
                for _, job in filtered_jobs.iterrows():
                    UserEmailManager().add_sent_email(user.email, job['job_url'], user.position, user.location)


def get_proxies():
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
