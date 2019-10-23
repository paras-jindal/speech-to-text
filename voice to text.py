#Python 2.x program for Speech Recognition 

import speech_recognition as sr 
r= sr.Recognizer()
with sr.Microphone() as source:
    print("say something")
    audio =r.listen(source)
    print("time over")
    
try:
    print("text "+r.recognize_google(audio))
except:
    pass