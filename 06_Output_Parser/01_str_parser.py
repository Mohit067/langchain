from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# model = ChatOllama(model='tinyllama:latest')
model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3,

)

# prompt 1
report_template = PromptTemplate(
    template='Write a short report on {topic}',
    input_variables=['topic']
)

# prompt 2
summary_template = PromptTemplate(
    template='Write a two line summary of the following text:\n{text}',
    input_variables=['text']
)

# prompt1 = report_template.invoke({'topic': 'black hole'})
# result1 = model.invoke(prompt1)

# prompt2 = summary_template.invoke({'text': result1.content})
# result2 = model.invoke(prompt2)

# print(result2.content)

parser = StrOutputParser()
chain = report_template | model | parser | summary_template | model | parser

result = chain.invoke({'topic': 'cricket'})
print(result)