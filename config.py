"""
Enhanced emotion to music parameter mapping
"""

def get_music_params(emotion):
    """
    Maps emotions to musical parameters
    
    Returns:
        dict: Contains tempo, scale, mood_description, instrument_intensity, etc.
    """
    mapping = {
        "joy": {
            "tempo": 140,
            "scale": "major",
            "mood_description": "Uplifting & Bright",
            "intensity": 0.9,
            "key": 60,  # C note
            "variations": 4,
            "effects": "bright"
        },
        "sadness": {
            "tempo": 55,
            "scale": "minor",
            "mood_description": "Melancholic & Reflective",
            "intensity": 0.5,
            "key": 57,  # A note
            "variations": 3,
            "effects": "soft"
        },
        "anger": {
            "tempo": 160,
            "scale": "minor",
            "mood_description": "Intense & Aggressive",
            "intensity": 1.0,
            "key": 59,  # B note
            "variations": 5,
            "effects": "sharp"
        },
        "fear": {
            "tempo": 95,
            "scale": "minor",
            "mood_description": "Tense & Mysterious",
            "intensity": 0.7,
            "key": 60,  # C note
            "variations": 3,
            "effects": "dark"
        },
        "surprise": {
            "tempo": 130,
            "scale": "major",
            "mood_description": "Dynamic & Energetic",
            "intensity": 0.85,
            "key": 62,  # D note
            "variations": 4,
            "effects": "bright"
        },
        "neutral": {
            "tempo": 90,
            "scale": "major",
            "mood_description": "Calm & Balanced",
            "intensity": 0.6,
            "key": 60,  # C note
            "variations": 3,
            "effects": "balanced"
        },
        "love": {
            "tempo": 85,
            "scale": "major",
            "mood_description": "Warm & Tender",
            "intensity": 0.7,
            "key": 64,  # E note
            "variations": 3,
            "effects": "soft"
        },
        "disgust": {
            "tempo": 110,
            "scale": "minor",
            "mood_description": "Uncomfortable & Edgy",
            "intensity": 0.6,
            "key": 61,  # C# note
            "variations": 3,
            "effects": "dark"
        }
    }
    
    # Default to neutral if emotion not recognized
    return mapping.get(emotion, mapping["neutral"])
