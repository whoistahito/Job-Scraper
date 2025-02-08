import time

import google.generativeai as genai

from JobSpy.src.jobspy.scrapers.utils import create_logger
from credential import Credential

logger = create_logger("llm")


def validate_job_title(job_title, search_term, try_count=1):
    cred = Credential()
    genai.configure(api_key=cred.get_google_api())
    model = genai.GenerativeModel("gemini-2.0-flash")
    time.sleep(4.5)
    response = model.generate_content(f"""
    Below are some examples showing a question, job title, search term, and answer format:
    
    Question: Is this job title related to searching term?
    Job title: IT-Architekt*in (m/w/d), 
    Search term: architectural project manager, 
    Answer: No

    Question: Is this job title related to searching term?
    Job title: Senior Architectural Designer / Project Manager , 
    Search term: architectural project manager ,
    Answer: Yes
    
    
    Question: Is this job title related to searching term?
    Job title:{job_title} , 
    Search term: {search_term} , 
    Answer: 
    """)
    res = response.text.strip().lower()  # Remove whitespace and make lowercase
    if res == "yes":
        return True
    elif res == "no":
        return False
    else:
        if try_count == 4:
            logger.error(f"Could not validate job title for {job_title} with response {res}")
            return False
        return validate_job_title(job_title, search_term, try_count + 1)


def validate_location(location):
    cred = Credential()
    genai.configure(api_key=cred.get_google_api())
    model = genai.GenerativeModel("gemini-2.0-flash")
    time.sleep(4.5)
    response = model.generate_content(f"""
    Below are some examples showing a question, job title, search term, and answer format:

    Question: Give This location in English.
    Term: Гамбург, Германия 
    Answer: Hamburg , Germany

    Question: Give This location in English.
    Term: برلین
    Answer: Berlin , Germany


    Question: Give This location in English.
    Term: {location}
    Answer: 
    """)
    return response.text.strip()

