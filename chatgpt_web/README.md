# Your own ChatGPT Q&A System

Welcome to your own ChatGPT Q&A system! This is a web application that allows you to interact with OpenAI's GPT models to generate responses to your questions.

## Features

- **Create New Session**: Start a new conversation session and save it to a Markdown file.
- **Choose Existing Session**: Select an existing conversation session to continue the conversation.
- **Save Conversation**: Save the conversation history to a Markdown file for future reference.
- **Web Interface**: Interact with the GPT models using a web-based interface.

## Installation

1. Clone the repository
2. Install Python 3.x (tested with 3.9)
3. run `pip install -r requirements.txt` in `chatgpt_web` root directory
   
Alternatively, you can create a virtual environment and run `pip install -r requirements.txt` in the virtual environment in `chatgpt_web` root directory

4. Set up your OpenAI API key in the `.env` file in the project root directory

## Usage

1. Run the Flask application `app.py` or via the following command:

   ```bash
   python app.py

2. Create a new session or choose an existing session
   
3. Open your web browser and go to http://127.0.0.1:5000
   
4. Create a new session or choose an existing session

5. Start asking questions and interacting with the ChatGPT assistant

6. *!!! The functionality to change models in the web is still under testing and may not yet be operational*. If you want to change the model, please go to line 71 in `app.py`: 
`model = request.args.get('model', 'gpt-4o-mini-2024-07-18')`.
Modify the second parameter to the model you need. For example if you want to use "gpt-4o" model, you can modify the code to `model = request.args.get('model', 'gpt-4o')`. Please refer to the OpenAI API website for specific model strings.


## File Structure

* `app.py`: Main script for running the Flask web application.
* `templates/`: Directory containing HTML templates for the web interface.
* `static/`: Directory containing CSS and JavaScript files for the web interface.
* `uploads/`: Directory to store uploaded files.
* `sessions/`: Directory to store conversation session files in Markdown format.
* `README.md`: This file, providing an overview of the web version.
