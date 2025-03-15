import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os
import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set default voice to female
def set_voice(gender="female"):
    voices = engine.getProperty('voices')
    if gender == "male":
        engine.setProperty('voice', voices[0].id)  # Male voice
    else:
        engine.setProperty('voice', voices[1].id)  # Female voice (default)

set_voice("female")

def speak(text, language="en"):
    try:
        if language in ["ta", "te", "hi", "kn"]:  # Use gTTS for regional languages
            tts = gTTS(text=text, lang=language)
            tts.save("temp.mp3")
            if os.name == "nt":  # Windows
                os.system("start temp.mp3")
            elif os.name == "posix":  # macOS or Linux
                os.system("afplay temp.mp3" if os.uname().sysname == "Darwin" else "mpg321 temp.mp3")
            time.sleep(1)  # Wait for the audio to finish playing
            os.remove("temp.mp3")  # Clean up the temporary file
        else:  # Use pyttsx3 for English
            engine.say(text)
            engine.runAndWait()
    except Exception as e:
        print(f"Error in speech synthesis: {e}")

def listen_with_retry(timeout=5, retries=3, language="en-IN"):
    recognizer = sr.Recognizer()
    for attempt in range(retries):
        with sr.Microphone() as source:
            print("Listening...")
            try:
                recognizer.adjust_for_ambient_noise(source)
                print("Say something!")
                audio = recognizer.listen(source, timeout=timeout)
                try:
                    text = recognizer.recognize_google(audio, language=language)
                    print(f"You said: {text}")
                    return text
                except sr.UnknownValueError:
                    print("Sorry, I didn't catch that. Can you repeat?")
                    speak("Sorry, I didn't catch that. Can you repeat?", language="en")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")
                    speak("Sorry, my speech service is down.", language="en")
            except sr.WaitTimeoutError:
                print("Listening timed out. Please try again.")
                speak("Listening timed out. Please try again.", language="en")
            except Exception as e:
                print(f"Error in speech recognition: {e}")
                speak("Sorry, I encountered an error. Please try again.", language="en")
    return None