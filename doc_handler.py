# Required Libraries
import os
from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import AzureOpenAIEmbeddings
from langchain.vectorstores import Chroma
from PyPDF2 import PdfReader

# Document Handler Class
class DocumentHandler:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )
        self.documents = []  # List to store document chunks with metadata
        self.vector_store = None  # Chroma vector store instance

    def upload_files(self, file_paths: List[str]):
        for file_path in file_paths:
            extension = os.path.splitext(file_path)[1].lower()
            if extension == '.txt':
                text = self._read_txt(file_path)
            elif extension == '.pdf':
                text = self._read_pdf(file_path)
            else:
                raise ValueError(f"Unsupported file type: {extension}")
            self._process_text(text, file_path)

    def _read_txt(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def _read_pdf(self, file_path: str) -> str:
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text

    def _process_text(self, text: str, source_name: str):
        chunks = self.text_splitter.split_text(text)
        for chunk in chunks:
            self.documents.append({
                'content': chunk,
                'source': source_name
            })

    def create_vector_store(self):
        embeddings = AzureOpenAIEmbeddings(
            model="openai.text-embedding-3-large",
            azure_endpoint=os.getenv("OPENAI_BASE_URL"),
            chunk_size=1000
        )
        self.vector_store = Chroma.from_texts(
            [doc['content'] for doc in self.documents],
            embeddings,
            metadatas=[{'source': doc['source']} for doc in self.documents]
        )

    def retrieve_relevant_chunks(self, query: str, k: int = 5) -> List[Dict]:
        if not self.vector_store:
            raise ValueError("Vector store is not initialized.")
        results = self.vector_store.similarity_search(query, k=k)
        return results
