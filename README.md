# 🎵 Emotion-Based Music Generator 🎵

A sophisticated AI-powered application that detects your emotion from text input and generates personalized music compositions in real-time.

## ✨ Features

- **AI Emotion Detection**: Uses transformer-based models to accurately detect emotions from text
- **Intelligent Music Generation**: Creates unique MIDI compositions based on detected emotions
- **Real-time Audio Conversion**: Converts MIDI to high-quality WAV audio
- **Cross-Platform Playback**: Works on Windows, macOS, and Linux
- **Rich Emotion Mapping**: 8+ emotion types with unique musical characteristics
- **Professional UI**: Beautiful terminal interface with progress indicators

## 📋 System Requirements

- **Python**: 3.8 or higher
- **RAM**: 2GB minimum (for model loading)
- **Disk Space**: 1GB for models and generated files
- **Audio Device**: Required for playback

## 🚀 Installation

### Step 1: Clone/Download Project
```bash
# Navigate to your project directory
cd emotion-music-generator
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Install System Audio Tools

#### Windows
- **Option A (Easiest)**: Install FluidSynth
  - Download from: http://www.fluidsynth.org/download/
  - Add to PATH environment variable
  
- **Option B**: Install Timidity
  - Download from: http://timidity.sourceforge.net/
  - Follow installation wizard

- **Option C (Fallback)**: App will use fallback synthesizer

#### macOS
```bash
brew install fluidsynth timidity
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install fluidsynth timidity
```

#### Linux (Fedora)
```bash
sudo dnf install fluidsynth timidity
```

## 🎮 Usage

### Basic Usage
```bash
python app.py
```

### Interaction Example
```
============================================================
         🎵 EMOTION-BASED MUSIC GENERATOR 🎵
============================================================

📝 Express your current mood or feeling:
   (e.g., 'I am very happy', 'feeling anxious today', 'I am excited!')

💭 Your mood: I'm feeling happy and energetic today!

⏳ Processing your emotion...
✨ Detected Emotion: JOY
   Mood: Uplifting & Bright

⏳ Generating music parameters...
   Tempo: 140 BPM
   Scale: Major

🎹 Creating MIDI composition...
   🎼 Composition: 4 variations
   🎹 Scale: Major
   ⚡ Intensity: ██████████

🔄 Converting MIDI to high-quality audio...
✅ WAV created: output.wav

▶️  Now playing your personalized music...
```

## 📊 Emotion Mapping

Each emotion is mapped to unique musical characteristics:

| Emotion | Tempo | Scale | Mood | Key |
|---------|-------|-------|------|-----|
| **Joy** | 140 BPM | Major | Uplifting & Bright | C |
| **Sadness** | 55 BPM | Minor | Melancholic & Reflective | A |
| **Anger** | 160 BPM | Minor | Intense & Aggressive | B |
| **Fear** | 95 BPM | Minor | Tense & Mysterious | C |
| **Surprise** | 130 BPM | Major | Dynamic & Energetic | D |
| **Love** | 85 BPM | Major | Warm & Tender | E |
| **Disgust** | 110 BPM | Minor | Uncomfortable & Edgy | C# |
| **Neutral** | 90 BPM | Major | Calm & Balanced | C |

## 🎼 Music Generation Algorithm

1. **Emotion Analysis**: Text → Emotion classification
2. **Parameter Mapping**: Emotion → Musical parameters
3. **Scale Selection**: Choose major or minor scale
4. **Pattern Generation**: Create melodic patterns based on intensity
5. **Chord Accompaniment**: Generate harmonic background
6. **Variation**: Add 3-5 musical variations
7. **MIDI Composition**: Compile all elements into MIDI
8. **Audio Conversion**: Convert MIDI → WAV
9. **Playback**: Play with multi-platform support

## 📁 Project Structure

```
emotion-music-generator/
├── app.py                    # Main application entry point
├── detector.py               # Emotion detection engine
├── config.py                 # Emotion-to-music parameter mapping
├── music_generator.py        # MIDI composition engine
├── audio_converter.py        # MIDI-to-WAV conversion
├── player.py                 # Audio playback engine
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── output.wav               # Generated audio (created after running)
```

## 🔧 Troubleshooting

### Issue: "FluidSynth not found"
**Solution**: 
- Windows: Install FluidSynth or Timidity (see Installation section)
- macOS: Run `brew install fluidsynth`
- Linux: Run `sudo apt-get install fluidsynth`

### Issue: "Audio file not playing"
**Solution**:
- Ensure audio device is connected and working
- Try installing pygame: `pip install pygame`
- Check file permissions in output directory

### Issue: "Model loading too slow"
**Solution**:
- This is normal for first run (downloads ~500MB model)
- Subsequent runs use cached model
- First load may take 1-2 minutes

### Issue: "MIDI conversion fails"
**Solution**:
- The app will automatically fallback to Python synthesizer
- Install optional dependency: `pip install scipy`
- Or install system audio tools (see Installation)

### Issue: "GPU out of memory"
**Solution**:
- Close other applications
- The model will use CPU if GPU unavailable
- Slow but functional

## 🎨 Customization

### Add Custom Emotions
Edit `config.py`:
```python
"custom_emotion": {
    "tempo": 100,
    "scale": "major",
    "mood_description": "Your mood",
    "intensity": 0.7,
    "key": 60,
    "variations": 4,
    "effects": "balanced"
}
```

### Adjust Music Parameters
In `config.py`:
- **tempo**: 40-200 BPM (beats per minute)
- **intensity**: 0.0-1.0 (how intense the music is)
- **variations**: 1-8 (number of musical sections)

### Modify Melody Patterns
In `music_generator.py`, edit the `base_patterns` list to create custom melodies.

## 📈 Performance

- **First Run**: 30-60 seconds (downloads emotion model)
- **Subsequent Runs**: 10-20 seconds
- **Music Generation**: 2-5 seconds
- **Audio Playback**: Depends on composition length (typically 30-60 seconds)

## 🐛 Debugging

Run with debug mode:
```python
# In app.py, uncomment:
import logging
logging.basicConfig(level=logging.DEBUG)
```

Check generated files:
```bash
# List MIDI files
ls -lh *.mid

# List WAV files
ls -lh *.wav
```

## 📝 License

This project is open source. Feel free to modify and distribute.

## 🙏 Acknowledgments

- **Transformers**: HuggingFace emotion model
- **MIDI**: midiutil library
- **Audio**: pygame and system audio tools

## 📧 Support

For issues:
1. Check the Troubleshooting section
2. Verify all dependencies are installed
3. Check file permissions
4. Try on a different machine if possible

## 🚀 Future Enhancements

- [ ] Real-time visualization of audio waveform
- [ ] MIDI file editing GUI
- [ ] More sophisticated chord progressions
- [ ] Custom instrument selection
- [ ] Music mixing and effects
- [ ] Export to multiple formats (MP3, FLAC, etc.)
- [ ] Web interface
- [ ] Mobile app version

---

**Enjoy your personalized emotional music! 🎵**
