import requests
import time
import json
from src.utils.logger import get_logger
from config.settings import NOTION_KEY

logger = get_logger(__name__)

# TODO: ????? Move this to config/settings.py
headers = {
    "Authorization": "Bearer " + NOTION_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def search_notion_pages():
    """
    Description:
        Search for pages in Notion.
    Parameters:
        None
    Returns:
        search_response.json() (dict): The JSON response from the Notion API.

    TODO: 10.20.23: Add pagination support, and return a list of page IDs instead of the raw JSON response.
    TODO: 10:20:23: You also need to take in arguments for the search parameters.
    """
    try:
        logger.debug("Fetching pages from Notion")
        search_params = {"filter": {"value": "page", "property": "object"}}
        search_response = requests.post(
            f'https://api.notion.com/v1/search', 
            json=search_params, headers=headers
        )
        search_response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return search_response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching pages from Notion: {e}")
        return {}

def fetch_page_content(page_id):
    """
    Description:
        Fetch the content of a page in Notion.
    Parameters:
        page_id (str): The ID of the page to fetch.
    Returns:
        blocks_response.json() (dict): The JSON response from the Notion API.

    TODO: 10.20.23: Type check the page_id argument.

    """
    try:
        logger.debug(f"Fetching page content for page ID {page_id}")
        blocks_response = requests.get(
            f"https://api.notion.com/v1/blocks/{page_id}/children", 
            headers=headers
        )
        blocks_response.raise_for_status()
        return blocks_response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching page content from Notion for page ID {page_id}: {e}")
        return {}

def process_search_results(search_results):
    """
    Description:
        Process the search results from Notion.
        
        TODO: 10.20.23:
            You're going to want to change this function to do something more useful.
            For example, get page_id, title, url, and content from the search results.
            You can return it as a json dict, or pandas dataframe. Look for efficiency.
            Idea is to send it over for downstream tasks like converting the json 
            response into ada002 embeddings, inside a postgre database, etc.
    Parameters:
        search_results (dict): The search results from Notion.
    
    Returns:
        None (for now)
        
    """
    if not isinstance(search_results, dict):
        logger.error(f"Unexpected search results format: {search_results}")
        return

    if 'object' in search_results:
        logger.debug(f"Search results object: {search_results['object']}")
        if search_results['object'] == 'list':
            if not search_results.get('results'):
                logger.info("No pages are connected to the integration.")
            else:
                logger.debug(json.dumps(search_results, indent=2))
        elif search_results['object'] == 'error':
            logger.error(f"Error from Notion API: {search_results.get('message')}")
        else:
            logger.error(f"Unexpected response object from Notion API: {search_results['object']}")

    for page in search_results.get('results', []):
        if 'title' in page.get('properties', {}):
            title = page['properties']['title']['title'][0]['plain_text']
            page_id = page['id']
            url = page['url']
            
            logger.info(f"Page ID: {page_id} | Title: {title} | URL: {url}")
            
            blocks_data = fetch_page_content(page_id)
            for block in blocks_data.get('results', []):
                if block['type'] == 'paragraph' and block['paragraph']['rich_text']:
                    content = block['paragraph']['rich_text'][0]['plain_text']
                    logger.debug(content)
            logger.debug("-------")


# TODO: 10.20.23: Rate limits with respect to Notion API.
def handle_rate_limit(api_call, *args, **kwargs):
    """
    A wrapper function to handle rate limits for API calls using exponential backoff.

    Parameters:
    - api_call (function): The API call function to be executed.
    - *args, **kwargs: Arguments and keyword arguments to be passed to the api_call function.

    Returns:
    - The result of the API call function.

    # Example usage:
    # response = handle_rate_limit(search_notion_pages, arg1, arg2, kwarg1=value1)

    """
    max_retries = 5
    wait = 0.5  # start with a half-second wait

    for _ in range(max_retries):
        response = api_call(*args, **kwargs)
        
        # Check if the response indicates a rate limit error (status code 429)
        if response.status_code != 429:
            return response

        print(f"Rate limit exceeded. Waiting for {wait} seconds.")
        time.sleep(wait)
        wait *= 2  # double the wait time

    # If we've reached here, it means we've retried max_retries times and still have the error.
    # You can either raise an exception or return the last response.
    print("Max retries reached. Returning the last response.")
    return response

