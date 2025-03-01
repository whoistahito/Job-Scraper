import random
import time
from typing import Optional

import pandas as pd
import schedule

from JobSpy.src.jobspy import Site
from JobSpy.src.jobspy import scrape_jobs
from JobSpy.src.jobspy.scrapers.utils import create_logger
from app import app
from db.database_service import UserManager, UserEmailManager
from email_manager import send_email
from html_render import create_job_card, get_html_template, get_welcome_message
from llm import validate_job_title, batch_process, validate_location

logger = create_logger("main")


def find_jobs(
        site: Site,
        search_term: str,
        location: str,
        job_type: Optional[str],
) -> pd.DataFrame:
    """
    Find jobs on a site with the given job characteristics.
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
        location=location.split(",")[0].strip() if location.split(",")[0].strip() else " ",
        results_wanted=10,
        hours_old=120,
        country_indeed=location.split(",")[-1].strip() if location.split(",")[-1].strip() else "Germany",
        proxies=None,
        enforce_annual_salary=True
    )


def try_find_jobs(
        site: Site,
        search_term: str,
        location: str,
        job_type: Optional[str],
        max_retries: int = 2,
) -> pd.DataFrame:
    """
    Process job scraping for a single site, retry if needed,
    and return a DataFrame with the found jobs.
    """
    retries = 0

    while retries < max_retries:
        try:
            return find_jobs(site, search_term, location, job_type)
        except Exception as err:
            logger.error(f"Exception while processing {site}: {err}")
            retries += 1
            logger.error(f"Retrying {retries}/{max_retries}")
            time.sleep(random.uniform(100, 200))  # Wait before retrying
    return pd.DataFrame()  # Return empty DataFrame if all retries fail


def notify_jobs(filtered_jobs: pd.DataFrame, email: str, position: str, location: str) -> bool:
    """
    Send notification email if there are filtered jobs based on refined criteria.
    """
    if not filtered_jobs.empty:
        # Sort jobs by site and date posted
        filtered_jobs = filtered_jobs.sort_values(
            by=["site", "date_posted"], ascending=[True, False]
        ).reset_index(drop=True)
        # Filter and render job listings
        filtered_jobs['has_salary'] = filtered_jobs["min_amount"].notna() | filtered_jobs["max_amount"].notna()
        html_content = ''.join(filtered_jobs.apply(create_job_card, axis=1))
        html_template = get_html_template(html_content, email, position, location)
        send_email(html_template, "Found some job opportunities for you!", email, is_html=True)
        return True

    logger.error("No jobs found based on the criteria.")
    return False


def check_for_new_users():
    """
    Check for new users and send them a welcome email.
    """
    with app.app_context():
        new_users = UserManager().get_new_users()
        for user in new_users:
            send_email(get_welcome_message(), "Welcome to Your Job Finder!", user.email, is_html=True)
            UserManager().mark_user_as_not_new(user.email, user.position, user.location)
            notify_user(user)


def notify_users() -> None:
    """
    Notify all registered users based on their preferences by scraping job sites
    and sending them an email with relevant job opportunities.
    """
    with app.app_context():
        users = UserManager().get_all_users()
        for user in users:
            notify_user(user)


def notify_user(user):
    jobs_df = pd.DataFrame()
    for site in [Site.LINKEDIN, Site.INDEED, Site.GOOGLE]:
        found_jobs = try_find_jobs(site, user.position, user.location, user.job_type)
        jobs_df = pd.concat([jobs_df, found_jobs], ignore_index=True)
        time.sleep(random.uniform(10, 20))
    if not jobs_df.empty:
        # Remove already sent jobs
        jobs_df = jobs_df[
            ~jobs_df['job_url'].apply(lambda url:
                                      UserEmailManager().is_sent(user.email, url, user.position, user.location)
                                      )
        ]
        jobs_df = jobs_df[:7]

        # Uniform location
        validated_locations = batch_process(validate_location, jobs_df['location'].tolist())
        jobs_df['location'] = validated_locations

        # Filter out unrelated titles
        job_title_search_pairs = [(title, user.position) for title in jobs_df['title']]
        is_related_results = batch_process(validate_job_title, job_title_search_pairs)
        jobs_df['is_related'] = is_related_results

        filtered_jobs = jobs_df[jobs_df['is_related']].copy()

        if notify_jobs(filtered_jobs, user.email, user.position, user.location):
            filtered_jobs.apply(
                lambda row: UserEmailManager().add_sent_email(
                    user.email, row['job_url'], user.position, user.location), axis=1)


if __name__ == "__main__":
    schedule.every().day.at("10:45").do(
        lambda: notify_users())

    while True:
        check_for_new_users()

        schedule.run_pending()
        time.sleep(20)
