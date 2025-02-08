import time

import google.generativeai as genai

from JobSpy.src.jobspy.scrapers.utils import create_logger
from credential import Credential

logger = create_logger("llm")


def batch_process(func, items, batch_size=15, sleep_time=50):
    """
    Processes a list of items in batches, applying the given function.

    Args:
        func (callable): The function to apply to each item in the batch.
        items (list): The list of items to process.
        batch_size (int): The number of items to process per batch.
        sleep_time (int): The time to sleep between batches, in seconds.

    Returns:
        list: A list of results from applying the function to each item.
    """
    results = []
    total_items = len(items)
    num_batches = (total_items + batch_size - 1) // batch_size  # ceil(total_items / batch_size)

    for batch_index in range(num_batches):
        start_index = batch_index * batch_size
        end_index = min(start_index + batch_size, total_items)
        batch = items[start_index:end_index]

        for item in batch:
            if isinstance(item, tuple):
                # If items are tuples, unpack them as arguments to the function
                result = func(*item)
            else:
                # Otherwise, pass the item directly
                result = func(item)
            results.append(result)

        # Sleep after every batch except the last one
        if batch_index < num_batches - 1 and len(batch) == batch_size:
            print(f"Processed batch {batch_index + 1} of {num_batches}. Sleeping for {sleep_time} seconds.")
            time.sleep(sleep_time)

    return results


def validate_job_title(job_title, search_term, try_count=1):
    cred = Credential()
    genai.configure(api_key=cred.get_google_api())
    model = genai.GenerativeModel("gemini-2.0-flash")
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
