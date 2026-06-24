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

I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast–whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera–the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware–why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
Pros:Insanely powerful processor (great for gaming and productivity)Stunning 200MP camera with incredible zoom capabilitiesLong battery life with fast chargingS-Pen support is unique and useful
Cons:Bulky and heavy–not great for one-handed useBloatware still exists in One UIExpensive compared to competitors

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


