from langchain_community.document_loaders import TextLoader
from langchain_openai import  ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate

load_dotenv()

model = ChatOpenAI()
prompt = PromptTemplate(
    template= "Write the summary for the following text - \n {text}",
    input_variables=['text']
)
parser = StrOutputParser()
loader = TextLoader(ai.txt,encoding="utf-8")
docs =  loader.load()
print(type(docs))#list
print(type(docs[0]))#document
print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser
result = chain.invoke({'text':docs[0].page_content})
print(result.content)