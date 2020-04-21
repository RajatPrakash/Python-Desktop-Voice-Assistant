import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)  # voice id of Girl --TTS_MS_EN-US_ZIRA_11.0
# print(voices[0].id)  # voice id of Boy --TTS_MS_EN-US_DAVID_11.0
engine.setProperty('voice', voices[0].id)  # voice of David is set here for out project


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning Sir')
    elif 12 < hour <= 18:
        speak('Good AfterNoon Sir')
    else:
        speak('Good Evening Sir')
    speak('I am Up and Ready to help you!')


def Take():  # It takes input from user's Mircophone and convert it into string
    r = sr.Recognizer()  # this recognizer class will actually help our code to under our language

    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 3000
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        #  print(f'User said {query} \n')

    except Exception as e:
        print(e)
        print('Say that Again .......')
        return 'None'

    return query


if __name__ == '__main__':
    WishMe()
    while True:
    query = TakeCommand().lower()

    #  Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentence = 3)
            speak('According to Wikipedia')
            speak(results)




