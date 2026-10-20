## About the Project
In this project we will try to learn how can we scale a RAG chatbot with higher accuracy/output. Intially we will be selecting a 10 page pdf document and build out RAG chatbot and test it end-to-end. Then we start scaling it with a factor of 10x and maintain a higher accuracy.

## Dataset selection
We are taking a pdf document of 462 pages (advanced rag course notes from campusx). Reason for selection is that, document contains text, images, graphs, visualization and more. So it has all type of format in pdf form. It will be good for understanding and bulding a good RAG application.

# First iteration
We are taking first 10 pages of this document to build out skeleton app.

## Framework
We will be using *Langchain* for building this project. Reason is because langchain has ready made integrations with LLM providers, all components are build in (data loaders, chukers, retrivers, etc). Also it has integration with *Langsmith* for observability.

# Package Manager
We are using *uv* as package manager to install our langchain packages and other requirements because it is much faster that pip. Apart from this, uv has many advantages over pip like automatic virtual env, etc.

## Langsmith tracing
tracing enabled in langsmith to keep monitoring our actions

# repository created on github and intial commits are done

# pdf loaders
1. pypdfloader
2. pymupdfloader
3. pdfminerloader
4. pdfplumberloader

which one to choose?
We are selecting pymupdfloader for our first interation because it is fast, mostly accurate and can handle most layouts. Our document has lot of text and diagrams and very few tables as well.

- After using pymupdfloader, it loads text perfectly, text from tables also (not the layout), but it is not loading images or diagrams. We need to enable extract_images and exract_tables parameter TRUE. This will loads text only from images.

# Chunking strategy
since we are dealing with lot of text in the form of paragraphs, langchain's *Recursivecharactertextsplitter* works pretty good. We are using it in our first iteration.
Initial chunking done taking chunk_size 100 and chunk overlap 10. We will tweak these parameters later.

# Embbedding model
So to convert our text chunks into embedding vectors, we need to select a suitable embbedding model.
Few factors to keep in mind for EM selection:
1. Domain : Our document is currently in education/technology, but we will be going towards general purpose model so this application can be used for other document types in future.
2. Language : We need to work on english mainly.
3. Modality : Only for text
4. Context window : So currently we have a small context window because we are sending 100 chunk size text.
5. Embedding dimension & Storage tradeoff : 
6. Latency : 
7. Cost : 

I am referencing openrouter leaderboard (https://openrouter.ai/rankings/embeddings) for embedding model comparison.
- First i am going to the domain specific model and selecting Software & Technology. Reason is because our pdf is notes on advanced RAG concept.
- Openrouter has 37 models listed on it's leaderboard (https://openrouter.ai/models?fmt=cards&output_modalities=embeddings). 
- I have downloaded all the model details in the google sheet for comparison and selection (https://docs.google.com/spreadsheets/d/1_3lbrw7ZFlMggJWHikZ-cKY4wT5S1x2SRXj7PFmFxsk/edit?gid=726893074#gid=726893074)
- First i am shorting models based on cost (small to large). We have 19 models which are under $0.01 output cost. Out of these, only 6 models which are above 1B parameters, and i am selecting 3 models based on latency.
- First is perplexityPerplexity: Embed V1 0.6B , it has 123ms latency and it is free to use.
- Second is BAAI: bge-m3, it has 357ms latency and it is a 29.1B parameter model.
- Thirst is Qwen: Qwen3 Embedding 8B, with 203B parameters but it has latency of 1.1s.


## Embedding model eval
I am going to prepare a dataset of 10 questions here 
