from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model ="claude-opus-4-8")
result =model.invoke("What is temperature in bengaluru today?")
print(result.content)