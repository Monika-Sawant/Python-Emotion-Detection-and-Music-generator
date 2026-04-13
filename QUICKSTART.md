# 🚀 QUICK START GUIDE

## 5-Minute Setup

### Windows Users
1. Open Command Prompt in the project folder
2. Double-click `setup.bat`
3. Wait for installation to complete
4. Run: `python app.py`

### macOS/Linux Users
1. Open Terminal in the project folder
2. Run: `chmod +x setup.sh && ./setup.sh`
3. Wait for installation to complete
4. Run: `source venv/bin/activate && python app.py`

---

## Usage Examples

### Example 1: Happy Mood
```
💭 Your mood: I just got promoted at work! I'm so excited!

✨ Detected Emotion: JOY
   Tempo: 140 BPM
   Scale: Major (Uplifting & Bright)

🎵 Your personalized happy music plays...
```

### Example 2: Sad Mood
```
💭 Your mood: I'm feeling lonely and lost today

✨ Detected Emotion: SADNESS
   Tempo: 55 BPM
   Scale: Minor (Melancholic & Reflective)

🎵 Your personalized sad music plays...
```

### Example 3: Angry Mood
```
💭 Your mood: This is absolutely infuriating!

✨ Detected Emotion: ANGER
   Tempo: 160 BPM
   Scale: Minor (Intense & Aggressive)

🎵 Your personalized intense music plays...
```

---

## What to Expect

### First Run
- ⏳ **Loading model**: 30-60 seconds (one-time only)
- 🎵 **Music generation**: 2-5 seconds
- 🔊 **Audio playback**: 30-60 seconds

### Subsequent Runs
- 🎵 **Music generation**: 2-5 seconds
- 🔊 **Audio playback**: 30-60 seconds

---

## Troubleshooting

### Issue: "Module not found"
**Solution**: Reinstall dependencies
```bash
pip install -r requirements.txt
```

### Issue: "No module named pygame"
**Solution**: Install pygame manually
```bash
pip install pygame
```

### Issue: "Audio won't play"
**Solution**: Try with verbose mode
```bash
python app.py
```

### Issue: "Model loading hangs"
**Solution**: 
- First run downloads ~500MB
- This is normal, be patient
- Ctrl+C to cancel, but model should finish

---

## Features to Try

### 1. Express Complex Emotions
```
"I'm happy but also nervous about tomorrow"
```
The AI will detect the dominant emotion!

### 2. Different Languages (with limitations)
```
"Je suis très heureux" (French)
"Soy muy feliz" (Spanish)
```

### 3. Creative Descriptions
```
"Like a sunny day after a storm"
"As excited as a kid on Christmas"
"The calm before a big event"
```

---

## Tips & Tricks

✨ **Tip 1**: Be descriptive about your mood
- Bad: "happy"
- Good: "I'm incredibly happy and energetic"

✨ **Tip 2**: Use emotional vocabulary
- "elated", "ecstatic", "overjoyed"
- "depressed", "melancholic", "sorrowful"
- "furious", "enraged", "livid"

✨ **Tip 3**: The model understands context
- "I'm nervous but excited"
- "Happy but tired"
- "Frustrated yet determined"

✨ **Tip 4**: Generated files are saved
- Check your project folder for `output.mid` and `output.wav`
- You can keep these files or delete them

---

## System Requirements Check

```bash
# Check Python version
python --version

# Should be 3.8 or higher
```

---

## Next Steps

Once you're comfortable with the basics:

1. **Customize Music**: Edit `config.py` to change tempo, scales, etc.
2. **Add Emotions**: Add new emotion types to the mapping
3. **Modify Patterns**: Edit melody patterns in `music_generator.py`
4. **Create Playlists**: Run multiple times and keep the WAV files

---

## Support

If something goes wrong:

1. **Check README.md**: Complete documentation
2. **Review error messages**: They're descriptive
3. **Check file permissions**: Especially on macOS/Linux
4. **Try with a fresh venv**: Virtual environment can help

---

## Have Fun! 🎵

Now you have a fully functional emotion-based music generator!

Try different moods, experiment with descriptions, and enjoy your personalized music! 🎶

---

**Questions?** Check README.md for complete documentation.
