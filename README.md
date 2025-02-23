# INFO-5940
# Files Q&A with OpenAI

## Prerequisites
- Docker
- Docker Compose
- Visual Studio Code with Remote - Containers extension
- OpenAI API Key

## Running the Application

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/shar-sun/INFO5940_A1
    cd A1_xs77
    ```

2. **Open in VS Code with Docker**:
    Open VS Code, navigate to the A1_xs77 folder.
    Open the Command Palette and search for: `Remote-Containers: Reopen in Container`
    Select this option. VS Code will build and open the project inside the container.


3. **Create a `.env` File**:
    Create a `.env` file in the project folder with the following content:
    ```env
    OPENAI_API_KEY=your-api-key-here
    OPENAI_BASE_URL=your-api-base-url-here
    TZ=your-timezone-here
    ```

4. **Reopen in Container**:
    Press `F1`, then select `Remote-Containers: Reopen in Container`. This will build the Docker container and open the project inside the container.

5. **Run the Application**:
    Open a terminal in Visual Studio Code and run the following command:
    ```bash
    streamlit run chat_with_pdf.py
    ```

6. **Upload a File and Ask Questions**:
    Open your browser and navigate to the URL provided by Streamlit. Use the file upload interface to upload `.txt` and `.pdf` files and ask questions about the content.

## Notes
- Ensure that Docker and Docker Compose are installed and running on your machine.
- The `.env` file should contain the necessary environment variables for your application.
