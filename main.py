import webbrowser
import pyttsx3 #text to speech conversion library in python. It works offline too.
import speech_recognition as sr # this does reverse of pyttsx3 , it converts speech to text,makes a query or gives reply.
import datetime #Its inbuilt into python,no external installation is required.
import wikipedia #imports wikipedia module, external installation is required
import os #inbuilt
import smtplib #inbuilt

master="mam"

print("Initialising Jarvis")


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

#This function will pronounce what ever is written in the string. Ive given welcome!
def speak(text):
    engine.say(text)
    engine.runAndWait()




#This function has used datetime module and will wish me according to time , hour of the day.
def wishMe():
    hour=datetime.datetime.now().hour
    print(hour)

    if hour>=0 and hour<12:
        speak("Good morning"+master)
    elif hour>=12 and hour<18:
        speak("good afternoon"+master+"how was your day")
    elif hour>=18 and hour<22:
        speak("Good evening"+master+"how was your day")
    else:
        speak("Good night mam, have a great sleep.")
    speak("How may I help you")


#this function will take command from microphone
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}\n")

    except Exception as e:
        print("Please say that again")
        query = None
    return query

speak("welcome!")   
wishMe()
query=takecommand()


def sendEmail(to,content):
    server=smtplib.SMTP('smpt.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('radhakrishna270402@gmail.com','password')
    server.sendmail("gsrinivasteja@gmail.com")
    server.close()


#Logic for excecuting tasks
if 'Wikipedia' in query:    #Notice "W" , avoid writing w , use uppercase()
    print('searching wikipedia')
    query=query.replace("wikipedia","")
    result=wikipedia.summary(query,sentences=2)
    speak(result)
    print(result)
elif 'open YouTube' in query:
    webbrowser.open("youtube.com")
elif 'open Google' in query:
    webbrowser.open("google.com")
elif 'open stack overflow' in query:
    webbrowser.open("stackoverflow.com")
elif 'open medium' in query:
    webbrowser.open("medium.com")
elif 'open Gmail' in query:
    webbrowser.open("gmail.com")
elif "what's the time" in query:
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Mam its {strTime} now")
elif 'open code' in query:
    codepath="C:\\Users\\gsrin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\code.exe"
    os.startfile(codepath)






