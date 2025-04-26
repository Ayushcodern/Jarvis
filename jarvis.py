import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine =pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        speak("good morning Ayush!") 

    elif hour>=12 and hour<18:
        speak("good afternoon ayush!")    

    else:
        speak("good evening ayush!")    

def start():
    print("initializing jarvis")
    speak("initializing jarvis ")
    print("booting all drives")
    speak("booting all drives")
    print("checking security")
    speak("checking security")
    print("server booting please wait")
    speak("server booting please wait ")
    speak("i am ready to takeover")   

def calculate():
    print("what is your first number")
    num1=input()
    print("what is your operator")
    op=input()
    print("what is your second number")
    num2=input()

    if op=="*":
        print(num1*num2)    

    else:
        print("invalid syntax")  
           
 

def takecommand():
    #it will takes user input and return string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_thresholds =2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')   
        print(f"User said: {query}\n") 

    except Exception as e:
        #print(e)   
        print("say that again please")
        return "none"
    return query    


if __name__ == "__main__":
    start()
    wishme()
    while 1:
        query = takecommand().lower()
        #logic for executing tasks.
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")   

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'jarvis you are great' in query:
            speak("yes sir its all your power to builtup me ")

        elif 'hello jarvis' in query:
            speak("hi sir how can i help you")    
          
        elif 'what can you do' in query:
            speak("i can manage your data")

        elif 'open vs code' in query:
            codepath = "C:\\Users\\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codepath)  

        elif 'open chrome' in query:
            chromepath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'open blender' in query:
            blenderpath = "C:\\Program Files\\Blender Foundation\\Blender 2.83\\blender.exe"
            os.startfile(blenderpath)

        elif  'open server' in query:
            jarvispath = "C:\\Users\\win 10\\Desktop\\jarvis.jpg"  
            os.startfile(jarvispath)  

        elif 'open milanote' in query:
            webbrowser.open("www.milanote.com")        
            

        elif 'jarvis keep online' in query:
            speak("yes sir i am online in just few seconds")
            speak("")
            speak("")  
            speak("")  
            speak("")
            speak("")  
            speak("") 
            speak("")
            speak("")  
            speak("yes sir i am online") 

        elif 'open pixabay' in query:
            webbrowser.open("www.pixabay.com")

        elif 'open python' in query:
            webbrowser.open("www.python.org")    

        elif 'open canva' in query:
            webbrowser.open("www.canva.com") 

        elif 'open visual scripting ' in query:
            webbrowser.open("www.code.org")    

        elif 'tell me a quote' in query:
           speak("if anyone ask me what is your language i said my language is english but writeen language is python") 

        elif 'connect watch' in query:
            speak("connecting server of mi watch")  

        elif 'say hi to my friend' in query:
            speak("hi sir you are friend of ayush")

        elif 'are you human' in query:
            speak("no i am i am not a human but i am ai")

        elif 'calculate my sum' in query:
            calculate()

        elif 'open my website' in query:
            webbrowser.open("https://devayush24.github.io/Ayushcreations.github.io/")


        '''
        elif 'play music' in query:
            music_dir = 'D:\\non critical\\songs\\favourite_songs1'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        # this is for playing music i have no music in mp laptop so i give comment.    
        '''