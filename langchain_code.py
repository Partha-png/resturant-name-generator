from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from openai_key import openai_key
import os

os.environ['OPENAI_API_KEY'] = openai_key

llms = OpenAI(temperature=0.7)

def generate_name(cuisine):
    # Chain 1 - Generating restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine}. Suggest me a name for it."
    )
    name_chain = prompt_template_name | llms

    # Chain 2 - Generating the menu items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest some menu items for {restaurant_name}."
    )
    food_chain = prompt_template_items | llms

    # Use RunnableSequence and fix key conflict
    chain = RunnableSequence(name_chain, food_chain)

    response = chain.invoke({"cuisine": cuisine})
    return response

if __name__ == "__main__":
    print(generate_name("indian"))
