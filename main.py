import speech_recognition as sr
from time import ctime
import webbrowser 
import time
import os
import playsound
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            accalado_speak(ask)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            accalado_speak("Sorry, I can't hear you")
        except sr.RequestError:
            accalado_speak("Sorry, my speech service is down")
        return voice_data


def accalado_speak(audio_string):
    tts = gTTS(audio_string,lang='en',tld='ca')
    r = random.randint(1,1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string) 
    os.remove(audio_file)

def respond(voice_data):
    if "hello" in voice_data:
        accalado_speak("Hi How are you ?")
    if "smile" in voice_data:
        accalado_speak("Because of your smile, you make life more beautiful")

    if "what's your name" in voice_data:
        accalado_speak( "Hi, I'm Accalado, I'm here to make everyone smile in his bad days")
    if "time" in voice_data:
        accalado_speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for ?")
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        accalado_speak("Here's what I found for " + search)

    if "location" in voice_data:
        location = record_audio("What's the location?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        accalado_speak("Here's the location of " + location)

    if 'exit' in voice_data:
        exit()


time.sleep(1)
accalado_speak('How can I help you ?')
while 1:
    voice_data = record_audio()
    respond(voice_data.lower())


