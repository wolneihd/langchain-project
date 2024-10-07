# pip install speechrecognition
# pip install pyaudio
# pip install pyttsx3

import speech_recognition as sr
import pyttsx3 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    
# Loop infinitely for user to speak
while True:  # Use 'True' instead of '1' for better readability
    
    try:
        # Use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # Wait for a second to let the recognizer adjust the energy threshold
            # based on the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            # Listens for the user's input
            audio2 = r.listen(source2)
            
            # Using Google to recognize audio
            MyText = r.recognize_google(audio2, language="pt-BR")
            MyText = MyText.lower()

            print("Did you say:", MyText)
            SpeakText(MyText)
            
            # Optionally break the loop if a specific word is said, e.g., 'exit'
            if 'exit' in MyText:
                print("Exiting...")
                break
            
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        
    except sr.UnknownValueError:
        print("Unknown error occurred")
