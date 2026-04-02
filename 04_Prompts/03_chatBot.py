from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
model = ChatOllama(model='llama3.2:3b', streaming=True)


chat_history = [
    SystemMessage(content='you are a helpfull AI assistance'),
    HumanMessage(content='')
]


# while(True):
#     user_input = input("You : ")

#     chat_history.append(HumanMessage(content=user_input))

#     if (user_input == "exit") or (user_input == "Exit"):
#         break

#     result = model.invoke(chat_history)

#     chat_history.append(AIMessage(content=result.content))

#     print("AI : ", result.content)


# here we use streaming

while(True):
    user_input = input("You : ")
    if(user_input == 'exit'):
        break

    chat_history.append(HumanMessage(content=user_input))

    print("AI : ", end="", flush=True)

    full_response = ""

    for chunk in model.stream(chat_history):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content

    print()  # new line after response

    chat_history.append(AIMessage(content=full_response))

print(chat_history)