from time import sleep
import pyttsx3
from gtts import gTTS

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    print(command)
    engine.runAndWait()

# Voice Converter - female version
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
voice = int(input("Enter 1 for female voice else 0 for male voice:"))
if voice == 1:
    # Use female voice
    converter = pyttsx3.init()
    converter.setProperty('voice', voice_id)
    converter.runAndWait()

current_floor_lift = 0

while True:
    # Input from the user to operate lift
    SpeakText("Enter the floor you are in : ")
    current_floor_person = eval(input())
    SpeakText("Enter the floor you want to go : ")
    floor_to_go = eval(input())

    # If lift and person are on the same floor or different floor, lift moves according to the user input.
    if floor_to_go == current_floor_person:
        SpeakText("You are on the same floor")

    elif current_floor_person != current_floor_lift:
        while current_floor_person > current_floor_lift:
            current_floor_lift += 1
            sleep(1)
            print("Currently in floor {}".format(current_floor_lift))
            sleep(2)

        while current_floor_person < current_floor_lift:
            current_floor_lift -= 1
            sleep(1)
            print("Currently in floor {}".format(current_floor_lift))
            sleep(2)

        SpeakText("Doors are opening..Please Enter")
        sleep(1)
        SpeakText("Doors are closing")
        sleep(2)

    # Once Person enters Lift moves to the desired floor.
    if floor_to_go > current_floor_person:
        while floor_to_go > current_floor_person:
            current_floor_person += 1
            current_floor_lift += 1
            print("Currently in floor {}".format(current_floor_person))
            sleep(2)

            if current_floor_person == floor_to_go:
                SpeakText("you reached your floor. Doors are opening")
                sleep(1)
                SpeakText("Doors are closing")
                sleep(1)
                break

    elif floor_to_go < current_floor_person:
        while floor_to_go < current_floor_person:
            current_floor_person -= 1
            current_floor_lift -= 1
            print("Currently in floor {}".format(current_floor_person))
            sleep(2)

            if current_floor_person == floor_to_go:
                SpeakText("You reached your floor. Doors are opening")
                sleep(1)
                SpeakText("Doors are closing")
                sleep(1)
                break

    exit_lift = eval(input("Please press 1 if you want to exit else press 0 to continue: "))
    if exit_lift:
        break
