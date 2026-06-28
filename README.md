# GenAI-Practice
get keys for openAI
https://platform.openai.com/
get keys for anthropics' claude:
https://platform.claude.com/

gemini model -
https://ai.google.dev/
docs:
https://ai.google.dev/gemini-api/docs

#opensource 
HuggingFace
https://huggingface.co/

small lib:
hg - TinyLlama


Prompts are the input instructions or quiries given  to its  output
text based prompts
multimodal prompts- ex- image or sounds and text


how to design the prompts in langchain 
 streamlit run script.py

static prompt
dynamic prompt
prepare a template

Please summarize the research paper titled "{paper_input}" with the following specifications:

Explaination style:{style_input}
explaination  length :{length_input}
1. mathematical details:
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical  concepts using simple, intuitive code snippets  where applicable.
2. Analogies:
- Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with :"Insufficient Information available" instead of guessing
Ensure the summary is clear, accurate , and aligned with the provided style and length.

A PromptTemplate in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template. Instead of hardcoding prompts, PromptTemplate allows you to define placeholders that can be filled in at runtime with different inputs.
This makes it reusable, flexible, and easy to manage, especially when working with dynamic user inputs or automated workflows.
Why use PromptTemplate

   1. Default validation
   2. Reusable
   3. LangChain Ecosystem


Message Placeholder
A MessagesPlaceholder in LangChain is a special placeholder used inside a ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime.

