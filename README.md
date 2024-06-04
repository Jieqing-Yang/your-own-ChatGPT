# ChatGPT Q&A System

Welcome to the ChatGPT Q&A system! This is a simple command-line application that allows you to interact with OpenAI's GPT models for generating responses to your questions.

## Features

- **Create New Session**: Start a new conversation session and save it to a Markdown file.
- **Choose Existing Session**: Select an existing conversation session to continue the conversation.
- **Save Conversation**: Save the conversation history to a Markdown file for future reference.

## Requirements

- Python 3.x
- OpenAI API Key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/chatgpt-qa-system.git 

2. Install the dependencies:
    ```bash
    cd chatgpt-qa-system
    pip install -r requirements.txt
3. Set up your OpenAI API key in the `.env` file in the project root directory
## Usage

1. Run the application:

   ```bash
   python chatgpt_cli.py

2. Follow the prompts to create a new session or choose an existing session.

3. Start asking questions and interacting with the ChatGPT assistant.

4. Open and previre the markdown file to better view the current conversation.

## File Structure

* `chatgpt_cli.py`: Main script for running the command-line interface.
* `sessions/`: Directory to store conversation session files in Markdown format.
