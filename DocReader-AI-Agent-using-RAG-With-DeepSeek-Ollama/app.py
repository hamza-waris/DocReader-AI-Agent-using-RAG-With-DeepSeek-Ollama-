import streamlit as st
from controllers.document_controller import save_uploaded_file, load_pdf_documents, chunk_documents
from models.document_model import index_documents, find_related_documents, generate_answer
from views.ui import inject_custom_css, render_title

inject_custom_css()
render_title()

uploaded_pdf = st.file_uploader("Upload Research Document (PDF)", type="pdf")

if uploaded_pdf:
    path = save_uploaded_file(uploaded_pdf)
    raw_docs = load_pdf_documents(path)
    chunks = chunk_documents(raw_docs)
    index_documents(chunks)
    st.success("✅ Document processed. Ask your question below.")

    user_input = st.chat_input("Ask something from the document...")
    
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)

        with st.spinner("Thinking..."):
            related_docs = find_related_documents(user_input)
            response = generate_answer(user_input, related_docs)

        with st.chat_message("assistant", avatar="🤖"):
            st.write(response)
