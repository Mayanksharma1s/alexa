import speech_recognition as sr
import sounddevice as sd
import pyttsx3, pywhatkit, wikipedia, pyjokes, datetime, os

# Initiate recognizer & TTS
listener = sr.Recognizer()
engine = pyttsx3.init()

print("Welcome to Alexa. Please speak what you want to say.")
# Set Voice Type (Female = 1, Male = 0)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

SAMPLE_RATE = 16000  # recommended for speech recognition
DURATION = 5         # seconds to listen

def talk(text):
    print("Alexa:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speech: {e}")

def record_audio(duration=DURATION, samplerate=SAMPLE_RATE):
    print("Listening.....")
    audio = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    return audio.flatten()

def take_command():
    command = ""
    try:
        audio_np = record_audio()

        audio_data = sr.AudioData(
            audio_np.tobytes(),
            SAMPLE_RATE,
            2  # 16-bit audio = 2 bytes
        )

        command = listener.recognize_google(audio_data)
        command = command.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that")
    except sr.RequestError:
        print("Network Error: Make sure you are connected to internet")

    return command

def run_alexa_talk():
    global run
    command = take_command()

    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"The current time is {time}")

    elif "who is" in command or "who the heck is" in command:
        person = (
            command.replace("who the heck is", "")
                   .replace("who is", "")
                   .strip()
        )
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "date" in command:
        talk("Sorry, I'm not in the mood")

    elif "are you single" in command:
        talk("I'm in a relationship with Wi-Fi")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    

    elif "open" in command:
        app = (
            command.replace("open", "")
                   .replace("launch", "")
                   .replace("start", "")
                   .strip()
        )
        if app == "browser":
            os.system("C:/Program Files/Google/Chrome/Application/chrome.exe") # use your own path for the application

        elif app == "spotify" or app == "music":
            os.system("C:/Users/mayan/AppData/Roaming/Spotify/Spotify.exe") # # use your own path for the application

        elif app == "code":
            os.system("C:/Users/mayan/AppData/Local/Programs/Microsoft VS Code/Code.exe") # # use your own path for the application

        elif app == "workspace":
            os.system("C:/Users/mayan/AppData/Local/Programs/Microsoft VS Code/Code.exe") # use your own path for the application
            os.system("C:/Users/mayan/AppData/Roaming/Spotify/Spotify.exe") # use your own path for the application
            os.system("C:/Program Files/Google/Chrome/Application/chrome.exe") # use your own path for the application
        
    elif "quit" in command:
        run = False
        talk("Goodbye!")
        return
    
    elif "hello" in command:
        talk("Hii Basfoot, Welcome to Alexa. How can I Help you ?") # Change Basfoot to your name if desired
    
    elif command != "":
        talk("Please say that again")

        

run = True
# Run Alexa
while run:
    run_alexa_talk()
