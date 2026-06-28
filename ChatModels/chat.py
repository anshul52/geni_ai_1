from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(override=True)  # Load environment variables from .env file


model = init_chat_model("gpt-5.5" , temperature=0.9 , max_tokens=200)
# print("model:", model)
# print("------------=================================")
response = model.invoke("write a short poem about the beauty of nature.")

print("response:", response.content)