# Author: Omkar Kumbhar
# reference: https://huggingface.co/pszemraj/led-base-book-summary

import torch
from transformers import pipeline
from joblib import Parallel, delayed
import os
# reference: https://stackoverflow.com/questions/62691279/how-to-disable-tokenizers-parallelism-true-false-warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

class Summarizer:
    def __init__(self):
        """
        Initialize the summarizer.
        NOTE: This is a heavy object, so it should be initialized once and reused.
        NOTE: Doesn't take any arguments yet, hardcoded for now.
        """
        self.hf_model = "pszemraj/led-base-book-summary"
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = pipeline(task="summarization", model=self.hf_model, device=self.device)

    def summarize(self,text):
        """Summarize a text."""
        result = self.model(text,
                    min_length=8,
                    max_length=256,
                    no_repeat_ngram_size=3,
                    encoder_no_repeat_ngram_size=3,
                    repetition_penalty=3.5,
                    num_beams=4,
                    do_sample=False,
                    early_stopping=True,
                )
        
        return result[0]['summary_text']
    
    def summarize_parallel(self,texts):
        """Summarize a list of texts in parallel."""
        result = Parallel(n_jobs=-1)(delayed(self.summarize)(text) for text in texts)
        return result
    
if __name__ == "__main__":
    sumy = Summarizer()
    paragraph = """
                Error 1: While installing urllib3, and it seems like it is compatible in python 3.10. Current fix is by downgrading. 
                Fix: https://github.com/imartinez/privateGPT/issues/482
                RuntimeError: Failed to import transformers.models.longt5.modeling_longt5 because of the 
                following error (look up to see its traceback):
                cannot import name 'DEFAULT_CIPHERS' from 'urllib3.util.ssl_' 
                (/Users/omkarkumbhar/opt/anaconda3/lib/python3.8/site-packages/urllib3/util/ssl_.py)
                
                Error 2: While generating summaries, it says np.object is something which doesn't exist. 
                Fix: python -m pip install numpy==1.23.5
                AttributeError: module 'numpy' has no attribute 'object'.
                `np.object` was a deprecated alias for the builtin `object`. To avoid this error in existing code, 
                use `object` by itself. Doing this will not modify any behavior and is safe. 
                The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
                https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
                """
    print('test single')
    res = sumy.summarize(paragraph)
    print(f'\n{res}\n')

    paragraph2 = """
                Once upon a time, in a small town, there lived a young boy named Max. Max had a loyal and playful dog named Charlie. 
                They were inseparable companions, always exploring the world together. One sunny day, Max and Charlie went on an 
                adventure to the nearby forest. They ran through the tall grass, chasing butterflies and laughing with joy. As they 
                ventured deeper into the woods, they stumbled upon a hidden path leading to a beautiful meadow. In the meadow, they 
                discovered a wounded bird with a broken wing. Max carefully picked up the bird and decided to take it home with them. 
                With Charlie's help, they built a cozy nest for the bird and provided it with food and water. Days turned into weeks, 
                and the bird began to heal under Max's care. It chirped happily, grateful for the love and attention it received. 
                Max and Charlie watched over the bird, delighted to see it regain its strength. One magical morning, the bird's wing 
                had fully healed. It fluttered its wings and soared into the sky, bidding farewell to Max and Charlie. Max looked up 
                with pride, knowing that they had helped the bird find its freedom. As Max and Charlie made their way back home, they 
                felt a sense of fulfillment and happiness in their hearts. They realized that their kind actions had brought joy not 
                only to the bird but also to themselves. From that day forward, Max and Charlie continued their adventures, 
                spreading love and kindness wherever they went. Their bond grew stronger, and they lived happily ever after, 
                cherishing the memories of their extraordinary journey together.The End.
                """
    print('test parallel')
    res = sumy.summarize_parallel([paragraph,paragraph2])
    print(f'\n{res}\n')
