
# Retrieval Grader Project

## Overview
This project is designed to grade the relevance of retrieved documents based on a user's question using a binary scoring system. It leverages the `langchain_openai` library to interact with OpenAI's GPT-3.5-turbo model.

## Project Structure
- `graph/chains/retrieval_grader.py`: Contains the `RetrievalGrader` class and the logic to create a grading chain using OpenAI's language model.
- `main.py`: Entry point of the application. Handles user input and invokes the grading chain.
- `data_seeder/mongo_db_seeder.py`: Contains the logic to load data into the application.
- `graph/graph.py`: Contains the application logic to process user questions and interact with the grading chain.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Requirements
- Python
- pip
- `langchain_openai`
- `langchain_core`
- `python-dotenv`

## Setup
1. Clone the repository.
2. Create a virtual environment:
    ```sh
    python -m venv .venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
5. Create a `.env` file in the root directory and add your environment variables.

## Usage
1. Run the application:
    ```sh
    python main.py
    ```
2. Interact with the application using the following commands:
    - `load_data`: Load data into the application.
    - `exit`: Exit the application.
    - Any other input will be treated as a question for the retrieval grader.

## License
This project is licensed under the MIT License.
