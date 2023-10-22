import os
import argparse

from src.notion import api
from src.chatgpt.utils import num_tokens_from_messages

def url_parser():
    """

    """
    parser = argparse.ArgumentParser(description='Optional argparse way to run scripts for now',
                                     epilog="Useful for running modules independently. See src/main.py for example."
                                            "The idea is to have a single entry point for all scripts."
                                            "1. You can ideally run just the notion API to get the pages and content as json"
                                            "2. You can run a summarizer to get the summary of the content."
                                            "3. You can run a query based retrieval system from embeddings.")
    parser.add_argument('-u', '--urlpath', type=str, default=None,
                        help='path to an S3 audio file in .wav, or .webm format')
    parser.add_argument('-o', '--output', type=str, default='output',
                        help='path to store output')
    parser.add_argument('-v', '--verbose', type=bool, default=False,
                        help='Maybe can be used for piping logging into into the terminal, and set levels')
    return parser



if __name__ == "__main__":
    search_results = api.search_notion_pages()
    api.process_search_results(search_results)