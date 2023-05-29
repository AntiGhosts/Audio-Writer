import speech_recognition as sr

# Create a speech recognizer
r = sr.Recognizer()

# Uses microphone as input source
with sr.Microphone() as source:
    # Adjusts background noise to reduce ambient noise
    r.adjust_for_ambient_noise(source)
    print("Say something...")
    # Listen to what you say
    audio = r.listen(source)

try:
    # Uses Google Speech Recognition to turn audio into text
    text = r.recognize_google(audio, language='en-US')
    print("You said:", text)
except sr.UnknownValueError:
    print("Did not understand what you said")
except sr.RequestError as e:
    print("Unable to get Google Speech Recognition results; {0}".format(e))
