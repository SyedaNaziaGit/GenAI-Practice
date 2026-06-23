from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

#storing history 
chat_history = [
    SystemMessage(content="You are Helpful AI Assistant")
]

#using infinite loop
while True:
    user_input = input("You: ")
    #appending userinput in history
    chat_history.append(HumanMessage(content=user_input))
    #break the loop when user chooses exit
    if user_input == "exit":
        break
    
    result = model.invoke(chat_history)
    #appending res in chathistory 
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)