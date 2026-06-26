from langchain_community.document_loaders import  WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import  ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate

load_dotenv()

model = ChatOpenAI()
prompt = PromptTemplate(
    template= "Answer the following question \n {question} from the following {text}",
    input_variables=['question','text']
)
parser = StrOutputParser()
url = "https://www.amazon.in/Samsung-Galaxy-Awesome-Black-Offers/dp/B0DYDS1MYD"
loader = WebBaseLoader(url)
docs = loader.load()
#print(len(docs))
#print(docs[0].page_content)
chain = prompt | model |  parser
result = chain.invoke('question':'What is storage of this phone?','text': docs[0].page_content)

print(result.content)