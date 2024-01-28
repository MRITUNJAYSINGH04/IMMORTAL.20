import openai
import sys
from apikey import api_data
import pyttsx3
import speech_recognition as sr
import webbrowser

sys.path.append('C:\\Users\\singh\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages')

openai.api_key = api_data
completion = openai.Completion()

# Adding the personal assistant name and meaning
name = "Immortal"
meaning = "Mritunjay, which means Lord Shiva, the conqueror of death."

def Reply(question):
    prompt = f'Chando: {question}\n{name}: '
    response = completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Chando'], max_tokens=200)
    answer = response.choices[0].text.strip()
    return answer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, How are you? I'm {0}. My name means {1}".format(name, meaning))

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("Chando Said: {} \n".format(query))
    except Exception as e:
        print("Say That Again....")
        return "None"
    return query


if __name__ == '__main__':
    while True:
        query = takeCommand().lower()
        ans = Reply(query)
        print(ans)
        speak(ans)
        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        if 'open google' in query:
            webbrowser.open("www.google.com")
        if 'bye' in query:
            speak("Goodbye, have a nice day!")
            break
