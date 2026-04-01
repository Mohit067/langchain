from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=10)

documents = [
    "hello my name is mohit",
    "hello my name is rohit",
    "hello my name is sohit",
    "hello my name is sumit",
]
result = embedding.embed_documents(documents)

print(str(result))
