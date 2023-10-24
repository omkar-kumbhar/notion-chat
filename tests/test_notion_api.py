import unittest
from unittest.mock import patch, Mock
from src.summarizer.summarize import Summarizer
from src.utils.logger import get_logger

class TestSummarizer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = get_logger(__name__)
        cls.logger.info("Starting tests for Summarizer")

    @patch('src.summarizer.summarize.pipeline')
    def test_summarizer_initialization(self, mock_pipeline):
        self.logger.info("Running test_summarizer_initialization")
        mock_pipeline.return_value = Mock()
        try:
            summarizer = Summarizer()
            self.logger.info("Summarizer initialization test passed.")
        except Exception as e:
            self.logger.error(f"Summarizer initialization test failed. Error: {e}")
            self.fail("Failed to initialize the Summarizer.")

    @patch('src.summarizer.summarize.pipeline')
    def test_summarize(self, mock_pipeline):
        self.logger.info("Running test_summarize")
        mock_model = Mock()
        mock_model.return_value = [{'summary_text': 'This is a summary.'}]
        mock_pipeline.return_value = mock_model

        text = "This is a long text that needs to be summarized."
        summary = self.summarizer.summarize(text)
        
        self.assertEqual(summary, 'This is a summary.')
        self.logger.info("Summarize test passed.")

    @patch('src.summarizer.summarize.pipeline')
    def test_summarize_parallel(self, mock_pipeline):
        self.logger.info("Running test_summarize_parallel")
        mock_model = Mock()
        mock_model.return_value = [{'summary_text': 'This is a summary.'}]
        mock_pipeline.return_value = mock_model

        texts = ["This is a long text that needs to be summarized.", "Another text to summarize."]
        summaries = self.summarizer.summarize_parallel(texts)
        
        self.assertEqual(summaries, ['This is a summary.', 'This is a summary.'])
        self.logger.info("Summarize parallel test passed.")

    @classmethod
    def tearDownClass(cls):
        cls.logger.info("Finished tests for Summarizer")

if __name__ == '__main__':
    unittest.main()
