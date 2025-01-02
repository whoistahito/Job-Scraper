import random

from JobSpy.src.jobspy import scrape_jobs
from email_manager import send_email
from html_render import create_job_card, get_html_template
from llm import validate_job_title
from proxy_scraper import get_valid_proxies


def find_jobs(search_term, google_search_term, prox_list):
    jobs = scrape_jobs(
        site_name=["linkedin", "indeed", "google"],
        search_term=search_term,
        radius=20,
        google_search_term=google_search_term,
        location="Hamburg",
        results_wanted=20,
        hours_old=120,
        country_indeed='germany',
        proxies=prox_list,
        ca_cert=None,
        enforce_annual_salary=True
    )
    return jobs


def process_and_notify_jobs(search_term, email):
    prox = get_valid_proxies(['http'], 50, 50)
    if not prox:
        raise Exception("Not enough proxies")
    found_jobs = find_jobs(search_term, search_term, random.sample(prox, 10))
    filtered_jobs = found_jobs[found_jobs['title'].apply(lambda title: validate_job_title(title, search_term))]
    html_content = ''.join(filtered_jobs.apply(create_job_card, axis=1))
    html_template = get_html_template(html_content)
    send_email(html_template, email, is_html=True)


try:
    process_and_notify_jobs()
except Exception as e:
    print(f" Exception : {e}")
