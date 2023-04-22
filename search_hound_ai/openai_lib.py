import typer
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain import LLMChain


"""
This function takes in a question as input and uses OpenAI's language model to generate a response.

Parameters:
- question (str): The question to be searched.

Returns:
- chain_response (str): The response generated by the language model.

Steps:
1. Create a template string with the input question.
2. Initialize an OpenAI language model with a temperature of 0.
3. Create a prompt template using the input question and the template string.
4. Initialize an LLMChain object with the language model and prompt template.
5. Run the LLMChain object with the input question.
6. Print the response generated by the LLMChain object.
7. Return the response generated by the LLMChain object.
"""

def OpenAISearch(question: str) -> str:
    template = """Search: {question} """
    llm = OpenAI(temperature=0)

    prompt = PromptTemplate(
        input_variables=['question'],
        template=template,
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    chain_response = chain.run(question)
    return chain_response
