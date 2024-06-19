# Speech-to-Text Chatbot with OpenAI GPT-3.5

This repository contains a Python script (`main.py`) that demonstrates a speech-to-text chatbot powered by the OpenAI GPT-3.5 model. The bot listens to user input via a microphone, converts speech to text using SpeechRecognition, and then generates a response based on the user's input using the OpenAI API.

## Features

- Converts speech to text using SpeechRecognition.
- Utilizes the OpenAI GPT-3.5 model to generate text-based responses.
- Outputs the generated response using text-to-speech with pyttsx3.

## How it Works

1. The script (`main.py`) starts by listening to the user's speech input via the microphone.
2. It uses SpeechRecognition to convert the speech input into text (in Portuguese).
3. The text input is then used as a prompt for the OpenAI GPT-3.5 model.
4. The model generates a response based on the prompt.
5. The response is outputted both to the console and spoken aloud using pyttsx3.

## Requirements

- Python 3.x
- OpenAI API key (replace `"OPENAI-KEY"` in `main.py` with your actual API key)
- SpeechRecognition (`pip install SpeechRecognition`)
- pyttsx3 (`pip install pyttsx3`)
- openai (`pip install openai`)

## Usage

1. Clone this repository to your local machine.
2. Install the dependencies listed above.
3. Replace `"OPENAI-KEY"` in `main.py` with your OpenAI API key.
4. Run the script by executing `python main.py` in your terminal or command prompt.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
