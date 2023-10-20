import unittest
from unittest.mock import patch
from src.notion import api
from src.utils.logger import get_logger

class TestNotionAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = get_logger(__name__)
        cls.logger.info("Starting tests for Notion API")

    @patch('src.notion.api.requests.post')
    def test_search_notion_pages(self, mock_post):
        self.logger.info("Running test_search_notion_pages")
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {'object': 'list', 'results': []}
        mock_post.return_value = mock_response
        result = api.search_notion_pages()
        self.assertEqual(result, {'object': 'list', 'results': []})

    @patch('src.notion.api.requests.get')
    def test_fetch_page_content(self, mock_get):
        self.logger.info("Running test_fetch_page_content")
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {'results': []}
        mock_get.return_value = mock_response

        page_id = "sample_page_id"
        result = api.fetch_page_content(page_id)
        self.assertEqual(result, {'results': []})

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("Finished tests for Notion API")

if __name__ == '__main__':
    unittest.main()

# import unittest
# from unittest.mock import patch
# import logging
# from src.notion import api
# # from src.utils import logger
# from src.utils.logger import get_logger

# class TestNotionAPI(unittest.TestCase):
#     def setUp(self):
#         self.logger = get_logger(__name__)

#     @patch('src.notion.api.requests.post')
#     def test_search_notion_pages(self, mock_post):
#         self.logger.info("test_search_notion_pages")
#         mock_response = unittest.mock.Mock()
#         mock_response.json.return_value = {'object': 'list', 'results': []}
#         mock_post.return_value = mock_response
#         result = api.search_notion_pages()
#         self.assertEqual(result, {'object': 'list', 'results': []})

#     @patch('src.notion.api.requests.get')
#     def test_fetch_page_content(self, mock_get):
#         self.logger.info("test_fetch_page_content")
#         mock_response = unittest.mock.Mock()
#         mock_response.json.return_value = {'results': []}
#         mock_get.return_value = mock_response

#         page_id = "sample_page_id"
#         result = api.fetch_page_content(page_id)
#         self.assertEqual(result, {'results': []})

# if __name__ == '__main__':
#     logger = get_logger(__name__)

#     logger.debug("This is a debug message.")
#     logger.info("This is an info message.")
#     logger.warning("This is a warning message.")

#     unittest.main()
