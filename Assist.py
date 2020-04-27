import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pyaudio
import Restart as r
import webbrowser
import os
import Shut as s
import sys
import requests
import subprocess, io


sys.path.append('..')

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


# checking for internet connection of system

def connected_to_internet(url='http://www.google.com/', timeout=2):
    try:
        _ = requests.get(url, timeout=timeout)

    except requests.ConnectionError:
        speak("Sir, I think internet is off, I Need Internet Connectivity to work properly.")
        speak('Switching My Self Off, Good day')
        quit()


# It takes input from user's Mircophone and convert it into string

def Take():
    r = sr.Recognizer()  # this recognizer class will actually help our code to under our language

    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 3000
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said {query} \n')

    except Exception as e:
        print(e)
        # speak('Say that Again ...')
        connected_to_internet()
        return 'None'

    return query


if __name__ == '__main__':
    WishMe()
    #  Logic for executing task based on query
    ChromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(ChromePath))
    while True:
        query = Take().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=3)
            speak('According to Wikipedia')
            speak(results)
        elif 'who are you' in query:
            speak('I am your Personal Assistant designed to make your work simpler')
        elif 'thank you' in query:
            speak('happy to help ')

        elif 'youtube' in query:
            url = 'www.youtube.com'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Opening youtube ')
        elif 'netflix' in query:
            url = 'www.netflix.com'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Opening Netflix ')
        elif 'amazon' in query:
            url = 'www.amazon.com'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Opening Amazon shopping website ')
        elif 'tata sky' in query:
            url = 'https://watch.tatasky.com/live-tv?pageType=live-tv'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Opening Tata Sky ')
        elif 'gmail' in query:
            EdgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(EdgePath))
            url = 'https://mail.google.com/mail/u/0/#inbox'
            webbrowser.get('edge').open_new_tab(url)
            speak('Opening your mails ')
        elif 'remote github' in query:
            EdgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(EdgePath))
            url = 'https://github.com/RajatPrakash'
            webbrowser.get('edge').open_new_tab(url)
            speak('Opening your Remote Github  ')
        elif 'udemy' in query:
            EdgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            webbrowser.register('edge', None, webbrowser.BackgroundBrowser(EdgePath))
            url = 'https://www.udemy.com/home/my-courses/learning/'
            webbrowser.get('edge').open_new_tab(url)
            speak('Opening udemy  ')
        elif 'play music' in query:
            music = 'C:\\Users\\rajat\\Downloads\\Music'
            songs = os.listdir(music)
            os.startfile(os.path.join(music, songs[0]))
            speak('Playing Music ')
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M')
            speak(f'sir, The time is {strTime}')
        elif 'google' in query:
            ChromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(ChromePath)
            speak('Opening google ')
        elif 'python' in query:
            PythonPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2\\bin\\pycharm64.exe"
            os.startfile(PythonPath)
            speak('Opening Python Please Wait ')

        # working on accessing the specific folder in windows file system
        elif 'downloads' in query:
            path = "C:\\Users\\rajat\\Downloads"
            subprocess.Popen(f'explorer {os.path.realpath(path)}')
            speak('Opening Downloads Folder ')
        elif 'movies' in query:
            External_HardDrive = "F:\\Movies\\HollyWood"
            subprocess.Popen(f'explorer {os.path.realpath(External_HardDrive)}')
            speak('Opening Movies ')
        elif 'sql server' in query:
            SqlPath = "C:\\Program Files (x86)\\Microsoft SQL Server Management Studio 18\\Common7\\IDE\\Ssms.exe"
            os.startfile(SqlPath)
            speak('Opening Sequel Server Please Wait ')
        elif 'my net' in query:
            EdgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(EdgePath)
            speak('Opening Edge Browser ')
        elif 'close browser' in query:
            EdgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            p = subprocess.Popen(EdgePath)
            p.terminate()
            speak('Closing Edge Browser ')
        elif 'notepad' in query:
            NotePadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(NotePadPath)
            speak('Opening Notepad ')
        elif 'github' in query:
            GitPath = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(GitPath)
            speak('Opening GitHub ')
        elif 'sleep now' in query:
            speak('Closing')
            s.shutdown()
        elif 'restart please' in query:
            speak('Restarting...')
            r.restart()