Structured Output
In LangChain, structured output refers to the practice of having language models return responses in a well-defined data format (for example, JSON), rather than free-form text. This makes the model output easier to parse and work with programmatically.[Prompt] - Can you create a one-day travel itinerary for Paris?[LLM's Unstructured Response]Here's a suggested itinerary: Morning: Visit the Eiffel Tower.Afternoon: Walk through the Louvre Museum.Evening: Enjoy dinner at a Seine riverside café.[JSON enforced output] 
                 

[
  {"time": "Morning", "activity": "Visit the Eiffel Tower"},
  {"time": "Afternoon", "activity": "Walk through the Louvre Museum"},
  {"time": "Evening", "activity": "Enjoy dinner at a Seine riverside café"}
]

Why do we need Structured Output
Data Extraction
API building
Agents

.with_structured_output() 
maps a specific schema to a model invocation (model_invoke).
 The method forces the model to guarantee data conforms to one of three structural types:
TypedDict
Pydantic
json_schema

TypedDict
TypedDict is a way to define a dictionary in Python where you specify what keys and values should exist. It helps ensure that your dictionary follows a specific structure.
Why use TypedDict?

It tells Python what keys are required and what types of values they should have.

It does not validate data at runtime (it just helps with type hints for better coding).
-> simple TypedDict
-> Annotated TypedDict
-> Literal-> More complex 
 -> with pros and cons

Typed Dict is only for presentation purpose if validation is also needed then we can use pydantic


Pydantic is a data validation and data parsing library for Python. It ensures that the data you work with is correct, structured, and type-safe.

When to use what?

Use TypedDict if:
You only need type hints (basic structure enforcement).
You don't need validation (e.g., checking numbers are positive).
You trust the LLM to return correct data.

✅ Use Pydantic if:
You need data validation (e.g., sentiment must be "positive", "neutral", or "negative").
You need default values if the LLM misses fields.
You want automatic type conversion (e.g., "100" ➔ 100).
✅ Use JSON Schema if:
You don't want to import extra Python libraries (Pydantic).
You need validation but don't need Python objects.
You want to define structure in a standard JSON format.

🚀 When to Use What?
FeatureTypedDict ✅Pydantic 🚀JSON Schema 
🌍Basic structure✅✅✅
Type enforcement✅✅✅
Data validation❌✅✅
Default values❌✅❌
Automatic conversion❌✅❌
Cross-language compatibility❌❌✅

  with_structured_output ( method )
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
        [ json mode ]                function calling



Output Parsers
Output Parsers in LangChain help convert raw LLM responses into structured formats like JSON, CSV, Pydantic models, and more. They ensure consistency, validation, and ease of use in applications.

StrOutputParser

The StrOutputParser is the simplest output parser in LangChain. It is used to parse the output of a Language Model (LLM) and return it as a plain string.

content='A black hole is a region in space where gravity is so strong that nothing, not even light, can escape its pull. It is formed when a massive star collapses upon itself.' 
additional_kwargs={'refusal': None} 
response_metadata={'token_usage': {'completion_tokens': 37, 'prompt_tokens': 15, 'total_tokens': 52, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} 
id='run-a7b90203-58f8-47c5-a01b-01184b6aec14-0' 
usage_metadata={'input_tokens': 15, 'output_tokens': 37, 'total_tokens': 52, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}

JSON Output parser
 

StructuredOutputParser 
StructuredOutputParser is an output parser in LangChain that helps extract structured JSON data from LLM responses based on predefined field schemas.
It works by defining a list of fields (ResponseSchema) that the model should return, ensuring the output follows a structured format.



PydanticOutputParser
🔹 What is PydanticOutputParser in LangChain?PydanticOutputParser is a structured output parser in LangChain that uses Pydantic models to enforce schema validation when processing LLM responses.
 Why Use PydanticOutputParser?
✅ Strict Schema Enforcement – Ensures that LLM responses follow a well-defined structure.
✅ Type Safety – Automatically converts LLM outputs into Python objects.
✅ Easy Validation – Uses Pydantic's built-in validation to catch incorrect or missing data.
✅ Seamless Integration – Works well with other LangChain components.


Table ContentsChain |NameDescription|
LLMChainBasic -chain that calls an LLM with a prompt template.
SequentialChainChains -multiple LLM calls in a specific sequence.
SimpleSequentialChain- A simplified version of SequentialChain for easier use.
ConversationalRetrievalChainHandles - conversational Q&A with memory and retrieval.
RetrievalQAFetches - relevant documents and uses an LLM for question-answering.
RouterChainDirects -user queries to different chains based on intent
MultiPromptChainUses -different prompts for different user intents dynamically.
HydeChain (Hypothetical Document Embeddings)- Generates hypothetical answers to improve document retrieval.
AgentExecutorChainOrchestrates - different tools and actions dynamically using an agent.
SQLDatabaseChainConnects - to SQL databases and answers natural language queries.


Runnables Types:
Task Specific Runnables 
Runnable Primitives 

Definition: These are core LangChain components that have been converted into Runnables so they can be used in pipelines.
Purpose: Perform task-specific operations like LLM calls, prompting, retrieval, etc.
Examples:
ChatOpenAI → Runs an LLM model.
PromptTemplate → Formats prompts dynamically.
Retriever → Retrieves relevant documents.

hese are core LangChain components that have been converted into Runnables so they can be used in pipelines.
Purpose: Perform task-specific operations like LLM calls, prompting, retrieval, etc.Examples:ChatOpenAI → Runs an LLM model.PromptTemplate → Formats prompts dynamically.Retriever → Retrieves relevant documents.

1. RunnableSequence
RunnableSequence is a sequential chain of runnables in LangChain that executes each step one after another, passing the output of one step as the input to the next.It is useful when you need to compose multiple runnables together in a structured workflow.

2. RunnableParallel
RunnableParallel is a runnable primitive that allows multiple runnables to execute in parallel.Each runnable receives the same input and processes it independently, producing a dictionary of outputs.


3. RunnablePassthrough
RunnablePassthrough is a special Runnable primitive that simply returns the input as output without modifying it.

4. RunnableLambda
RunnableLambda is a runnable primitive that allows you to apply custom Python functions within an AI pipeline.It acts as a middleware between different AI components, enabling preprocessing, transformation, API calls, filtering, and post-processing in a LangChain workflow.

5. RunnableBranch
RunnableBranch is a control flow component in LangChain that allows you to conditionally route input data to different chains or runnables based on custom logic.It functions like an if/elif/else block for chains — where you define a set of condition functions, each associated with a runnable (e.g., LLM call, prompt chain, or tool). The first matching condition is executed. If no condition matches, a default runnable is used (if provided).

LCEL
RunnableSequence ( r1, r2, r3 . . . )
[ r1 | r2 | r3 . . . ] → LCEL



Here is the complete, verbatim text extracted from all six images you have shared throughout this conversation, presented in order:
------------------------------
## Image 1: Limitations of PyPDF
Limitations:

* It uses the PyPDF library under the hood — not great with scanned PDFs or complex layouts.

| Use Case | Recommended Loader |
|---|---|
| Simple, clean PDFs | PyPDFLoader |
| PDFs with tables/columns | PDFPlumberLoader |
| Scanned/image PDFs | UnstructuredPDFLoader or AmazonTextractPDFLoader |
| Need layout and image data | PyMuPDFLoader |
| Want best structure extraction | UnstructuredPDFLoader |

------------------------------
## Image 2: DirectoryLoader
DirectoryLoader
27 March 2025 19:44
DirectoryLoader is a document loader that lets you load multiple documents from a directory (folder) of files.

| Glob Pattern | What It Loads |
|---|---|
| "**/*.txt" | All .txt files in all subfolders |
| "*.pdf" | All .pdf files in the root directory |
| "data/*.csv" | All .csv files in the data/ folder |
| "**/*" | All files (any type, all folders) |

** = recursive search through subfolders
------------------------------
## Image 3: Load vs Lazy load
Load vs Lazy load
27 March 2025 23:51
load()

* Eager Loading (loads everything at once).
* Returns: A list of Document objects.
* Loads all documents immediately into memory.
* Best when:
* The number of documents is small.
   * You want everything loaded upfront.

lazy_load()

* Lazy Loading (loads on demand).
* Returns: A generator of Document objects.
* Documents are not all loaded at once; they're fetched one at a time as needed.
* Best when:
* You're dealing with large documents or lots of files.
   * You want to stream processing (e.g., chunking, embedding) without using lots of memory.

------------------------------
## Image 4: WebBaseLoader
WebBaseLoader
28 March 2025 00:34
WebBaseLoader is a document loader in LangChain used to load and extract text content from web pages (URLs).
It uses BeautifulSoup under the hood to parse HTML and extract visible text.
When to Use:

* For blogs, news articles, or public websites where the content is primarily text-based and static.

Limitations:

* Doesn’t handle JavaScript-heavy pages well (use SeleniumURLLoader for that).
* Loads only static content (what’s in the HTML, not what loads after the page renders).

------------------------------
## Image 5: CSVLoader
CSVLoader
28 March 2025 01:48
CSVLoader is a document loader used to load CSV files into LangChain Document objects — one per row, by default.
------------------------------
RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses.Benefits of using RAG
Use of up-to-date information
Better privacy
No limit of document size

This diagram breaks down the four core components required to build a Retrieval-Augmented Generation (RAG) pipeline.
## Core Components of RAG

* Document Loaders: Import unstructured data from various sources like PDFs, HTML pages, or databases.
* Text Splitters: Break down large documents into smaller, manageable chunks to fit model context limits.
* Vector Databases: Store and index the text chunks as mathematical vectors for fast similarity searching.
* Retrievers: Fetch the most relevant text chunks from the database based on a user's query.

This diagram highlights common Document Loaders used in LangChain to ingest different file types into your RAG pipeline.
## LangChain Document Loaders

* TextLoader: Reads raw, unstructured plain text (.txt) files.
* PyPDFLoader: Extracts text content from Adobe PDF (.pdf) files.
* WebBaseLoader: Scrapes and parses HTML content directly from webpages.
* CSVLoader: Parses tabular data row-by-row from comma-separated values (.csv) files.

This image explains how LangChain Document Loaders standardize raw data into a consistent, reusable format.
## The Standardized Document Object
Regardless of the source file type (PDF, web page, or CSV), LangChain always outputs data as an array of standard Document objects. Every Document contains exactly two fields:

* page_content: A string containing the extracted raw text from the source.
* metadata: A dictionary containing structural details like the file name, page number, or URL.

## Code Blueprint
When you run a loader in LangChain, this is what the underlying data looks like:

from langchain_core.documents import Document
# Example of what a loaded document structure looks likedoc = Document(
    page_content="The actual text content extracted from the file.",
    metadata={"source": "filename.pdf", "page": 1}
)



This image outlines LangChain's TextLoader, which converts plain text files into structured Document objects.
## LangChain TextLoader Breakdown

* Definition: A simple document loader used to parse raw plain text (.txt) files.
* Use Cases: Best for importing chat logs, scraped text, interview transcripts, or source code snippets.
* Limitation: It cannot handle formatted media types like PDFs, CSVs, or raw HTML pages.

## Python Code Implementation
Here is how you implement TextLoader using modern LangChain practices:

from langchain_community.document_loaders import TextLoader
# Initialize the loader with the path to your fileloader = TextLoader("sample_data.txt")
# Load the file into a list of Document objectsdocuments = loader.load()
# Access the content and metadatafor doc in documents:
    print(f"Content: {doc.page_content[:100]}...")
    print(f"Source metadata: {doc.metadata}")

This image explains how PyPDFLoader extracts content from PDF files in LangChain, converting each page into its own Document object.
## LangChain PyPDFLoader Breakdown

* Function: Splits a single PDF file automatically by page.
* Output Structure: Creates an individual Document object for every page.
* Page Indexing: Stores zero-indexed page numbers inside the metadata dictionary.
* Limitations: Fails with scanned image PDFs.
* Layout Risks: Inaccurate with multi-column layouts or complex tables.

## Python Code Implementation
Here is how you use PyPDFLoader in your RAG setup:

# Required package: pip install pypdffrom langchain_community.document_loaders import PyPDFLoader
# Initialize with file pathloader = PyPDFLoader("manual.pdf")
# Extract and split by pagepages = loader.load()
# Inspect page metadatafor page in pages:
    print(f"Page Number: {page.metadata['page'] + 1}")
    print(f"Text Snippet: {page.page_content[:100]}")

Since PyPDFLoader struggles with scanned images or complex layouts, we can bypass this limitation. Would you like to see how to use PyMuPDF (Fitz) or OCR-based loaders for better layout handling?

This image lists alternative LangChain PDF loaders optimized for handling specific limitations like complex layouts, tables, and scanned text.
## Alternative PDF Loaders Matrix

| Use Case | Recommended Loader | Key Advantage |
|---|---|---|
| Simple, clean PDFs | PyPDFLoader | Fast and lightweight for standard text. |
| PDFs with tables/columns | PDFPlumberLoader | High precision for grid structures. |
| Scanned/image PDFs | UnstructuredPDFLoader or AmazonTextractPDFLoader | Uses OCR to extract non-selectable text. |
| Need layout and image data | PyMuPDFLoader | Fast extraction of text positions and embedded images. |
| Want best structure extraction | UnstructuredPDFLoader | Preserves structural elements like headings and lists. |

## Comparative Python Quickstart

# Choose the right loader based on your document structure:from langchain_community.document_loaders import (
    PDFPlumberLoader,
    PyMuPDFLoader,
    UnstructuredPDFLoader
)
# For complex tablestable_loader = PDFPlumberLoader("report_with_tables.pdf")
# For fast processing with layout preservationlayout_loader = PyMuPDFLoader("magazine_layout.pdf")
# For scanned documents requiring OCRscanned_loader = UnstructuredPDFLoader("scanned_invoice.pdf")


