#!/usr/bin/env python3

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 
import sys
import subprocess
import speech_recognition as sr



def text_to_voice(text,index):
    # print("ds")
    # The text that you want to convert to audio 
    # mytext = 'Welcome to geeksforgeeks!'

    # # Language in which you want to convert 
    language = 'en'

    # # Passing the text and language to the engine, 
    # # here we have marked slow=False. Which tells 
    # # the module that the converted audio should 
    # # have a high speed 
    myobj = gTTS(text=text, lang=language, slow=False) 

    # # Saving the converted audio in a mp3 file named 
    # # welcome
    file_name = "audio_"+str(index)+".mp3" 
    file_name = "audio.mp3" 
    myobj.save(file_name) 

    # # Playing the converted file 
    cmd = "mpg321 " + file_name
    os.system(cmd) 
    check_for_commands(text)



def execute_commands(cmd):
    print("executing comman", cmd)
    # os.system(cmd.lower())
    subprocess.call(cmd.lower(), shell=True)

def check_for_commands(text):
    if "babu" in text.lower():
        text_to_voice("hellooo manikanta\nactivating Baaaaaaaaaaaaaaaaaaaaaaaaaaaaburao command mode",1)
        speech(True)
    elif "quit" in text.lower():
        sys.exit('exit')





r = sr.Recognizer()
def speech(isCMD):
    with sr.Microphone() as source:
        print("speak something: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("you said: {}".format(text))
            text_to_voice(text, x)
            if isCMD:
                execute_commands(text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


x = True
while x:
    speech(False)