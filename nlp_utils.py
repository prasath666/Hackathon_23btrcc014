from transformers import pipeline

# Load pre-trained models
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
intent_detector = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_sentiment(text):
    try:
        result = sentiment_analyzer(text)
        return result[0]
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return {"label": "NEUTRAL", "score": 0.0}

def detect_intent(text, intents):
    try:
        result = intent_detector(text, intents)
        return result["labels"][0], result["scores"][0]
    except Exception as e:
        print(f"Error in intent detection: {e}")
        return None, 0.0