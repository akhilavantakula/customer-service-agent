from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()

def classify_intent(inquiry: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", google_api_key=os.getenv("GOOGLE_API_KEY"))
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Classify into: Technical Support, Product Feature Request, Sales Lead, Escalate. No explanation."),
        ("human", inquiry)
    ])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"input": inquiry}).strip()