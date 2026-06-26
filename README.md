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





