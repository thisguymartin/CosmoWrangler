from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain import LLMChain

def OpenAISearch(question):
    template = """Question: {question} """
    llm = OpenAI(temperature=0.9)

    prompt = PromptTemplate(
        input_variables=['question'],
        template=template,
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    chain_response = chain.run(question)
    
    return chain_response









