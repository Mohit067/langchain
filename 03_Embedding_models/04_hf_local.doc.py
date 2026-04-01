from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

documents = [
    "my name is mohit",
    "my name is mohit",
    "my name is mohit"
]

vector = embedding.embed_documents(documents)

print(vector)