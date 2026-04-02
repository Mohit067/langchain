from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(model='tinyllama:latest')
# model = ChatOllama(model='llama3.2:3b', streaming=True)
# model = ChatOllama(model='tinyllama:latest', streaming=True)
#
messages =[
    SystemMessage(content='you are a helpfull assistance'),
    HumanMessage(content='tell me about cricket')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
# for chunk in model.stream(messages):
#     print(chunk.content, end="", flush=True)