This image explains LangChain's DirectoryLoader, which targets and imports multiple files from a local directory or folder simultaneously.
## DirectoryLoader Glob Patterns
The loader utilizes glob syntax to filter exactly which files to ingest:

| Glob Pattern | Description |
|---|---|
| "**/*.txt" | Finds all .txt files in the root folder and all nested subfolders. |
| "*.pdf" | Finds all .pdf files only in the top-level root directory. |
| "data/*.csv" | Finds all .csv files specifically inside a folder named data/. |
| "**/*" | Finds every file of any extension across all folders. |

Note: The ** operator dictates a recursive search that drills down into every subfolder level.
## Python Code Implementation
Here is how to set up a DirectoryLoader to handle batch file importing:

from langchain_community.document_loaders import DirectoryLoaderfrom langchain_community.document_loaders import TextLoader
# Initialize to recursively pull all text filesloader = DirectoryLoader(
    path="./my_knowledge_base",
    glob="**/*.txt",
    loader_cls=TextLoader
)
# Ingest all matching files into a single listdocs = loader.load()
print(f"Successfully loaded {len(docs)} documents.")

This image explains the core architectural difference between standard eager loading and resource-efficient lazy loading in LangChain.
## Load vs. Lazy Load

* load(): Eagerly fetches every single document simultaneously, storing them as a structural list directly inside your system memory.
* lazy_load(): Uses on-demand streaming to pass data downstream as a memory-efficient Python generator, preventing out-of-memory crashes during large batch operations.

