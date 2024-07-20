from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired
import openai
import os
from dotenv import load_dotenv

# Load API key from environment variable
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a secure secret key
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploads')
app.config['SESSION_FOLDER'] = os.path.join(app.root_path, 'sessions')

# Ensure the 'uploads' and 'sessions' directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['SESSION_FOLDER'], exist_ok=True)

class ChatForm(FlaskForm):
    prompt = TextAreaField('Your Question:', validators=[DataRequired()])
    file = FileField('Upload File (optional)')
    submit = SubmitField('Submit')

def get_response(prompt, history, model):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    if history:
        messages += history
    messages.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model=model,  # Use the selected model
        messages=messages,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message["content"]

def save_conversation(session_name, conversation):
    session_dir = app.config['SESSION_FOLDER']
    session_path = os.path.join(session_dir, f"{session_name}.md")
    with open(session_path, 'a', encoding='utf-8') as file:
        file.write(conversation)

def load_conversation(session_name):
    session_dir = app.config['SESSION_FOLDER']
    session_path = os.path.join(session_dir, f"{session_name}.md")
    history = []
    if os.path.exists(session_path):
        with open(session_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("You: "):
                    history.append({"role": "user", "content": line[4:].strip()})
                elif line.startswith("ChatGPT: "):
                    history.append({"role": "assistant", "content": line[9:].strip()})
    return history

@app.route('/', methods=['GET', 'POST'])
def index():
    sessions = [f[:-3] for f in os.listdir(app.config['SESSION_FOLDER']) if f.endswith('.md')]
    return render_template('index.html', sessions=sessions)

@app.route('/chat/<session_name>', methods=['GET', 'POST'])
def chat(session_name):
    form = ChatForm()
    history = load_conversation(session_name)
    model = request.args.get('model', 'gpt-4o-mini-2024-07-18')
    context = request.args.get('context', 'enabled')
    sessions = [f[:-3] for f in os.listdir(app.config['SESSION_FOLDER']) if f.endswith('.md')]

    if context == 'disabled':
        history = []  # Clear history if context is disabled

    if form.validate_on_submit():
        prompt = form.prompt.data
        file = form.file.data

        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
        
        response = get_response(prompt, history, model)
        
        history.append({"role": "user", "content": prompt})
        history.append({"role": "assistant", "content": response})

        if context == 'enabled':
            save_conversation(session_name, f"You: {prompt}\nChatGPT: {response}\n\n")

        return redirect(url_for('chat', session_name=session_name, model=model, context=context))

    return render_template('chat.html', form=form, history=history, session_name=session_name, sessions=sessions, model=model, context=context)

@app.route('/create_session', methods=['POST'])
def create_session():
    session_name = request.form.get('session_name')
    if session_name:
        session_path = os.path.join(app.config['SESSION_FOLDER'], f"{session_name}.md")
        if not os.path.exists(session_path):
            with open(session_path, 'w', encoding='utf-8') as file:
                file.write("")
    return redirect(url_for('chat', session_name=session_name))

if __name__ == '__main__':
    app.run(debug=True)
