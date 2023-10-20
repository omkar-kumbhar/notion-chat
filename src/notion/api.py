import requests
import json
from src.utils.logger import get_logger
from config.settings import NOTION_KEY

logger = get_logger(__name__)

headers = {
    "Authorization": "Bearer " + NOTION_KEY,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def search_notion_pages():
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


