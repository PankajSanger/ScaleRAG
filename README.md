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

# pdf loaders
1. pypdfloader
2. pymupdfloader
3. pdfminerloader
4. pdfplumberloader

which one to choose?
We are selecting pymupdfloader for our first interation because it is fast, mostly accurate and can handle most layouts. Our document has lot of text and diagrams and very few tables as well.

- After using pymupdfloader, it loads text perfectly, text from tables also (not the layout), but it is not loading images or diagrams. We need to enable extract_images and exract_tables parameter TRUE. This will loads text only from images.
