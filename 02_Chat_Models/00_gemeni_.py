# chat model with google gemini
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

genai_LLM = ChatGoogleGenerativeAI(
    model="gemini-3-pro-preview",
    temperature=0.6,
    streaming=True,
    max_tokens=500
)

messages = [
    ("system", "You are a good translator who can understand the user query and give the answer in Devanagari Hindi."),
    ("human", "Explain the importance of the Internet in modern life.")
]

for chunk in genai_LLM.stream(messages):
    print(chunk.content, end="", flush=True)