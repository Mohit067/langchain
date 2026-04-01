# chat model with anthropic
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

Anthropic_Chat_LLM = ChatAnthropic(
    model="claude-sonnet-4-5-20250929",
    temperature=0.2, 
    max_tokens=1024,
    streaming=True
)

messages = [
    ("system", "You are a helpful assistant."),
    ("human", "Tell me about India's nature."),
]

for chunk in Anthropic_Chat_LLM.stream(messages):
    print(chunk.content, end="", flush=True)

