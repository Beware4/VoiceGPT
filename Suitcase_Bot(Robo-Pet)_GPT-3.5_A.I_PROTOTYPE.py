#API KEY: 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
import openai
import speech_recognition as mic
import gtts
from gtts import gTTS
import playsound
from playsound import playsound
import os

openai.api_key = "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"
print(openai.Model.list())
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
            prompt="""
            I want you to act as a science teacher. I will provide some middle school science questions or concepts, and it will be your job to explain them in easy-to-understand terms.
            This could include providing step-by-step instructions for solving a problem, demonstrating various techniques with visuals or suggesting online resources for further study.
            Also try to use cell analogies as much as possible. Please keep your answers shortened to fifty words or less.

            """
        #  question = text + " and please shorten it to twenty words or less"
        #print(question)
            question = prompt + "My request is: " + text + " and remember to use a cell analogy."
        except:
            print("Make sure that your input audio device (mic/microphone) is correctly plugged in/connected. Also, try checking your internet connection")
        response = openai.ChatCompletion.create(
            model="gpt-4",
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
