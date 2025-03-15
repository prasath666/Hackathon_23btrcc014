import json
from datetime import datetime
import random
import webbrowser

# Mood tracking
def log_mood(mood):
    try:
        with open("mood_log.json", "a") as file:
            entry = {"timestamp": datetime.now().isoformat(), "mood": mood}
            file.write(json.dumps(entry) + "\n")
        return f"Your mood ({mood}) has been logged."
    except Exception as e:
        return f"Error logging mood: {e}"

def analyze_mood():
    try:
        with open("mood_log.json", "r") as file:
            moods = [json.loads(line)["mood"] for line in file]
            if moods:
                mood_count = {}
                for mood in moods:
                    mood_count[mood] = mood_count.get(mood, 0) + 1
                mood_summary = ", ".join([f"{k} ({v} times)" for k, v in mood_count.items()])
                return f"Your recent moods: {mood_summary}"
            else:
                return "No mood data found."
    except FileNotFoundError:
        return "No mood data found."
    except Exception as e:
        return f"Error analyzing mood: {e}"

# Crisis intervention
def check_for_crisis(command):
    crisis_keywords = ["sad", "depressed", "suicide", "help", "crisis"]
    for keyword in crisis_keywords:
        if keyword in command.lower():
            return (
                "I'm sorry you're feeling this way. Please reach out to a trusted friend or a mental health professional. "
                "Here’s the number for the National Suicide Prevention Lifeline: 1-800-273-TALK."
            )
    return None

# Guided therapy
def guided_therapy():
    return (
        "Let’s try a CBT exercise. Think about a recent situation that upset you. "
        "What were your thoughts and feelings? Write them down if you can. "
        "Now, let’s challenge those thoughts. Are they based on facts or assumptions?"
    )

# Guided meditation
def guided_meditation():
    return (
        "Let’s begin a guided meditation. Sit comfortably and close your eyes. "
        "Take a deep breath in... and out... Focus on your breathing. "
        "If your mind wanders, gently bring it back to your breath."
    )

# Breathing exercises
def breathing_exercise():
    return (
        "Let’s try a breathing exercise. Inhale deeply for 4 seconds, "
        "hold your breath for 4 seconds, and exhale slowly for 6 seconds. "
        "Repeat this cycle for a few minutes."
    )

# Open Spotify and YouTube
def open_spotify():
    webbrowser.open("https://open.spotify.com")
    return "Opening Spotify. Search for calming music or guided meditations."

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube. Search for relaxation music or guided meditations."

# Motivational tips
motivational_tips = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Don't watch the clock; do what it does. Keep going."
]

def get_motivational_tip():
    return random.choice(motivational_tips)

# Goal setting and tracking
goals = []

def set_goal(goal):
    goals.append({"goal": goal, "status": "In Progress"})
    return f"Your goal '{goal}' has been set."

def check_goals():
    if goals:
        return "Here are your current goals: " + ", ".join([goal["goal"] for goal in goals])
    else:
        return "You have no goals set yet."