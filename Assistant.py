import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis , Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


    
def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    query(f"The current time is {current_time}")

# define a function to get the current date
def get_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    query(f"Today is {current_date}")

# define a function to open a file
def open_file(filename):
    os.startfile(filename)

# define a function to shut down the computer
def shut_down():
    speak("Shutting down...")
    os.system("shutdown /s /t 1")

# define a function to restart the computer
def restart():
    speak("Restarting...")
    os.system("shutdown /r /t 1")

# define a function to log out of the computer
def log_out():
    speak("Logging out...")
    os.system("shutdown -l")

def get_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    speak(f"Today is {current_date}")
    print(f"Today is {current_date}")


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

          
            
         # get the current time
        elif "what time is it" in query:
            get_time()

    # get the current date
        elif "what's the date" in query:
           get_date()

    # open a file
        elif "open" in query and "file" in query:
            filename = query.split()[-1]
            open_file(filename)

    # shut down the computer
        elif "shut down" in query:
            shut_down()

    # restart the computer
        elif "restart" in query:
            restart()

    # log out of the computer
        elif "log out" in query:
            log_out()


        elif 'music' in query:
            music_dir = 'C:\Music Downloader'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        if 'play' in  query:
            song = query.replace('play', '')
            speak('playing ' + song)
            print('playing ' + song)
            pywhatkit.playonyt(song)
            
        elif 'take me to' in query:
            task = query.replace('take me to', '')
            speak('opening' +task)
            print('opening' +task)
            pywhatkit.search(task)
        
        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        elif 'date' in query:
            get_date()
        elif 'are you single' in query:
             speak('I am in a relationship with wifi')
             print("LOL. No I am not single. Don't try.")
        elif "what time is it" in query:
             get_time()  
             
        elif "how are you" in query:
            speak("I am good thank you. How are you doing?")
    
        elif "good" in query or "fine" in query:
            speak("I am glad to hear that sir.")
        
        elif "not ok" in query or "sad" in query:
            speak("What happened sir? Want to hear a joke? If yes, please say 'Tell me a joke'")
        
        elif "what are you doing?" in query or "doing" in query:
            speak("Just waiting for your orders :smiling_face:")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())
        elif "bye" in query:
            exit()
        
        
