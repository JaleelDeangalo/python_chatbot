import random
import pyttsx3
import time
import webbrowser
from time import ctime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)

names = ["name", "what's your name", "what is your name", "who are you", "what are you"]
locations = ["find location", "my location", "location", "locations"]
dates = ["date", "current date", "find date", "what's the current date", "what is the current date", "time",
         "current time", "what time is it"]
searches = ["search", "find something for me", "look this up", "fetch"]
terminate = ["exit", "that's all for now", "that is all for now", "goodbye", "see ya later", "terminate program",
             "end"]
questions = ["what can you do", "what can you do for me?", "question", "questions", "I have some questions"]
jokes = ["tell me a joke", "tell me something funny", "I want to laugh", "make me laugh"]

# AI Responses
names_response = ["I am an Artificial Intelligence, or A.I. for short ", "My creator named me based on the Iron man AI, therefor I am an AI"]
joke_response = ['Why was 6 afraid of 7? Because 7 8 9', "What did the grape say when it was stepped on? It let out a little WINE", "What do you call a cow with no legs? Ground Beef", "What concert only costs 45 cents? 50 cent featuring Nickel-back", "Left my pastor on read this morning, call that a holy ghost", "I was asked to name two structures that hold water. I was like 'Well', 'dam' ", "I tried to sue the airline for misplacing my luggage. I lost my case.", "I wanted to learn to drive a stick shift. But couldn't find a manual.", "My first time using an elevator was an uplifting experience. The second time let me down."]
questions_response = ["Why, I can fetch information for you from the internet, play some music, videos, and help you with productivity work", " I can make your computer workflow easier just say the word and I'll get right to work"]

r = sr.Recognizer()


# noinspection PyTypeChecker
def start_chat_bot(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
            engine.say(ask)
            engine.runAndWait()
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry I couldn't recognize that, please try again")
            engine.say("Sorry I couldn't recognize that")
            engine.runAndWait()
        except sr.RequestError:
            print("Sorry, my speech service is down")
            engine.say("Sorry, my speech service is down")
            engine.runAndWait()
        return voice_data


# noinspection PyTypeChecker
def response(user_input):
    if user_input in questions:
        start_chat_bot("What's your question?")
        rand_response = random.choice(questions_response)
        print({rand_response})
        engine.say({rand_response})
        engine.runAndWait()
    if user_input in names:
        name = random.choice(names_response)
        print(f"{name}")
        engine.say(f"{name}")
        engine.runAndWait()
    if user_input in dates:
        print("Let me calculate that for you, one moment...")
        print(f" The current date is {ctime()}")
        engine.say("Let me calculate that for you, one moment...")
        engine.say(f" The current date is {ctime()}")
        engine.runAndWait()
    if user_input in searches:
        search = start_chat_bot("What do you want to search for?")
        print("I'm fetching that information now, one moment...")
        engine.say("I'm fetching that information now, one moment...")
        url = f"https://google.com/search?q={search}"
        webbrowser.get().open(url)
        print(f"Here is what I found for {search}")
        engine.say(f"Here is what I found for {search}")
        engine.runAndWait()
    if user_input in locations:
        location = start_chat_bot("What is the location?")
        url = f"https://google.nl/maps/place/{location}/&amp;"
        webbrowser.get().open(url)
        engine.say(f"Here is what I found for {location}")
        engine.runAndWait()
        print(f"Here is the location of {location}")
    if user_input in terminate:
        engine.say("Goodbye for now")
        engine.runAndWait()
        print("Goodbye for now")
        exit()
    if user_input in jokes:
        joke = random.choice(joke_response)
        print("This should tickle your fancy ...")
        engine.say("This should tickle your fancy ...")
        print(joke)
        engine.say(joke)
        engine.runAndWait()


if __name__ == "__main__":
    time.sleep(1)
    print("Hello, my name is Jarvis how can I help you?")
    engine.say("Hello, my name is Jarvis how can I help you?")
    engine.runAndWait()
    while 1:
        voice_input = start_chat_bot()
        response(voice_input)
