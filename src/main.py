from src.notion import api

if __name__ == "__main__":
    search_results = api.search_notion_pages()
    api.process_search_results(search_results)