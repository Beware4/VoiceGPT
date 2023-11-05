#API KEY: 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
import openai
import speech_recognition as mic
import gtts
from gtts import gTTS
import playsound
from playsound import playsound
import os

openai.api_key = "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"
#print(openai.Model.list())
#openai.api_version = "2023-03-15-preview"
r = mic.Recognizer()
#question = input("QUESTION_PROMPT>> ")

def SAVETTSTOMP3(TTS_VAR):
    tts = gTTS(str(TTS_VAR))
    tts.save("answer.mp3")

while True:
    with mic.Microphone() as source:
     
        print("Start talking")
        try:
            speech = r.record(source, duration=5)
            print("recorded")
            text = r.recognize_google(speech)
            print("recognized")
            print("text: " + text)
            question = text + " and please shorten it to twenty words or less"
            print(question)
        
        except:
            print("Make sure that your input audio device (mic/microphone) is correctly plugged in/connected. Also, try checking your internet connection")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": question
            }])
        print("responses generated")
    
        finalresponse = response.choices[0].message.content
        print("response validated")
    
        print(finalresponse)
        print("outputted response")
    
        try:
            SAVETTSTOMP3(finalresponse)
            print("saved mp3")
            playsound("answer.mp3")
            print("played mp3")
        
            if os.path.isfile("answer.mp3"):
                os.remove("answer.mp3")
                print("removed mp3")
        except:
            print("Error: Please make sure that you are speaking clearly")
