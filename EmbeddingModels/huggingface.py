from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
load_dotenv(override=True)


embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3",  encode_kwargs={"normalize_embeddings": True},)

query_embedding = embeddings.embed_query("What is apple ?")
doc_embeddings = embeddings.embed_documents(
    [
        "what is benifits of apple ?",
        "apple is a healthy fruit.",
    ]
)

print("query_embedding:", query_embedding)
print("=====================================================================================================")
print("=====================================================================================================")
print("=====================================================================================================")
print("=====================================================================================================")
print("=====================================================================================================")
print("doc_embeddings:", doc_embeddings)