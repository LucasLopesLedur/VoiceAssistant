import openai
import speech_recognition as sr
import pyttsx3

microphone = sr.Recognizer()

machine = pyttsx3.init()

with sr.Microphone() as source:
    microphone.adjust_for_ambient_noise(source)
    print("Speak")
    audio = microphone.listen(source)

try:
    phrase = microphone.recognize_google(audio, language="pt-BR")
    print(phrase)

except sr.UnknownValueError:
    print("Sorry, I don’t understand.")

openai.api_key = "OPENAI-KEY"

model_engine = "text-davinci-003"

while True:
    prompt = phrase
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        temperature = 0.5,
    )
    response = completion.choices[0].text
    print(response)
    machine.say(response)
    machine.runAndWait()
    break