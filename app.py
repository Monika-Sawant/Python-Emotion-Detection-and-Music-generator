import os
import sys
from detector import detect_emotion
from config import get_music_params
from music_generator import create_music
from audio_converter import midi_to_wav
from player import play_music


# Get the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def print_header():
    """Print a stylish header"""
    print("\n" + "="*60)
    print("🎵 EMOTION-BASED MUSIC GENERATOR 🎵".center(60))
    print("="*60 + "\n")

def main():
    print_header()
    
    try:
        # Get mood input from user
        print("📝 Express your current mood or feeling:")
        print("   (e.g., 'I am very happy', 'feeling anxious today', 'I am excited!')")
        text = input("\n💭 Your mood: ").strip()
        
        if not text:
            print("❌ Please enter a mood!")
            return
        
        print("\n⏳ Processing your emotion...")
        emotion = detect_emotion(text)
        print(f"✨ Detected Emotion: {emotion.upper()}")
        
        print("\n⏳ Generating music parameters...")
        params = get_music_params(emotion)
        print(f"   Tempo: {params['tempo']} BPM")
        print(f"   Scale: {params['scale'].capitalize()}")
        print(f"   Mood: {params['mood_description']}")
        
        print("\n🎹 Creating MIDI composition...")
        midi_file = create_music(params)
        print(f"✅ MIDI created: {os.path.basename(midi_file)}")
        
        print("\n🔄 Converting MIDI to high-quality audio...")
        wav_file = midi_to_wav(midi_file)
        print(f"✅ WAV created: {os.path.basename(wav_file)}")
        
        print("\n▶️  Now playing your personalized music...\n")
        print("-" * 60)
        play_music(wav_file)
        print("-" * 60)
        
        print("\n✅ Music playback completed!")
        print(f"📁 Your audio saved as: {os.path.abspath(wav_file)}\n")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Playback cancelled by user.")
    except FileNotFoundError as e:
        print(f"\n❌ Error: {e}")
        print("   Make sure all required files are in the correct directory.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("   Please check your configuration and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
