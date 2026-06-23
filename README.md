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

