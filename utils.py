import os
import webbrowser
import subprocess
from datetime import datetime

def tell_time():
    """
    Get the current time.

    :return: The current time in HH:MM:SS format.
    """
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def detect_language(text):
    """
    Detect the language of the input text (basic implementation).

    :param text: The input text.
    :return: The detected language.
    """
    if "hello" in text.lower():
        return "English"
    elif "hola" in text.lower():
        return "Spanish"
    else:
        return "Unknown"

def open_app(app_name):
    """
    Open a specific application or website based on the user's input.

    :param app_name: The name of the app or website to open.
    :return: A confirmation message or an error message.
    """
    app_name = app_name.lower()
    app_mappings = {
        "whatsapp": "https://web.whatsapp.com",
        "instagram": "https://www.instagram.com",
        "youtube": "https://www.youtube.com",
        "calculator": "calc.exe" if os.name == "nt" else "gnome-calculator",  # Windows or Linux
        "notepad": "notepad.exe" if os.name == "nt" else "gedit",  # Windows or Linux
        "spotify": "spotify",  # Ensure Spotify is installed and added to PATH
        "browser": "start chrome" if os.name == "nt" else "google-chrome",  # Windows or Linux
    }

    try:
        if app_name in app_mappings:
            if app_name in ["whatsapp", "instagram", "youtube"]:
                webbrowser.open(app_mappings[app_name])
                return f"Opening {app_name.capitalize()} in your browser."
            else:
                subprocess.run(app_mappings[app_name], shell=True)
                return f"Opening {app_name.capitalize()}."
        else:
            return "Sorry, I can't open that app."
    except Exception as e:
        return f"Error opening the app: {e}"

def play_on_youtube(query):
    """
    Play a song or video on YouTube based on the user's query.

    :param query: The song or video to search for on YouTube.
    :return: A confirmation message.
    """
    try:
        # Construct the YouTube search URL
        url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        webbrowser.open(url)
        return f"Playing {query} on YouTube."
    except Exception as e:
        return f"Error playing on YouTube: {e}"