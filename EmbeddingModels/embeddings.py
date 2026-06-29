from dotenv import load_dotenv
load_dotenv(override=True)
from langchain_openai import  OpenAIEmbeddings


embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector = embeddings.embed_query("Hello world")

print("vector:", vector)