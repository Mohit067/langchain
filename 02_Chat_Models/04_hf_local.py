# !pip install  langchain  langchain-core  langchain-openai  openai  langchain-anthropic  langchain-google-genai  google-generativeai  langchain-huggingface  transformers  huggingface-hub  python-dotenv  numpy  scikit-learn

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"temperature":0.5, "max_new_tokens":100,}
)

model = ChatHuggingFace(llm=llm)
# print(model.invoke("what is the capital of Inida?").content)


# here we are enabling streaming
from langchain_core.messages import HumanMessage

messages = [
    ('system', 'you are a helpful assistant, that give answer of user query and give answer in devnagri hindi'),
    ('user', "what is the capital of Inida")
]

for chunk in model.stream(messages):
    print(chunk.content, end="", flush=True)