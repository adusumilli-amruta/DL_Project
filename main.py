import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
import torch
from langchain.prompts import PromptTemplate
import os
from langchain_groq import ChatGroq

os.environ["GROQ_API_KEY"] = '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'


if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=2500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_texts(texts=text_chunks, embedding=embeddings, persist_directory="chroma_db")
    return vectorstore



def get_conversation_chain(vectorstore):

    llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)

    # Set up conversation memory and retrieval chain
    memory = ConversationBufferMemory(memory_key='chat_history',output_key="answer", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain




def handle_userinput(user_question):
    prompt = f"""
    You are an AI assistant trained to provide short and sweet answers to user questions. Your responses should be:
    
    1. Concise: Use as few words as possible while retaining clarity.
    2. Accurate: Ensure no critical information or key words are missed.
    3. Friendly: Use a polite and approachable tone.

    Always include key terms or phrases relevant to the user's question.

    User Question: {user_question}

    Your Short and Sweet Answer:
    """



    response = st.session_state.conversation({'question': prompt})
    # chat_history = response['chat_history']
    # print(response['question'])

    st.session_state.chat_history.append({'question':user_question,'answer':response['answer']})

    for i,message in enumerate(st.session_state.chat_history):
        print(f'chat{i}: ',message)
        print(len(st.session_state.chat_history))
        st.write(user_template.replace(
                "{{MSG}}", message['question']), unsafe_allow_html=True)
        st.write(bot_template.replace(
                "{{MSG}}", message['answer']), unsafe_allow_html=True)


# Function to read a local PDF file and extract its text
def read_pdf(file_path):
    try:
        # Create a PDF reader object
        reader = PdfReader(file_path)
        
        # Extract text from each page
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text() + "\n"
        
        return pdf_text
    except Exception as e:
        return f"Error reading PDF: {e}"


def main():
    load_dotenv()
    st.set_page_config(page_title="DocBot",
                       page_icon="🩺")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    

    st.header("DocBot for all your queries about all your questions about Radiology(contextual) 🩺")
    user_question = ""
    user_question = st.text_input('Ask DocBot...')
    if user_question:
        handle_userinput(user_question)

    file_path = "/teamspace/studios/this_studio/DL/Project/amruta_chatbot/Radiology_for_Medical_Students.pdf"  
    pdf_content = read_pdf(file_path)

    # get the text chunks
    text_chunks = get_text_chunks(pdf_content)

    # create vector store
    vectorstore = get_vectorstore(text_chunks)

    # create conversation chain
    st.session_state.conversation = get_conversation_chain(vectorstore)


if __name__ == '__main__':
    main()


