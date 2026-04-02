from langchain_core.prompts import ChatPromptTemplate

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant of {domain} expert."),
    ("user", "Tell me about {topic}.")
])

result = chat_prompt.invoke({'domain' : 'mathmatics', 'topic': 'multiplication of 2 and 3'})

print(result)