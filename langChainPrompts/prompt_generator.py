from langchain_core.prompts import PromptTemplate
#creating a prompt template
template = PromptTemplate(
    template= """
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
    """,
    input_variables=["paper_input","style_input","length_input"],
    validate_template= True
)

template.save("template.json")

#run : python prompt_generator.py 
#we get:  template.json file 