------------------------------
## Structural Comparison

| Feature | load() | lazy_load() |
|---|---|---|
| Strategy | Eager Loading (all at once) | Lazy Loading (on demand) |
| Return Type | list[Document] | Iterator[Document] (Generator) |
| Memory Cost | High (grows with dataset size) | Minimal (flat memory footprint) |
| Ideal For | Small, localized file batches | Massive datasets or continuous streaming |

------------------------------
## Python Implementation Example
Here is how you use both loading strategies using LangChain primitives:

from langchain_community.document_loaders import TextLoader
loader = TextLoader("massive_dataset.txt")
# 1. Eager Loading (Blocks until the entire file sits in memory)documents_list = loader.load()
print(f"Loaded {len(documents_list)} objects simultaneously.")
# 2. Lazy Loading (Streams documents one by one using a generator loop)document_generator = loader.lazy_load()
for doc in document_generator:
    # Process, chunk, or embed one document at a time without swelling RAM
    print(f"Processing chunk from source: {doc.metadata.get('source')}")



This image details LangChain's WebBaseLoader, which scrapes and parses static HTML web pages directly into structured data.
## WebBaseLoader Core Architecture

* Engine: Uses the BeautifulSoup library under the hood to parse raw HTML and isolate visible text content.
* Best Use Cases: Ideal for static blogs, documentation pages, or public news articles where text content renders strictly server-side.
* Major Limitations: Fails to parse client-side, JavaScript-heavy Single Page Applications (SPAs) like React or Vue sites. It cannot pull any text content that loads dynamically after the initial page renders.

