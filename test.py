import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio, lang='en'):
    if lang == 'hi':
        engine.setProperty('voice', voices[1].id)  # Change to Hindi voice if available
    else:
        engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Ayush!", 'en')
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Ayush!", 'en')
    else:
        speak("Good evening Ayush!", 'en')

def start():
    print("Initializing Jarvis")
    speak("Initializing Jarvis", 'en')
    print("Booting all drives")
    speak("Booting all drives", 'en')
    print("Checking security")
    speak("Checking security", 'en')
    print("Server booting, please wait")
    speak("Server booting, please wait", 'en')
    speak("I am ready to take over", 'en')

def calculate():
    print("What is your first number?")
    num1 = float(input())
    print("What is your operator?")
    op = input()
    print("What is your second number?")
    num2 = float(input())

    if op == "*":
        print(num1 * num2)
    else:
        print("Invalid syntax")

def google_search(query):
    service = build("customsearch", "v1", developerKey="AIzaSyDb-MhBot66ntsxEj5URozmqzzjzrVx6mU")
    res = service.cse().list(q=query, cx='30b0bf37c57fb409d').execute()
    results = res.get('items', [])
    if results:
        return results[0]['snippet']
    else:
        return "Sorry, I couldn't find any information on that."

def takecommand():
    # It will take user input and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi-IN')  # You can set to 'en-IN' for English and 'hi-IN' for Hindi
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "none"
    return query

def listen_for_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-IN')
        if "hello jarvis" in query.lower():
            return True
    except Exception as e:
        pass
    return False

def open_website(query):
    url = query.split("open ")[1]
    if not url.startswith("http"):
        url = "http://" + url
    # Replace this with Brave browser executable path
    brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
    webbrowser.get('brave').open(url)
    speak(f"Opening {url}")

def search_on_gemini(query, num_results=1, snippet_length=50):
    api_key = "AIzaSyDb-MhBot66ntsxEj5URozmqzzjzrVx6mU"  # Your Google API key
    cse_id = "30b0bf37c57fb409d"  # Your Custom Search Engine ID
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}&num={num_results}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'items' in data and len(data['items']) > 0:
                first_result = data['items'][0]
                snippet = first_result.get('snippet', '')
                if len(snippet.split()) >= snippet_length:
                    return ' '.join(snippet.split()[:snippet_length]) + '...'
                else:
                    return snippet
            else:
                return "Sorry, I couldn't find any information on that."
        else:
            return f"Sorry, I couldn't access Gemini at this time. HTTP status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    start()
    wishme()
    while True:
        if listen_for_wake_word():
            speak("Yes sir, how can I help you?", 'en')
            while True:
                query = takecommand().lower()
                if 'wikipedia' in query:
                    speak("Searching Wikipedia...", 'en')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia", 'en')
                    speak(results, 'en')
                    print(results)

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")

                elif 'jarvis you are great' in query:
                    speak("Yes sir, it's all your power to build me up.", 'en')

                elif 'hello jarvis' in query:
                    speak("Hi sir, how can I help you?", 'en')

                elif 'what can you do' in query:
                    speak("I can manage your data.", 'en')

                elif 'open vs code' in query:
                    codepath = "C:\\Users\\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codepath)

                elif 'open chrome' in query:
                    chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(chromepath)

                elif 'open blender' in query:
                    blenderpath = "C:\\Program Files\\Blender Foundation\\Blender 2.83\\blender.exe"
                    os.startfile(blenderpath)

                elif 'open server' in query:
                    jarvispath = "C:\\Users\\win 10\\Desktop\\jarvis.jpg"
                    os.startfile(jarvispath)

                elif 'open milanote' in query:
                    webbrowser.open("www.milanote.com")

                elif 'jarvis keep online' in query:
                    speak("Yes sir, I am online in just a few seconds.", 'en')
                    for _ in range(7):
                        speak("", 'en')
                    speak("Yes sir, I am online.", 'en')

                elif 'open pixabay' in query:
                    webbrowser.open("www.pixabay.com")

                elif 'open python' in query:
                    webbrowser.open("www.python.org")

                elif 'open canva' in query:
                    webbrowser.open("www.canva.com")

                elif 'open visual scripting' in query:
                    webbrowser.open("www.code.org")

                elif 'tell me a quote' in query:
                    speak("If anyone asks me what is your language, I say my language is English, but written language is Python.", 'en')

                elif 'connect watch' in query:
                    speak("Connecting server of MI watch.", 'en')

                elif 'say hi to my friend' in query:
                    speak("Hi sir, you are a friend of Ayush.", 'en')

                elif 'are you human' in query:
                    speak("No, I am not a human, but I am AI.", 'en')

                elif 'calculate my sum' in query:
                    calculate()

                elif 'open my website' in query:
                    webbrowser.open("https://devayush24.github.io/Ayushcreations.github.io/")

                elif 'search on gemini' in query:
                    search_query = query.replace("search on gemini", "")
                    result = search_on_gemini(search_query, snippet_length=50)
                    speak(result, 'en')
                    print(result)

                elif 'open' in query:
                    open_website(query)

                else:
                    result = google_search(query)
                    speak(result, 'en')
                    print(result)
                    break
