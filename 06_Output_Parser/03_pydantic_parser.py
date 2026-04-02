from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of person')
    city: str = Field(description='Name of the city person belogns to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='generate the name, age and city of a unique {place} person  \n {format_instruction}',
    input_variables=['palce'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'place': 'pakistan'})
# result = model.invoke(prompt)
# parser_result = parser.parse(result.content)
# print(parser_result)

# use chain
chain = template | model | parser
result = chain.invoke({'place': 'India'})
print(result)