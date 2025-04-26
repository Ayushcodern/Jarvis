import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont

class JarvisGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Jarvis AI Assistant")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: black;")

        # Create central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Add a label for the time
        self.time_label = QLabel(self)
        self.time_label.setStyleSheet("color: cyan;")
        self.time_label.setFont(QFont('Arial', 100))
        self.time_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.time_label)

        # Add a text edit for displaying recognized speech and outputs
        self.output_text = QTextEdit(self)
        self.output_text.setStyleSheet("color: white; background-color: black;")
        self.output_text.setFont(QFont('Arial', 14))
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Update the time every second
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)  # Update every second to ensure minute change is caught immediately

        self.show_time()

        # Initialize AI Assistant
        self.init_ai_assistant()
        self.start_ai()

    def show_time(self):
        current_time = QTime.currentTime().toString('hh:mm')
        self.time_label.setText(current_time)

    def init_ai_assistant(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def speak(self, audio):
        self.output_text.append(f"Jarvis: {audio}")
        self.engine.say(audio)
        self.engine.runAndWait()

    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("Good morning Ayush!")
        elif hour >= 12 and hour < 18:
            self.speak("Good afternoon Ayush!")
        else:
            self.speak("Good evening Ayush!")

    def start_ai(self):
        self.output_text.append("Initializing Jarvis")
        self.speak("Initializing Jarvis")
        self.output_text.append("Booting all drives")
        self.speak("Booting all drives")
        self.output_text.append("Checking security")
        self.speak("Checking security")
        self.output_text.append("Server booting, please wait")
        self.speak("Server booting, please wait")
        self.speak("I am ready to take over")
        self.wishme()

    def calculate(self):
        self.output_text.append("What is your first number?")
        self.speak("What is your first number?")
        num1 = float(input())
        self.output_text.append(f"First number: {num1}")

        self.output_text.append("What is your operator?")
        self.speak("What is your operator?")
        op = input()
        self.output_text.append(f"Operator: {op}")

        self.output_text.append("What is your second number?")
        self.speak("What is your second number?")
        num2 = float(input())
        self.output_text.append(f"Second number: {num2}")

        if op == "*":
            result = num1 * num2
            self.output_text.append(f"Result: {result}")
            self.speak(f"The result is {result}")
        else:
            self.output_text.append("Invalid syntax")
            self.speak("Invalid syntax")

    def google_search(self, query):
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        result = ""
        for g in soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'):
            result = g.get_text()
            break
        if not result:
            for g in soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
                result = g.get_text()
                break
        if not result:
            result = "Sorry, I couldn't find any information on that."
        return result

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.output_text.append("Listening...")
            r.pause_threshold = 2
            audio = r.listen(source)

        try:
            self.output_text.append("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            self.output_text.append(f"User said: {query}\n")
        except Exception as e:
            self.output_text.append("Say that again please")
            return "none"
        return query

    def listen_for_wake_word(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.output_text.append("Listening for wake word...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            if "hello jarvis" in query.lower():
                return True
        except Exception as e:
            pass
        return False

    def open_website(self, query):
        url = query.split("open ")[1]
        if not url.startswith("http"):
            url = "http://" + url
        brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
        webbrowser.get('brave').open(url)
        self.speak(f"Opening {url}")

    def search_on_gemini(self, query, num_results=1, snippet_length=50):
        api_key = "AIzaSyDb-MhBot66ntsxEj5URozmqzzjzrVx6mU"
        cse_id = "30b0bf37c57fb409d"
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

def main():
    app = QApplication(sys.argv)
    window = JarvisGUI()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
