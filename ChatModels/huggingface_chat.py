from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
load_dotenv(override=True)


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    temperature=0.7,
    # max_length=1024,
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("Who are you ?")
print("model--->", response.content)

