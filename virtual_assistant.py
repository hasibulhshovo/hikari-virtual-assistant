import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
hikari = pyttsx3.init()
voices = hikari.getProperty('voices')
hikari.setProperty('voice', voices[1].id)

def talk(text):
    hikari.say(text)
    hikari.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Device is listening.....!')
            voice = listener.listen(source)
            com = listener.recognize_google(voice)
            com = com.lower()
            if 'hikari' in com:
                com = com.replace('hikari', '')
    except:
        pass
    return com


def run_hikari():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 3)
        talk(info)
    elif 'bye bye' in command:
        talk('Allah Hafiz. Take Care!')
        return 0
    else:
        talk('Not recognizing what you are saying. Let me search it for you.')
        pywhatkit.search(command)

while True:
    d = run_hikari()
    if d == 0:
        break