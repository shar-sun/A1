import streamlit as st
from openai import OpenAI
from os import environ
from doc_handler import DocumentHandler

# Initialize Document Handler
handler = DocumentHandler()

# Streamlit Interface
st.title("📝 Multi-File Q&A with OpenAI")
uploaded_files = st.file_uploader("Upload articles", type=("txt", "pdf"), accept_multiple_files=True)

question = st.chat_input(
    "Ask something about the uploaded articles",
    disabled=not uploaded_files,
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Ask something about the uploaded articles"}]

# Process uploaded files
if uploaded_files:
    uploaded_file_paths = []
    for uploaded_file in uploaded_files:
        file_path = f"./temp_{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        uploaded_file_paths.append(file_path)

    # Process and create vector store
    handler.upload_files(uploaded_file_paths)
    handler.create_vector_store()

# Display chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Process user's question
if question and uploaded_files:
    client = OpenAI(api_key=environ['OPENAI_API_KEY'])

    # Retrieve relevant document chunks
    relevant_chunks = handler.retrieve_relevant_chunks(question)
    context_text = "\n\n".join([chunk.page_content for chunk in relevant_chunks])

    # Append the user's question
    st.session_state.messages.append({"role": "user", "content": question})
    st.chat_message("user").write(question)

    # Generate a response using relevant chunks
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="openai.gpt-4o",
            messages=[
                {"role": "system", "content": f"Relevant excerpts from the documents:\n\n{context_text}"},
                *st.session_state.messages
            ],
            stream=True
        )
        response = st.write_stream(stream)

    # Append the assistant's response
    st.session_state.messages.append({"role": "assistant", "content": response})
