# from langchain_ollama import ChatOllama
# from typing import TypedDict, Annotated

# model = ChatOllama(model='tinyllama:latest')


# model = ChatOllama(model='llama3.2:3b', streaming=True)

# # class Review(TypedDict):
# #     summary: str
# #     sentiment: str


# class Review(TypedDict):
#     summary: Annotated[str, "A brief summary about review"]
#     sentiment: Annotated[str, "Return the sentiment of the review either positive, negative or neutral"]

# structure_output = model.with_structured_output(Review)

# result = structure_output.invoke("""the hardware is greate, but the software feels bloated. There are too many pre-installed apps that i can't removed. also the ui is outdated compare to other brand hoping for a software update to fix this""")

# print(type(result))
# print(result['summary'])
# print(result['sentiment'])





from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated, Optional

model = ChatOllama(model='llama3.2:3b')

class Review(TypedDict):
    key_themes: Annotated[list[str], "write down all key themes discussed in the review in the list"]
    summary: Annotated[str, "a brief summary about given review"]
    sentiment: Annotated[str, 'a sentimet about given review']
    pros: Annotated[Optional[list[str]], "write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "write down all the cons inside a list"]

structure_output = model.with_structured_output(Review)

result = structure_output.invoke("""Samsung continues to impress with its [Model], offering a sleek design and vibrant display.
The Super AMOLED screen delivers deep blacks and bright colors, making videos and games a delight.
Performance is smooth thanks to the powerful processor and ample RAM, handling multitasking effortlessly.
Camera quality is impressive, with sharp photos in daylight and decent low-light performance.
Battery life is reliable, easily lasting a full day with moderate usage.
Software experience is smooth with One UI, though some pre-installed apps feel unnecessary.
Expandable storage and microSD support are a plus for heavy users.
The device feels premium, with a solid build and ergonomic design.

Pros:

Stunning AMOLED display

Strong performance and multitasking

Good camera quality

Reliable battery life

Expandable storage

Cons:

Some bloatware apps

Average low-light camera performance

Fast charging could be better

Overall, [Model] is a solid choice for users looking for a premium Samsung experience without major compromises.""")


print(type(result))
print(result)