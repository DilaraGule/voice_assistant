# Library for performing speech recognition, with support for several engines and APIs, online and offline.
# Çevrimiçi ve çevrimdışı çeşitli motorlar ve API'ler desteğiyle konuşma tanıma gerçekleştirmek için kitaplık.
import speech_recognition as sr

# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
# pyttsx3 , Python'da bir metinden konuşmaya dönüştürme kitaplığıdır. Alternatif kitaplıkların aksine çevrimdışı çalışır ve hem Python 2 hem de 3 ile uyumludur.
import pyttsx3 as pyt

# Sending Message to a WhatsApp Group or Contact
# Sending Image to a WhatsApp Group or Contact
# Converting an Image to ASCII Art
# Converting a String to Handwriting
# Playing YouTube Videos
# Sending Mails with HTML Code
# Install and Use
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyt.init()


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('Can you help me?')
            listener.adjust_for_ambient_noise(source)   # AMBİENT NOISE
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'helena' in command:
                command = command.replace('helena', '')
                print(command)

    except:
        pass

    return command


def run_helena():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)        # play on youtube

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)

    elif 'what is the' in command:
        information = command.replace('what is the', '')
        info = wikipedia.summary(information, 1)
        print(info)
        talk(info)

    elif 'who is' in command:
        information = command.replace('who is', '')
        info = wikipedia.summary(information, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'love you' in command:
        talk('I hate you')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk("I don't understand, sorry.")


while True:
    try:
        run_helena()
    except UnboundLocalError:
        talk('Have a good day. See you later.')
        break
