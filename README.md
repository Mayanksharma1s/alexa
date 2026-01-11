# Personal Alexa Voice Assistant (Python)

A simple **Python-based personal voice assistant** inspired by Alexa. This project uses speech recognition, text-to-speech, and custom command handling to perform tasks such as answering questions, telling the time, playing music, telling jokes, and opening desktop applications using absolute paths.

> ⚠️ **Note:** This is a personal/local project and not an official Amazon Alexa implementation.

---

## ✨ Features

* Voice input using microphone
* Text-to-speech responses
* Play songs on YouTube
* Tell current time
* Wikipedia search ("who is" queries)
* Tell jokes
* Open desktop applications (Chrome, Spotify, VS Code, etc.)
* Custom commands and workflows (e.g., `workspace`)
* Continuous listening loop until `quit` command

---

## 🧱 Tech Stack

* Python 3.x
* `speechrecognition`
* `sounddevice`
* `numpy`
* `pyttsx3`
* `pywhatkit`
* `wikipedia`
* `pyjokes`

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mayanksharma1s/alexa
   ```

2. **Install dependencies**

   ```bash
   pip install speechrecognition sounddevice numpy pyttsx3 pywhatkit wikipedia pyjokes
   ```

3. **Ensure microphone access** is enabled on your system.

---

## ⚙️ Configuration (IMPORTANT)

### Absolute Application Paths

This project uses `os.system()` to open applications. **You must replace the paths with absolute paths from your own system**, otherwise the commands will not work.

Example:

```python
os.system("C:/Program Files/Google/Chrome/Application/chrome.exe")
```

To find the absolute path on Windows:

1. Right-click the application shortcut
2. Select **Properties**
3. Copy the value from **Target**

Update paths inside the `open` command block accordingly.

---

## 🎙️ Available Voice Commands

| Command           | Action                |
| ----------------- | --------------------- |
| `play <song>`     | Plays song on YouTube |
| `what time is it` | Speaks current time   |
| `who is <person>` | Wikipedia summary     |
| `tell me a joke`  | Random joke           |
| `open browser`    | Opens Chrome          |
| `open spotify`    | Opens Spotify         |
| `open code`       | Opens VS Code         |
| `open workspace`  | Opens multiple apps   |
| `hello`           | Greets the user       |
| `quit`            | Stops the assistant   |

---

## 🧠 How It Works

1. Records audio using `sounddevice`
2. Converts audio to text using Google Speech Recognition API
3. Matches spoken text with predefined commands
4. Executes actions or speaks responses using `pyttsx3`
5. Runs continuously in a loop until stopped

---

## 🐞 Troubleshooting

* **Assistant not speaking**: Restart the program; `pyttsx3` may lock the audio engine.
* **Speech not recognized**: Check microphone input and internet connection.
* **App not opening**: Verify absolute path is correct.
* **Unicode path error**: Use forward slashes (`/`) instead of backslashes (`\\`).

---

## 🚧 Limitations

* Requires active internet connection for speech recognition
* Windows-focused (paths are OS-specific)
* Blocking speech engine (single-threaded)

---

## 📌 Future Improvements (Optional)

* Threaded TTS and listening
* Config file for app paths
* Wake-word detection
* GUI interface
* Cross-platform support

---

## 📄 License

This project is for **personal and educational use**.
Kindly give credits if used.

---

## 🙌 Acknowledgements

* Google Speech Recognition
* Python open-source community

---

If you find this project useful, feel free to ⭐ the repository.

-Basfoot
