"""
Advanced music composition engine with emotion-aware patterns
"""

from midiutil import MIDIFile
import random
import math

def create_music(params, filename="output.mid"):
    """
    Create sophisticated MIDI music based on emotion parameters
    
    Args:
        params (dict): Emotion-based music parameters
        filename (str): Output MIDI file path
        
    Returns:
        str: Path to created MIDI file
    """
    
    midi = MIDIFile(2)  # 2 tracks: melody + accompaniment
    
    # ========== SETUP ==========
    tempo = params["tempo"]
    intensity = params["intensity"]
    scale_type = params["scale"]
    key = params["key"]
    variations = params["variations"]
    
    # Set tempo
    midi.addTempo(0, 0, tempo)
    midi.addTempo(1, 0, tempo)
    
    # ========== DEFINE SCALES ==========
    if scale_type == "major":
        scale_intervals = [0, 2, 4, 5, 7, 9, 11]  # Major scale intervals
        chords_intervals = [[0, 4, 7], [5, 9, 12], [7, 11, 14]]  # I, IV, V chords
    else:  # minor
        scale_intervals = [0, 2, 3, 5, 7, 8, 10]  # Natural minor
        chords_intervals = [[0, 3, 7], [5, 8, 12], [7, 10, 14]]  # i, iv, v chords
    
    # Build full scale
    scale = [key + interval for interval in scale_intervals]
    chords = [[key + interval for interval in chord] for chord in chords_intervals]
    
    # ========== MELODIC PATTERNS ==========
    # Different patterns based on intensity
    if intensity > 0.8:  # High intensity
        base_patterns = [
            [0, 2, 4, 5, 4, 2, 6, 5],
            [0, 1, 2, 3, 4, 5, 6, 0],
            [2, 4, 5, 6, 5, 4, 2, 1],
            [0, 3, 5, 6, 5, 3, 0, 2]
        ]
    elif intensity < 0.6:  # Low intensity
        base_patterns = [
            [0, 2, 3, 2, 0, 1, 0, 2],
            [0, 1, 2, 1, 0, 0, 0, 1],
            [3, 2, 1, 0, 1, 2, 3, 2],
            [0, 0, 2, 2, 3, 3, 2, 1]
        ]
    else:  # Medium intensity
        base_patterns = [
            [0, 2, 4, 5, 4, 2, 6, 3],
            [0, 1, 3, 4, 3, 1, 5, 2],
            [2, 3, 4, 5, 4, 3, 2, 0],
            [1, 2, 4, 5, 3, 2, 1, 0]
        ]
    
    # ========== COMPOSITION ==========
    time = 0
    beat_duration = 0.5  # Quarter note
    
    for variation in range(variations):
        pattern = base_patterns[variation % len(base_patterns)]
        chord = chords[variation % len(chords)]
        
        # Add variation through octave changes
        octave_offset = random.randint(-1, 1) * 12 if variation > 0 else 0
        
        # 🎼 Chord accompaniment (lower notes)
        for chord_note in chord:
            volume_acc = int(60 + intensity * 30)
            midi.addNote(1, 0, chord_note - 12, time, beat_duration * 4, volume_acc)
        
        # 🎵 Melody line (upper notes)
        for step in pattern:
            # Add some note variations
            if random.random() < 0.15 and variation > 0:  # 15% chance of variation
                melody_step = (step + random.choice([-1, 1])) % len(scale)
            else:
                melody_step = step
            
            note = scale[melody_step % len(scale)] + octave_offset
            volume_melody = int(80 + intensity * 40)
            
            # Vary duration slightly for humanization
            duration = beat_duration * random.uniform(0.9, 1.1)
            
            midi.addNote(0, 0, note, time, duration, volume_melody)
            time += beat_duration
    
    # ========== ADD DECORATIVE ELEMENTS ==========
    if intensity > 0.7:
        # Add percussion track for energetic emotions
        add_percussion(midi, time, tempo)
    
    # ========== WRITE FILE ==========
    with open(filename, "wb") as f:
        midi.writeFile(f)
    
    print(f"   🎼 Composition: {variations} variations")
    print(f"   🎹 Scale: {scale_type.capitalize()}")
    print(f"   ⚡ Intensity: {'█' * int(intensity * 10)}{'░' * (10 - int(intensity * 10))}")
    
    return filename


def add_percussion(midi, start_time, tempo):
    """Add percussion elements to accompany the melody"""
    # Percussion channel
    beat_duration = 0.5
    drum_notes = [36, 38, 42, 46]  # Kick, snare, hi-hat, open hat
    
    for i in range(8):
        drum = random.choice(drum_notes)
        midi.addNote(1, 9, drum, start_time + i * beat_duration, beat_duration * 0.8, 90)


def generate_arpeggio(scale, chord, variations=3):
    """Generate arpeggiated chord patterns"""
    arpeggios = []
    for _ in range(variations):
        arpeggio = chord + chord[::-1]
        arpeggios.append(arpeggio)
    return arpeggios
