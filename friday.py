import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your wolfalpha code')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)



def speak(audio):
    print('Friday: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant Friday!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)                                                                      
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        if(name==''):
            print('User: ' + query + '\n')
        else:
            print(name+': ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    return query
        
name=''
if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'my name' in query:
            if(name==''):
                speak('You have not tolk me your name, but I will remember it. What is your name, sir ?')
                myName=myCommand()
                name=myName
                speak('Hello Mr.'+myName)
            else: speak('Your name is: '+name)
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.com.vn')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("your email", 'your password')
                    server.sendmail('username', "username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder='D:/music/'
            music = ['music1', 'music2', 'music3', 'music4']
            random_music = os.path.join(music_folder,random.choice(music) + ".mp3")
            speak('Okay, here is your music! Enjoy!')
            os.system(random_music)
            
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
