from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model='tinyllama:latest')

# chat template
chat_template = ChatPromptTemplate.from_messages([
    ('system', 'you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# load chat history
chat_history = []
with open(r"C:\Users\MM0956\Documents\langchain_new\04_Prompts\data.txt", "r") as f:
    chat_history.extend(f.readlines())


# # print(chat_history)
# result = chat_template.invoke({'chat_history': chat_history, 'query': 'where is my refund'})
# print(result)


user_query = input("You: ")  # ya hardcode: 'where is my refund'

# Use chat template to create final prompt
final_prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': user_query
})

# Pass the prompt to the TinyLlama model
result = model.invoke(final_prompt)

# Print LLM response
print("AI:", result.content)

# Add AI response to chat history
chat_history.append(HumanMessage(content=user_query))
chat_history.append(AIMessage(content=result.content))

# print chat_history if u want