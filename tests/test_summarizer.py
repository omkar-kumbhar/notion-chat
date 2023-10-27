import unittest
from src.summarizer.summarize import Summarizer
from src.utils.logger import get_logger

# TODO: Work on max_len for summarizer, if the input text is less than it. 
# 2023-10-24 12:39:13,379 - src.summarizer.summarize - INFO - Loaded model pszemraj/led-base-book-summary on device cpu
# Your max_length is set to 256, but your input_length is only 208. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=104)
# .2023-10-24 12:39:25,255 - src.summarizer.summarize - INFO - Logger src.summarizer.summarize created.
# 2023-10-24 12:39:25,255 - src.summarizer.summarize - INFO - Logger src.summarizer.summarize created.
# 2023-10-24 12:39:27,114 - src.summarizer.summarize - INFO - Loaded model pszemraj/led-base-book-summary on device cpu
# 2023-10-24 12:39:27,114 - src.summarizer.summarize - INFO - Loaded model pszemraj/led-base-book-summary on device cpu
# Your max_length is set to 256, but your input_length is only 211. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=105)
# Your max_length is set to 256, but your input_length is only 208. Since this is a summarization task, where outputs shorter than the input are typically wanted, you might consider decreasing max_length manually, e.g. summarizer('...', max_length=104)

class TestSummarizer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = get_logger(__name__)
        cls.logger.info("Starting tests for Summarizer")

    def setUp(self):
        self.summarizer = Summarizer()
        self.text1 = """
        Error 1: While installing urllib3, and it seems like it is compatible in python 3.10. Current fix is by downgrading. 
        Fix: https://github.com/imartinez/privateGPT/issues/482
        RuntimeError: Failed to import transformers.models.longt5.modeling_longt5 because of the 
        following error (look up to see its traceback):
        cannot import name 'DEFAULT_CIPHERS' from 'urllib3.util.ssl_' 
        (/Users/omkarkumbhar/opt/anaconda3/lib/python3.8/site-packages/urllib3/util/ssl_.py)
        """
        self.text2 = """
        Error 2: While generating summaries, it says np.object is something which doesn't exist. 
        Fix: python -m pip install numpy==1.23.5
        AttributeError: module 'numpy' has no attribute 'object'.
        `np.object` was a deprecated alias for the builtin `object`. To avoid this error in existing code, 
        use `object` by itself. Doing this will not modify any behavior and is safe. 
        The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
        https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
        """

    def test_summarize(self):
        text = self.text1
        summary = self.summarizer.summarize(text)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) < len(text))

    def test_summarize_parallel(self):
        texts = [
            self.text1,
            self.text2,
        ]
        summaries = self.summarizer.summarize_parallel(texts)
        self.assertEqual(len(summaries), len(texts))
        for i, summary in enumerate(summaries):
            self.assertIsInstance(summary, str)
            self.assertTrue(len(summary) < len(texts[i]))

if __name__ == '__main__':
    unittest.main()
