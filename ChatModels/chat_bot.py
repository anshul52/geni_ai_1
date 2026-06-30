from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv(override=True)  # Load environment variables from .env file


model = init_chat_model("gpt-5.5" , temperature=0.9)

message = [
    SystemMessage(content="You are a funny assistant."),
]

print("====================Welcome to Bot , type 0 to exit====================")

while True:
    prompt = input("you : ")
    if prompt == "0":
        print("Exiting the chat. Goodbye!" ,message)
        break
    message.append(HumanMessage(content=prompt))
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot :", response.content)