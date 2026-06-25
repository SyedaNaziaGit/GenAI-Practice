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




