import os
import argparse

from src.notion import api
from src.chatgpt.utils import num_tokens_from_messages

from src.summarizer.summarize import Summarizer

def nc_parser():
    """

    """
    parser = argparse.ArgumentParser(description='Optional argparse way to run scripts for now',
                                     epilog="Useful for running modules independently. See src/main.py for example."
                                            "The idea is to have a single entry point for all scripts."
                                            "1. You can ideally run just the notion API to get the pages and content as json"
                                            "2. You can run a summarizer to get the summary of the content."
                                            "3. You can run a query based retrieval system from embeddings.")
    
    parser.add_argument('-o', '--option', type=str, default='summary',
                        help='either put in "notion" or put in "summary"')
    parser.add_argument('-c', '--custom', type=bool, default='Find my summary',
                        help='Maybe can be used for piping logging into into the terminal, and set levels')
    return parser



if __name__ == "__main__":
    parser = nc_parser()
    args = parser.parse_args()
    print(args.option)

    if args.option == 'summary':
        sumy = Summarizer()
        sumy.summarize("This is a test")
    else:
        search_results = api.search_notion_pages()
        api.process_search_results(search_results)