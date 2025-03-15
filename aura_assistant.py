import time
from speech import speak, listen_with_retry
from utils import tell_time, open_app, detect_language, play_on_youtube
from nlp_utils import analyze_sentiment, detect_intent
from google_search import search_google
from wikipedia_integration import ask_wikipedia
from mental_health import (
    log_mood, guided_therapy, guided_meditation, breathing_exercise,
    open_spotify, open_youtube, get_motivational_tip, set_goal, check_goals, check_for_crisis
)

# Global variable to track mental health mode
mental_health_mode = False

def handle_question(query, language="en"):
    """
    Handle user questions by querying Wikipedia or Google.

    :param query: The user's question.
    :param language: The language for the query (default is "en").
    :return: The response from Wikipedia or Google.
    """
    # Try Wikipedia first
    wikipedia_response = ask_wikipedia(query, language)
    if "sorry" not in wikipedia_response.lower():
        return wikipedia_response

    # Fallback to Google Search
    google_response = search_google(query, language)
    return google_response

def main():
    global mental_health_mode

    # Greet the user
    speak("Hello! I am your personal AI assistant. How can I assist you today?", language="en")
    print("Assistant started. Waiting for input...")

    while True:
        # Listen for user input
        command = listen_with_retry()
        if command:
            print(f"User command: {command}")

            # Check for exit command
            if "bye" in command.lower() or "exit" in command.lower():
                speak("Goodbye!", language="en")
                break

            # Check for mental health mode activation/deactivation
            if "activate mental health" in command.lower():
                mental_health_mode = True
                speak("Mental health mode activated.", language="en")
                continue
            elif "deactivate mental health" in command.lower():
                mental_health_mode = False
                speak("Mental health mode deactivated.", language="en")
                continue

            # Check for crisis
            crisis_response = check_for_crisis(command)
            if crisis_response:
                speak(crisis_response, language="en")
                continue

            # Detect language
            language = detect_language(command)
            print(f"Detected language: {language}")

            # Analyze sentiment only if emotional keywords are present
            emotional_keywords = ["happy", "sad", "angry", "upset", "excited"]
            if any(word in command.lower() for word in emotional_keywords):
                sentiment = analyze_sentiment(command)
                print(f"Detected sentiment: {sentiment}")
                if sentiment["label"] == "POSITIVE":
                    speak("I'm glad you're feeling positive!", language=language)
                elif sentiment["label"] == "NEGATIVE":
                    speak("I'm sorry you're feeling this way. How can I help?", language=language)

            # Handle YouTube Play Command
            if "play" in command.lower() and "on youtube" in command.lower():
                query = command.replace("play", "").replace("on youtube", "").strip()
                response = play_on_youtube(query)
                speak(response, language=language)
                continue

            # Handle Google Search command
            if "search google" in command.lower() or "search in google" in command.lower():
                query = command.replace("search google", "").replace("search in google", "").strip()
                response = search_google(query, language)
                speak(response, language=language)
                # If the response suggests opening Chrome, ask for confirmation
                if "open Chrome" in response:
                    speak("Should I open Chrome for more details?", language=language)
                    confirmation = listen_with_retry()
                    if "yes" in confirmation.lower():
                        open_app("browser")
                continue

            # Handle Wikipedia Search command
            if "search wiki" in command.lower():
                query = command.replace("search wiki", "").strip()
                response = ask_wikipedia(query, language)
                speak(response, language=language)
                continue

            # Detect intent
            intents = [
                "get_time", "set_alarm", "play_music", "ask_question", "translate_text",
                "open_app", "log_mood", "therapy", "meditation", "breathing", "motivation",
                "set_goal", "check_goals", "open_spotify", "open_youtube"
            ]
            intent, confidence = detect_intent(command, intents)
            print(f"Detected Intent: {intent}, Confidence: {confidence}")

            # Handle commands based on mode
            if mental_health_mode:
                if intent == "log_mood":
                    mood_response = log_mood(command)
                    speak(mood_response, language=language)
                elif intent == "therapy":
                    therapy_response = guided_therapy()
                    speak(therapy_response, language=language)
                elif intent == "meditation":
                    meditation_response = guided_meditation()
                    speak(meditation_response, language=language)
                elif intent == "breathing":
                    breathing_response = breathing_exercise()
                    speak(breathing_response, language=language)
                elif intent == "motivation":
                    motivation_response = get_motivational_tip()
                    speak(motivation_response, language=language)
                elif intent == "set_goal":
                    goal = command.replace("set a goal", "").strip()
                    goal_response = set_goal(goal)
                    speak(goal_response, language=language)
                elif intent == "check_goals":
                    goals_response = check_goals()
                    speak(goals_response, language=language)
                elif intent == "open_spotify":
                    spotify_response = open_spotify()
                    speak(spotify_response, language=language)
                elif intent == "open_youtube":
                    youtube_response = open_youtube()
                    speak(youtube_response, language=language)
                else:
                    speak("I'm sorry, I didn't understand that.", language=language)
            else:
                if intent == "get_time":
                    current_time = tell_time()
                    speak(current_time, language=language)
                elif intent == "ask_question":
                    response = handle_question(command, language)
                    speak(response, language=language)
                elif intent == "open_app":
                    app_name = command.replace("open", "").strip()
                    response = open_app(app_name)
                    speak(response, language=language)
                else:
                    speak("I'm sorry, I didn't understand that.", language=language)
        else:
            print("No command detected. Waiting for input...")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"An error occurred: {error}")