"""
Emotion detection using transformer models
"""

from transformers import pipeline

# Load the emotion classifier once (important for performance)
print("🔄 Loading emotion detection model...")
classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)
print("✅ Model loaded successfully!\n")

# Emotion aliases for better understanding
EMOTION_ALIASES = {
    "neutral": "neutral",
    "admiration": "joy",
    "amusement": "joy",
    "anger": "anger",
    "annoyance": "anger",
    "approval": "joy",
    "caring": "love",
    "confusion": "fear",
    "curiosity": "surprise",
    "desire": "joy",
    "disappointment": "sadness",
    "disapproval": "disgust",
    "disgust": "disgust",
    "embarrassment": "fear",
    "excitement": "surprise",
    "fear": "fear",
    "gratitude": "love",
    "grief": "sadness",
    "joy": "joy",
    "love": "love",
    "nervousness": "fear",
    "optimism": "joy",
    "pride": "joy",
    "realization": "surprise",
    "relief": "joy",
    "remorse": "sadness",
    "sadness": "sadness",
    "surprise": "surprise",
    "breakup":"sad"
}

def detect_emotion(text):
    """
    Detect emotion from text input
    
    Args:
        text (str): User input text expressing their mood
        
    Returns:
        str: Mapped emotion category
    """
    if not text:
        return "neutral"
    
    try:
        # Get prediction from transformer model
        result = classifier(text)[0]
        raw_emotion = result['label'].lower()
        confidence = result['score']
        
        # Map to our emotion categories
        mapped_emotion = EMOTION_ALIASES.get(raw_emotion, "neutral")
        
        # Show confidence for debugging
        if confidence < 0.5:
            print(f"   (Low confidence: {confidence:.2%})")
        
        return mapped_emotion
        
    except Exception as e:
        print(f"⚠️  Error in emotion detection: {e}")
        print("   Defaulting to 'neutral'")
        return "neutral"
