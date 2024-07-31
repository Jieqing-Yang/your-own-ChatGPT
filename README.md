# Your own ChatGPT Q&A System

Welcome to your own ChatGPT Q&A system! This is a application that allows you to interact with OpenAI's GPT models to generate responses to your questions. There are two versions, CLI and Web, and the corresponding guides can be found in the README in their respective folders.

## Features

- **Create New Session**: Start a new conversation session and save it to a Markdown file.
- **Choose Existing Session**: Select an existing conversation session to continue the conversation.
- **Save Conversation**: Save the conversation history to a Markdown file for future reference.

## Configuration

1. Clone the repository
2. Run `pip install -r requirements.txt` in `chatgpt_web` root directory. Alternatively, create a virtual environment and run `pip install -r requirements.txt` in the virtual environment in their respective project folders.
3. Set up your OpenAI API key in the `.env` file in the project root directory

## File Structure

* `chatgpt_cli/`:  Directory containing the CLI version of the ChatGPT Q&A system.
* `chatgpt_web/`:  Directory containing the web version of the ChatGPT Q&A system.
