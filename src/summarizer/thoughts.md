## Thoughts
Summary with a higher ROUGE-L score is important. But I'm not trying to train/finetune a new model.
I guess I need more control on inference parameters. Probably look at making it faster and more efficient.
I don't know if chunking is important for LED.

### Summarizing with equal focus on import stuff?
So a potential model needs to be able to retain important things, and depends on quality of dataset. Booksum 
looks to be a good way to do it. And textsum API could be useful. 

### Is chunking a good idea?
Umm one strategy could be a tree based combination of chunks and summarizing them. 
This seems like more of an engineering fix and can think about it later.

### Textsum and its limitations?
Umm, slow on CPU. Lets see, I need to dwelve deeper. If I have a CPU based inference, and I'm not inferencing on the fly. 
So class based implementation using the model trained by pszemraj in https://huggingface.co/pszemraj/led-base-book-summary 
could be a good idea. He has simplified the inference pipeline in textsum github repo, but we'll try to build our own
inference pipeline.

### Hosted inference API or on device?
Better idea would be to dockerize it. E
Dockers should be easier to deploy on cloud. I can potentially either expose an API or an event trigger based inference.

### Strategies for summarizing?

Longform text -> chunking -> summarizing -> combining summaries -> final summary

### Infra constraints?
I don't have a GPU, so I'll have to use CPU based inference. If required, we'll switch to GPU based inference.
Another idea is to use ggml, and a CPP based implementation, which I don't think exists. 
Can lambda be used for summarizing? Unless someone has finetuned it. 
Remember, the main goal was for use already used models. Keep it as simple as possible.
Probably chunking followed by summarizing is a good idea. Keeps the pipeline simple.
You can also potentially rely on joblib for parallelizing the summarization process.