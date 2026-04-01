# chat model with groq
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    max_tokens=2000,
    reasoning_format="parsed",
    timeout=None,
    max_retries=2,
    streaming=True
)

messages = [
    ("system", "You are a helpful assistant."),
    ("human", "Tell me about India's nature."),
]

# ai_msg = chat_model.invoke(messages)
for chunk in chat_model.stream(messages):
    print(chunk.content, end="", flush=True)



