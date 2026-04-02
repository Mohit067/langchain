from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

parser = JsonOutputParser()

template = PromptTemplate(
    template='give me the name, age and city of a unique person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)
# print(final_result)

# use chain instead of doing propt,result,final_result
chain = template | model | parser
result = chain.invoke({})

print(result)




# note -> json parser use krte time hame structuring ka schema khud se decide nhi kr skte h ye model khud hi decide krta h ham kuch nhi kr skte hai