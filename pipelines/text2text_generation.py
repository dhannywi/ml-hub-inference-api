from langchain import PromptTemplate, LLMChain
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
from utils import load_model, load_tokenizer

def get_answer(model_id, question:str) -> str:
    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["question"])

    pipe = pipeline(
        "text2text-generation",
        model=load_model(model_id),
        tokenizer=load_tokenizer(model_id),
        max_length=100
    )
    
    local_llm = HuggingFacePipeline(pipeline=pipe)
    llm_chain = LLMChain(prompt=prompt, llm=local_llm)
    answer = llm_chain.run(question)
    return answer

# likely model is downloaded to directory:
#  ~/.cache
#print(get_answer('What is the capital of England?'))