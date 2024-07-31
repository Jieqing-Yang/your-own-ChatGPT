This is a simple command-line application that allows you to interact with OpenAI's GPT models to generate responses to your questions.

## Features

- **Create New Session**: Start a new conversation session and save it to a Markdown file.
- **Choose Existing Session**: Select an existing conversation session to continue the conversation.
- **Save Conversation**: Save the conversation history to a Markdown file for future reference.

## Requirements

- VPN (if in mainland)
- Python 3.x (testing with 3.9)
- python-dotenv openai
- openai==0.28.0 (Compatibility issues with higher versions that are installed directly)
- OpenAI API Key

## Installation

1. Clone the repository
2. Install Python 3.x and the following dependencies:
    ```bash
    pip install python-dotenv openai
    pip install openai==0.28.0
Alternatively, you can create a virtual environment and run `pip install -r requirements.txt` in the virtual environment.

3. Set up your OpenAI API key in the `.env` file in the project root directory
## Usage

1. Run the application or via the following command:

   ```bash
   python chatgpt_cli.py

2. Follow the prompts to create a new session or choose an existing session.

3. Start asking questions and interacting with the ChatGPT assistant.

4. Open and preview the markdown file to better view the current conversation.

5. Input `exit` or press `Ctrl + c` to exit the application.

## File Structure

* `chatgpt_cli.py`: Main script for running the command-line interface.
* `sessions/`: Directory to store conversation session files in Markdown format.
