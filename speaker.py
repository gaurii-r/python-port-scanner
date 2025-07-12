import pyttsx3

engine = pyttsx3.init()

print("Welcome to RoboSpeaker 1.1. Created by Gauri")

while True:
    x = input("Enter what you want me to speak: ")
    if x.lower() == "q":
        engine.say("bye bye friend")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()
