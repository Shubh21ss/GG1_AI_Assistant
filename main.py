from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import speech_recognition as sr
import io
import os

app = Flask(__name__, static_folder='www', static_url_path='')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return send_from_directory('www', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('www', path)

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        # Get audio data from request
        audio_file = request.files['audio']

        # Create a recognizer instance
        recognizer = sr.Recognizer()

        # Use AudioFile to read WAV data
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

            # Recognize speech
            try:
                text = recognizer.recognize_google(audio).lower()
                response_text = process_command(text)
                return jsonify({'success': True, 'transcript': text, 'response': response_text})
            except sr.UnknownValueError:
                return jsonify({'success': False, 'error': 'Could not understand audio'})
            except sr.RequestError as e:
                return jsonify({'success': False, 'error': f'Could not request results; {e}'})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def process_command(command):
    if 'hello' in command or 'hi' in command:
        return 'Hello! How can I help you today?'
    elif 'time' in command:
        from datetime import datetime
        now = datetime.now()
        return f'The current time is {now.strftime("%I:%M %p")}.'
    elif 'date' in command:
        from datetime import datetime
        now = datetime.now()
        return f'Today\'s date is {now.strftime("%B %d, %Y")}.'
    elif 'weather' in command:
        return 'I\'m sorry, I don\'t have access to weather information right now.'
    elif 'name' in command or 'who are you' in command:
        return 'My name is GG1, your voice assistant.'
    elif 'bye' in command or 'goodbye' in command:
        return 'Goodbye! Have a great day!'
    else:
        return 'I\'m sorry, I didn\'t understand that. Can you please repeat?'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)