from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.prompts import ChatPromptTemplate
from config.settings import EMBEDDING_MODEL, LANGUAGE_MODEL, PROMPT_TEMPLATE

DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)

def index_documents(chunks):
    DOCUMENT_VECTOR_DB.add_documents(chunks)

def find_related_documents(query):
    return DOCUMENT_VECTOR_DB.similarity_search(query)

def generate_answer(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    chain = prompt | LANGUAGE_MODEL
    return chain.invoke({
        "user_query": query,
        "document_context": context
    })
