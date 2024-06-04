# Your own ChatGPT Q&A System

Welcome to the your own ChatGPT Q&A system! This is a simple command-line application that allows you to interact with OpenAI's GPT models for generating responses to your questions.

## Features

- **Create New Session**: Start a new conversation session and save it to a Markdown file.
- **Choose Existing Session**: Select an existing conversation session to continue the conversation.
- **Save Conversation**: Save the conversation history to a Markdown file for future reference.

## Requirements

- Python 3.x
- python-dotenv openai
- openai==0.28.0 (Compatibility issues with higher versions that are installed directly)
- OpenAI API Key

## Installation

1. Clone the repository
2. Install Python 3.x and the following dependencies:
    ```bash
    pip install python-dotenv openai
    pip install openai==0.28.0
3. Set up your OpenAI API key in the `.env` file in the project root directory
## Usage

1. Run the application or via the following command:

   ```bash
   python chatgpt_cli.py

2. Follow the prompts to create a new session or choose an existing session.

3. Start asking questions and interacting with the ChatGPT assistant.

4. Open and preview the markdown file to better view the current conversation.

## File Structure

* `chatgpt_cli.py`: Main script for running the command-line interface.
* `sessions/`: Directory to store conversation session files in Markdown format.