------------------------------
## Python Code Implementation
Here is how you use WebBaseLoader along with the alternative SeleniumURLLoader recommended for dynamic pages:

# Required package: pip install beautifulsoup4 langchain-communityfrom langchain_community.document_loaders import WebBaseLoader
# 1. Parsing a Static Webpagestatic_loader = WebBaseLoader("https://example.com")static_docs = static_loader.load()

print("Static Content:")
print(static_docs[0].page_content[:100])

# 2. Handling Dynamic/JavaScript-Heavy Webpages (Alternative)# Required package: pip install seleniumfrom langchain_community.document_loaders import SeleniumURLLoader
dynamic_loader = SeleniumURLLoader(urls=["https://example.com"])dynamic_docs = dynamic_loader.load()

This image introduces LangChain's CSVLoader, which transforms structured tabular data into format-friendly documents for your LLM or RAG pipeline.
## CSVLoader Core Behavior

* Default Behavior: It processes your .csv file row-by-row, generating exactly one Document object per row.
* Text Formatting: Every cell value in a row is automatically paired with its corresponding column header, creating a clean string format inside the page_content field.
* Metadata Storage: The target row index number and data source path are appended directly to the metadata dictionary.

------------------------------
## Python Code Implementation
Here is how you initialize, read, and custom-configure the CSVLoader:

from langchain_community.document_loaders.csv_loader import CSVLoader
# 1. Standard Loading (Parses every column)loader = CSVLoader(file_path="user_data.csv")docs = loader.load()
# Print out the structured string representation of the first row
print(docs[0].page_content)

# 2. Targeted Loading (Specify a key column as the main source identifier)advanced_loader = CSVLoader(
    file_path="user_data.csv",
    csv_args={
        "delimiter": ",",
        "quotechar": '"',
        "fieldnames": ["ID", "Name", "Feedback"]
    },
    source_column="ID" # Overrides document source metadata with this cell value
)

========================================================

https://docs.langchain.com/oss/python/langchain/overview

https://docs.langchain.com/oss/python/integrations/document_loaders




