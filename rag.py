from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
import os

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
data = Chroma(persist_directory="data/chroma_db", embedding_function=embeddings)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=data.as_retriever())

def search_knowledge_base(query: str) -> str:
    result = qa.invoke({"query": query})
    return result.get("result", "No relevant info found.")