from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L6-v2'
)

text = "my name is mohit"

vector = embedding.embed_query(text=text)

print(vector)