Text Splitting
Text Splitting is the process of breaking large chunks of text (like articles, PDFs, HTML pages, or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively.



* Overcoming model limitations: Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.
* Downstream tasks - Text Splitting improves nearly every LLM powered task

| Task | Why Splitting Helps |
|---|---|
| Embedding | Short chunks yield more accurate vectors |
| Semantic Search | Search results point to focused info, not noise |
| Summarization | Prevents hallucination and topic drift |

* Optimizing computational resources: Working with smaller chunks of text can be more memory-efficient and allow for better parallelization of processing tasks.

------------------------------
## Diagram Flowchart

                 [Text Splitters]
                        |
      +-----------------+-----------------+-----------------+

      |                 |                 |                 |
      v                 v                 v                 v
[Length Based]  [Text Structure]  [Document Structure]  [Semantic Meaning]
                    [Based]             [Based]              [Based]

## Text Transcripts

* Text Splitters
* Length Based
* Text Structure Based
* Document Structure Based
* Semantic Meaning Based

(Top right handwritten diagram notes: text, vec)
------------------------------
## 1. Length Based Text Splitting
Original Text (Left Box):
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what's possible beyond our planet.
These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
------------------------------
Split Chunks (Right Box):

* Chunk 1:
Space exploration has led to incredible scientific discoveries. From landing on the Moon to explorin
* Chunk 2:
g Mars, humanity continues to push the boundaries of what's possible beyond our planet. These missi
* Chunk 3:
ons have not only expanded our knowledge of the universe but have also contributed to advancements in
* Chunk 4:
n technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniqu
* Chunk 5:
es trace their roots back to innovations driven by space programs.

------------------------------
.

## 2. Text-Structured Based
My name is Nitish
I am 35 years old
I live in Gurgaon
How are you
------------------------------

## 3. Document-Structured Based
Markdown Document (Left Column):
## 📘 Project Name: Smart Student Tracker
A simple Python-based project to manage and track student data,
...
## 🔍 Features

* Add new students with relevant info
* View student details
* Check if a student is passing
* Easily extendable class-based design

...
## 🛠️ Tech Stack

* Python 3.10+
* No external dependencies

------------------------------
Python Code Document (Right Column):

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # Grade is a float (like 8.5 or 9.2)

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def is_passing(self):
        return self.grade >= 6.0

# Example usagestudent1 = Student("Aarav", 20, 8.2)
print(student1.get_details())
if student1.is_passing():
    print("The student is passing.")else:
    print("The student is not passing.")

------------------------------

## 4. Semantic Meaning Based
------------------------------

What are Vector Stores

[ A vector store is a system designed to store and retrieve data represented as numerical vectors.
Key Features

   1. Storage – Ensures that vectors and their associated metadata are retained, whether in-memory for quick lookups or on-disk for durability and large-scale use.
   2. Similarity Search - Helps retrieve the vectors most similar to a query vector.
   3. Indexing - Provide a data structure or method that enables fast similarity searches on high-dimensional vectors (e.g., approximate nearest neighbor lookups).
   4. CRUD Operations - Manage the lifecycle of data—adding new vectors, reading them, updating existing entries, removing outdated vectors.

Use-cases

   1. Semantic Search
   2. RAG
   3. Recommender Systems
   4. Image/Multimedia search


Vector Store Vs Vector Database

• Vector Store
o Typically refers to a lightweight library or service that focuses on storing vectors (embeddings) and performing similarity search.
o May not include many traditional database features like transactions, rich query languages, or role-based access control.
o Ideal for prototyping, smaller-scale applications
o Examples: FAISS (where you store vectors and can query them by similarity, but you handle persistence and scaling separately).


• Vector Database
o A full-fledged database system designed to store and query vectors.
o Offers additional "database-like" features:
▪ Distributed architecture for horizontal scaling
▪ Durability and persistence (replication, backup/restore)
▪ Metadata handling
▪ Potential for ACID or near-ACID guarantees
▪ Authentication/authorization and more advanced security
o Geared for production environments with significant scaling, large datasets.


Vector Stores in LangChain
05 April 2025 17:41
• Supported Stores: LangChain integrates with multiple vector stores (FAISS, Pinecone, Chroma, Qdrant, Weaviate, etc.), giving you flexibility in scale, features, and deployment.
• Common Interface: A uniform Vector Store API lets you swap out one backend (e.g., FAISS) for another (e.g., Pinecone) with minimal code changes.
• Metadata Handling: Most vector stores in LangChain allow you to attach metadata (e.g., timestamps, authors) to each document, enabling filter-based retrieval.

[Code snippet]:
from_documents(...) or from_texts(...)
add_documents(...) or add_texts(...)
similarity_search(query, k=...)
Metadata-Based Filtering


Chroma Vector Store

[ Chroma is a lightweight, open-source vector database that is especially friendly for local development and small- to medium-scale production needs. ]
Chroma Tenancy and DB Hierarchy

* Tenant
* Database
   * Collection
      * Doc
         * Doc
      * Collection
      * Doc
         * Doc
      * Database
   * Collection
      * Doc
         * Doc
      * Collection
      * Doc
         * Doc





A retriever is a component in LangChain that fetches relevant documents from a data source in response to a user's query.
There are multiple types of retrievers
All retrievers in LangChain are runnables


This diagram visualizes how a LangChain retriever works to fetch data based on a user's input.
## Workflow Components

* Query: The user's input question or search phrase.
* Retriever: The core component that processes the incoming query.
* Data Source: The external repository (like a vector database or search engine) searched by the retriever.
* Document: The relevant text snippets found and returned to the system.


[LangChain](https://docs.langchain.com/oss/python/langchain/retrieval) features several types of retrievers categorized by their search strategies and data management behaviors: [1, 2] 
## 1. Vector Store-Backed Retrievers
These are the most common retrievers. They wrap a [Vector Store Integration](https://docs.langchain.com/oss/python/integrations/retrievers) (like Chroma, Pinecone, or FAISS) and use semantic similarity search to grab relevant document chunks. [1, 3] 

* VectorStoreRetriever: The standard baseline retriever that converts a query into an embedding and performs a basic distance calculation to find matching text chunks. [1, 4] 
* Maximum Marginal Relevance (MMR): Instead of just pulling the absolute closest matches, MMR optimizes for a balance of relevance and diversity. This prevents the LLM from receiving redundant data chunks that all say the same thing. [1] 

## 2. Advanced Context-Optimized Retrievers
These handle the "Goldilocks problem" of chunking by separating what is searched from what is sent to the LLM. [1] 

* Parent Document Retriever: Splits data into small child chunks for precise vector matching. Once a child chunk matches the query, it retrieves the larger parent document to give the LLM full, meaningful context. [1, 5] 
* MultiVector Retriever: Allows you to create multiple vectors pointing to a single document chunk. For example, you can embed summaries or hypothetical questions that the document answers rather than embedding the raw text itself. [1, 6] 

## 3. Hybrid and Smart Retrievers
These fuse different search strategies to deliver highly robust results. [1] 

* BM25 Retriever (Sparse Search): A keyword matching retriever that ignores semantic meaning but excels at finding exact product IDs, names, or rare technical terms. [1] 
* Ensemble Retriever: Combines results from multiple underlying retrievers (such as a hybrid of BM25 + a Vector Store) and uses Reciprocal Rank Fusion (RRF) to re-rank the final output. [1] 
* Self-Query Retriever: Uses a query-analysis LLM layer to inspect the user's prompt, parse out structural criteria, and automatically apply a metadata filter (e.g., separating the semantic text query from an execution filter like year == 2026). [1] 

## 4. Query-Transforming Retrievers

* Multi-Query Retriever: Uses an LLM to generate multiple variations of the user's query from different angles. It runs all variations against the database simultaneously to bypass poor search wording. [1, 7] 
* Contextual Compression Retriever: Wraps a standard retriever and uses a secondary model or a compressor to strip out unneeded noise from the fetched documents, passing only the exact target answers to the language model to save context tokens. [1, 5] 

Wikipedia Retriever
A Wikipedia Retriever is a retriever that queries the Wikipedia API to fetch relevant content for a given query.
🔧 How It Works

   1. You give it a query (e.g., "Albert Einstein")
   2. It sends the query to Wikipedia's API
   3. It retrieves the most relevant articles
   4. It returns them as LangChain Document objects


Vector Store Retriever
A Vector Store Retriever in LangChain is the most common type of retriever that lets you search and fetch documents from a vector store based on semantic similarity using vector embeddings.
⚙️ How It Works

   1. You store your documents in a vector store (like FAISS, Chroma, Weaviate)
   2. Each document is converted into a dense vector using an embedding model
   3. When the user enters a query:
   * It's also turned into a vector
      * The retriever compares the query vector with the stored vectors
      * It retrieves the top-k most similar ones
   

Maximal Marginal Relevance (MMR)
"How can we pick results that are not only relevant to the query but also different from each other?"
MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query.
🤔 Why MMR Retriever?
In regular similarity search, you may get documents that are:

* All very similar to each other
* Repeating the same info
* Lacking diverse perspectives

MMR Retriever avoids that by:

* Picking the most relevant document first
* Then picking the next most relevant and least similar to already selected docs
* And so on...

This helps especially in RAG pipelines where:

* You want your context window to contain diverse but still relevant information
* Especially useful when documents are semantically overlapping



Maximal Marginal Relevance (MMR)
10 April 2025 16:24
"How can we pick results that are not only relevant to the query but also different from ea
MMR is an information retrieval algorithm designed to reduce redundancy in the
results while maintaining high relevance to the query.
🧐 Why MMR Retriever?
In regular similarity search, you may get documents that are:

* All very similar to each other
* Repeating the same info
* Lacking diverse perspectives

MMR Retriever avoids that by:

* Picking the most relevant document first
* Then picking the next most relevant and least similar to already selected docs
* And so on...



Multi-Query Retriever
10 April 2025 16:26
Sometimes a single query might not capture all the ways information is phrased in your documents.
For example:
Query:
"How can I stay healthy?"
Could mean:

* What should I eat?
* How often should I exercise?
* How can I manage stress?

A simple similarity search might miss documents that talk about those things but don't use the word "healthy."

   1. Takes your original query
   2. Uses an LLM (e.g., GPT-3.5) to generate multiple semantically different versions of that query
   3. Performs retrieval for each sub-query
   4. Combines the unique results

"How can I stay healthy?"

   1. "What are the best foods to maintain good health?"
   2. "How often should I exercise to stay fit?"
   3. "What lifestyle habits improve mental and physical wellness?"
   4. "How can I boost my immune system naturally?"
   5. "What daily routines support long-term health?"

Contextual Compression Retriever
10 April 2025 16:29
The Contextual Compression Retriever in LangChain is an advanced retriever that improves retrieval quality by compressing documents after retrieval — keeping only the relevant content based on the user's query.
❓ Query:
"What is photosynthesis?"
📄 Retrieved Document (by a traditional retriever):
"The Grand Canyon is a famous natural site.
Photosynthesis is how plants convert light into energy.
Many tourists visit every year."
❌ Problem:

* The retriever returns the entire paragraph
* Only one sentence is actually relevant to the query
* The rest is irrelevant noise that wastes context window and may confuse the LLM

------------------------------
❌ Problem:

* The retriever returns the entire paragraph
* Only one sentence is actually relevant to the query
* The rest is irrelevant noise that wastes context window and may confuse the LLM

✅ What Contextual Compression Retriever does:
Returns only the relevant part, e.g.
"Photosynthesis is how plants convert light into energy."
⚙️ How It Works

   1. Base Retriever (e.g., FAISS, Chroma) retrieves N documents.
   2. A compressor (usually an LLM) is applied to each document.
   3. The compressor keeps only the parts relevant to the query.
   4. Irrelevant content is discarded.

✅ When to Use

* Your documents are long and contain mixed information
* You want to reduce costs and token usage
* You need to improve accuracy in RAG pipelines

More Retrievers

* BM25Retriever
* ParentDocumentRetriever
* TimeWeightedVectorRetriever
* SelfQueryRetriever
* EnsembleRetriever
* MultiVectorRetriever
* ArxivRetriever


https://docs.langchain.com/oss/python/integrations/providers/overview




https://docs.langchain.com/oss/python/integrations/providers/overview
