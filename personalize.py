from langchain.llms import OpenAI as LangChainOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

def personalize_listing(listing, preferences):
    template = (
        "You are a real estate copywriter. Buyer preferences:\n{preferences}\n\n"
        "Rewrite this property listing:\n{listing}\n\n"
        "Emphasize details relevant to the buyer, keeping factual accuracy."
        "Result should be 3-5 sentences."
    )
    prompt = PromptTemplate(input_variables=["listing", "preferences"], template=template)
    llm = LangChainOpenAI(
        model_name="gpt-3.5-turbo",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        openai_api_base=os.getenv("BASE_URL")
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"listing": listing, "preferences": preferences})
