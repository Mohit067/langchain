from langchain_cohere import CohereEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import os

os.environ["COHERE_API_KEY"] = "vlxlikpvFB9xqApmHScNa3VG7j3wdxVepqF179FS"

embedding = CohereEmbeddings(
    model="embed-multilingual-v3.0"
)

documents = [ 
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

user_query = "tell me about virat kohli"

doc_embedding = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(user_query)

similarities = cosine_similarity([query_embedding], doc_embedding)[0]

print(similarities)

index, score = sorted(list(enumerate(similarities)), key=lambda x: x[1])[-1]
print(user_query)
print(documents[index])
print("similarity : ", score)