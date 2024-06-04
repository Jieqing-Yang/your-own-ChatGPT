import openai
import os
import sys
import time
from datetime import datetime
from dotenv import load_dotenv, find_dotenv

# Load API key from environment variable
def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.getenv('OPENAI_API_KEY')

openai.api_key = get_openai_key()

if openai.api_key is None:
    print("API key is missing. Please set the OPENAI_API_KEY environment variable.")
    sys.exit(1)

# Function to get GPT-3 response
def get_response(prompt, history):
    """
    Function to get response from OpenAI's GPT model.

    Parameters:
    - prompt (str): The input prompt/question from the user.
    - history (list): A list of message dictionaries representing the conversation history.

    Returns:
    - str: The response from the GPT model.
    
    Explanation of Parameters:
    - messages (list): A list of message dictionaries, where each dictionary contains:
        - role (str): The role of the message sender. It can be:
            - "system": Provides context or instructions for the assistant.
            - "user": Represents the user's input.
            - "assistant": Represents the assistant's (GPT's) response.
        - content (str): The actual message content.
    - model (str): The model to use for generating responses. Options include:
        - "gpt-3.5-turbo": A fast and capable model suitable for most tasks.
        - "text-davinci-003": Another powerful model with high capabilities (older than gpt-3.5-turbo).
    - max_tokens (int): The maximum number of tokens to generate in the response. 
    - temperature (float): Controls the randomness of the output.
        - Lower values (e.g., 0.2) make the output more deterministic.
        - Higher values (e.g., 0.8) make the output more random and creative.
    """
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    if history:
        messages += history
    messages.append({"role": "user", "content": prompt})

    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # You can choose models like "gpt-3.5-turbo" or "text-davinci-003"
                messages=messages,
                max_tokens=4096,  # Maximum tokens in the response
                temperature=0.7,  # Controls the randomness of the output
            )
            return response.choices[0].message["content"]
        except openai.error.OpenAIError as e:
            print(f"OpenAI API error: {e}")
            print("Retrying in 60 seconds...")
            time.sleep(60)

# Function to save conversation to file
def save_conversation(conversation, session_path):
    try:
        with open(session_path, 'a', encoding='utf-8') as file:
            file.write(conversation)
            file.write("\n\n")  # Add an empty line after each conversation block
    except Exception as e:
        print(f"Error saving conversation: {e}")

# Function to create a new session
def create_new_session():
    session_name = input("Enter the new session name: ")
    session_dir = "sessions"
    if not os.path.exists(session_dir):
        os.makedirs(session_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_path = os.path.join(session_dir, f"{session_name}_{timestamp}.md")
    return session_path

# Function to list existing sessions
def list_sessions():
    session_dir = "sessions"
    if not os.path.exists(session_dir):
        print("No session records found.")
        return []
    sessions = [f for f in os.listdir(session_dir) if f.endswith(".md")]
    if not sessions:
        print("No session records found.")
    else:
        print("Existing session records:")
        for i, session in enumerate(sessions, 1):
            print(f"{i}. {session}")
    return sessions

# Function to select a session
def select_session():
    sessions = list_sessions()
    if not sessions:
        return None
    session_index = int(input("Please select a session number: ")) - 1
    return os.path.join("sessions", sessions[session_index])

# Main function
def main():
    print("Welcome to the ChatGPT Q&A system!")
    print("1. Create a new session")
    print("2. Choose an existing session")
    choice = input("Please enter your choice: ")
    
    if choice == '1':
        session_path = create_new_session()
        history = []
    elif choice == '2':
        session_path = select_session()
        if not session_path:
            print("No valid session available for selection.")
            return
        try:
            with open(session_path, 'r', encoding='utf-8') as file:
                history_lines = file.readlines()
                history = []
                for line in history_lines:
                    if line.startswith("You: "):
                        history.append({"role": "user", "content": line[4:].strip()})
                    elif line.startswith("ChatGPT: "):
                        history.append({"role": "assistant", "content": line[9:].strip()})
        except Exception as e:
            print(f"Error reading session file: {e}")
            return
    else:
        print("Invalid choice.")
        return
    
    print("Type 'exit' to end the conversation.")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Thanks for using, goodbye!")
                break
            history.append({"role": "user", "content": user_input})
            response = get_response(user_input, history)
            print(f"ChatGPT: {response}\n")
            history.append({"role": "assistant", "content": response})
            save_conversation(f"You: {user_input}\n\n ChatGPT: {response}\n", session_path)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
