# INFO-5940 Assignment: Files Q&A with OpenAI

This application allows users to upload `.txt` and `.pdf` documents and ask questions about their content using a conversational AI interface. It efficiently handles large documents by chunking them into smaller pieces and retrieves contextually relevant information to answer user queries.

---

## 🚀 Features

- 📄 **File Upload Functionality for `.txt` and `.pdf` Files**  
  Users can upload `.txt` and `.pdf` files for processing and analysis.

- 💬 **Conversational Interface with Document Content**  
  A chat interface that allows users to ask questions about the uploaded documents and receive relevant, context-aware responses.

- 📚 **Support for Multiple Documents**  
  Upload and interact with multiple documents simultaneously, with separate handling of each document's content.

- 📏 **Efficient Document Chunking**  
  Automatically breaks large documents into manageable chunks for faster processing and improved retrieval accuracy.

- 🔍 **Intelligent Information Retrieval**  
  Fetches accurate answers based on the specific context of the uploaded files using `LangChain`, `Chroma`, and `AzureOpenAIEmbeddings`.

---

## 🛠️ Prerequisites

- Docker
- Docker Compose
- Visual Studio Code with the **Remote - Containers** extension
- OpenAI API Key (for GPT-based querying)

---

## ⚙️ Running the Application

### 1. **Clone the Repository**

Clone the repository to your local machine:

```bash
git clone https://github.com/shar-sun/A1.git
cd A1
```

### 2. **Open in VS Code with Docker**

- Open **VS Code** and navigate to the `A1` folder.
- Open the Command Palette:
  - Press `Ctrl+Shift+P` on **Windows/Linux** or `Cmd+Shift+P` on **macOS**.
- Search for: `Remote-Containers: Reopen in Container` and select it.
- VS Code will build and open the project inside the Docker container automatically.

### 3. **Create a `.env` File**
    
Create a `.env` file in the project folder with the following content:

```env
OPENAI_API_KEY=your-api-key-here
OPENAI_BASE_URL=your-api-base-url-here
TZ=your-timezone-here
```

### 4. **Reopen in Container**

If you’re not already inside the container, press `F1`, then select `Remote-Containers: Reopen in Container`. This will build the Docker container and open the project inside the container.

### 5. **Run the Application**

Open a terminal in Visual Studio Code and run the following command:

```bash
streamlit run chat_with_pdf.py
```

### 6. **Upload Files and Ask Questions**

- Open the URL provided by **Streamlit** in your browser (usually `http://localhost:8501`).
- Upload `.txt` and `.pdf` files using the provided interface.
- Interact with the chatbot by asking questions related to the content of the uploaded documents.

---

## 🔄 Changes Made to Provided Configuration

### 📦 **Dependencies Added**

- Added `PyPDF2 = "*"` in `pyproject.toml` to enable PDF parsing functionality.

### 🐳 **Docker & DevContainer Modifications**

- Updated Docker configuration to include additional libraries needed for file processing (`PyPDF2` and `LangChain`).

---

## 📝 Notes

- Ensure Docker and Docker Compose are installed and running on your machine.
- The `.env` file must contain valid OpenAI API credentials for the application to function correctly.
- Make sure that the **Remote - Containers** extension in VSCode is properly configured.
