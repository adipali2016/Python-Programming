import webbrowser
import speech_recognition as sr

print("Ahoy! Welcome to Sasti Services")

print("We are listening your requirements : ", end='')

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening Started")
    audio = r.listen(source)
    print("Listening Stopped")

ch = r.recognize_google(audio)

if ("Facebook" in ch) and ("launch" in ch):
    webbrowser.open("https://www.facebook.com")
elif ("Google" in ch) and ("launch" in ch):
    webbrowser.open("https://www.google.com")
else:
    print("Command not found")
