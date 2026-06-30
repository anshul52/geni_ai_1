from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv(override=True)  # Load environment variables from .env file


model = init_chat_model("gpt-5.5" , temperature=0.9)

choice = int(input("tell me your mood : "))

if choice == 1:
    mood = "happy"
elif choice == 2:
    mood = "sad"
elif choice == 3:
    mood = "angry"
elif choice == 4:
    mood = "Roleplay as Donald Trump. Respond in a style inspired by his public speaking and communication mannerisms—confident, emphatic, and distinctive—without claiming to be him. Stay in character throughout the conversation while avoiding fabricated facts or impersonating real-world actions."

message = [
    SystemMessage(content=f"You are a {mood} assistant."),
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