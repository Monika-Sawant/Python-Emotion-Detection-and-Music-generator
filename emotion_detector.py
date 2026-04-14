import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import cv2
import numpy as np
from PIL import Image, ImageTk
import threading
import speech_recognition as sr
from scipy import signal
import os
import pygame

# Initialize Pygame Mixer
try:
    import pygame
    pygame.mixer.init(frequency=44100, size=-16, channels=2)
except ImportError:
    os.system("pip install pygame --quiet")
    import pygame
    pygame.mixer.init()

try:
    from transformers import pipeline
except ImportError:
    os.system("pip install transformers torch --quiet")
    from transformers import pipeline

# Load Models
print("Loading emotion detection models...")
emotion_classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

class MusicGenerator:
    @staticmethod
    def generate_emotion_music(emotion, duration=15):
        sample_rate = 44100
        total_samples = int(sample_rate * duration)
        
        emotion_params = {
            'happy': {'base_freq': 523.25, 'harmonics': [1.25, 1.5], 'vibrato_depth': 0.005, 'volume': 0.2},
            'sad': {'base_freq': 196.00, 'harmonics': [1.2, 1.5], 'vibrato_depth': 0.002, 'volume': 0.15},
            'angry': {'base_freq': 110.00, 'harmonics': [1.05, 1.1], 'vibrato_depth': 0.02, 'volume': 0.3},
            'neutral': {'base_freq': 261.63, 'harmonics': [1.5, 2.0], 'vibrato_depth': 0.003, 'volume': 0.2},
        }
        
        params = emotion_params.get(emotion.lower(), emotion_params['neutral'])
        t = np.linspace(0, duration, total_samples, False)
        
        # Smooth Vibrato (not an ambulance!)
        vibrato = np.sin(2 * np.pi * 4.0 * t) 
        freq_mod = params['base_freq'] * (1 + params['vibrato_depth'] * vibrato)
        
        main_wave = np.sin(2 * np.pi * freq_mod * t)
        harmony = np.zeros_like(t)
        for h in params['harmonics']:
            harmony += 0.5 * np.sin(2 * np.pi * (freq_mod * h) * t)
        
        combined = main_wave + harmony
        
        # Fade in/out
        envelope = np.ones_like(t)
        fade = int(sample_rate * 1.5)
        envelope[:fade] = np.linspace(0, 1, fade)
        envelope[-fade:] = np.linspace(1, 0, fade)
        
        music = (combined * envelope)
        music = music / np.max(np.abs(music))
        music_int16 = (music * params['volume'] * 32767).astype(np.int16)
        
        return np.column_stack((music_int16, music_int16)), sample_rate

class EmotionDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Detection System")
        self.root.geometry("900x700")
        
        self.music_generator = MusicGenerator()
        self.recognizer = sr.Recognizer()
        self.current_emotion = None
        self.is_camera_running = False
        
        self.setup_ui()

    def setup_ui(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Facial Tab
        self.facial_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.facial_frame, text="Facial Recognition")
        self.camera_label = tk.Label(self.facial_frame, bg='black', width=60, height=20)
        self.camera_label.pack(pady=10)
        self.emotion_display_label = tk.Label(self.facial_frame, text="Emotion: Detecting...", font=("Arial", 12, "bold"))
        self.emotion_display_label.pack()
        
        btn_f = tk.Frame(self.facial_frame)
        btn_f.pack()
        self.camera_button = tk.Button(btn_f, text="Start Camera", command=self.start_camera, bg='green', fg='white')
        self.camera_button.pack(side=tk.LEFT, padx=5)
        self.stop_camera_button = tk.Button(btn_f, text="Stop Camera", command=self.stop_camera, bg='red', fg='white', state=tk.DISABLED)
        self.stop_camera_button.pack(side=tk.LEFT, padx=5)
        tk.Button(btn_f, text="Play Music", command=lambda: self.play_music(self.current_emotion), bg='blue', fg='white').pack(side=tk.LEFT)

        # Text Tab
        self.text_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.text_frame, text="Text Analysis")
        self.text_input = scrolledtext.ScrolledText(self.text_frame, height=5)
        self.text_input.pack(pady=10)
        tk.Button(self.text_frame, text="Analyze", command=self.analyze_text).pack()
        self.text_emotion_label = tk.Label(self.text_frame, text="Emotion: Waiting...", font=("Arial", 12, "bold"))
        self.text_emotion_label.pack()
        tk.Button(self.text_frame, text="Play Music", command=lambda: self.play_music(self.current_emotion), bg='blue', fg='white').pack()

        # Voice Tab
        self.voice_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.voice_frame, text="Voice Input")
        self.record_button = tk.Button(self.voice_frame, text="Start Recording", command=self.start_voice, bg='green', fg='white')
        self.record_button.pack(pady=10)
        # FIX: Added the missing voice_status_label
        self.voice_status_label = tk.Label(self.voice_frame, text="Ready", fg="gray")
        self.voice_status_label.pack()
        self.voice_emotion_label = tk.Label(self.voice_frame, text="Emotion: Waiting...", font=("Arial", 12, "bold"))
        self.voice_emotion_label.pack()
        tk.Button(self.voice_frame, text="Play Music", command=lambda: self.play_music(self.current_emotion), bg='blue', fg='white').pack()

        self.status_label = tk.Label(self.root, text="Ready", bg='lightgray')
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def start_camera(self):
        self.is_camera_running = True
        self.camera_button.config(state=tk.DISABLED)
        self.stop_camera_button.config(state=tk.NORMAL)
        threading.Thread(target=self.camera_loop, daemon=True).start()

    def camera_loop(self):
        cap = cv2.VideoCapture(0)
        while self.is_camera_running:
            ret, frame = cap.read()
            if not ret: break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            if len(faces) > 0:
                x,y,w,h = faces[0]
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
                brightness = np.mean(gray[y:y+h, x:x+w])
                self.current_emotion = 'happy' if brightness > 120 else 'sad'
                self.emotion_display_label.config(text=f"Emotion: {self.current_emotion.upper()}")
            
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            imgtk = ImageTk.PhotoImage(image=img)
            self.camera_label.config(image=imgtk)
            self.camera_label.image = imgtk
        cap.release()

    def stop_camera(self):
        self.is_camera_running = False
        self.camera_button.config(state=tk.NORMAL)
        self.stop_camera_button.config(state=tk.DISABLED)

    def analyze_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if text:
            res = emotion_classifier(text)
            self.current_emotion = 'happy' if res[0]['label'] == 'POSITIVE' else 'sad'
            self.text_emotion_label.config(text=f"Emotion: {self.current_emotion.upper()}")

    def start_voice(self):
        self.record_button.config(state=tk.DISABLED)
        self.voice_status_label.config(text="Listening...", fg="red")
        threading.Thread(target=self.voice_loop, daemon=True).start()

    def voice_loop(self):
        try:
            with sr.Microphone() as source:
                audio = self.recognizer.listen(source, timeout=10)
            text = self.recognizer.recognize_google(audio)
            res = emotion_classifier(text)
            self.current_emotion = 'happy' if res[0]['label'] == 'POSITIVE' else 'sad'
            self.voice_emotion_label.config(text=f"Emotion: {self.current_emotion.upper()}")
            self.voice_status_label.config(text="Done!", fg="green")
        except Exception:
            self.voice_status_label.config(text="Try again", fg="red")
        finally:
            self.record_button.config(state=tk.NORMAL)

    def play_music(self, emotion):
        if not emotion:
            messagebox.showwarning("Wait", "Detect emotion first!")
            return
        threading.Thread(target=self._play_thread, args=(emotion,), daemon=True).start()

    def _play_thread(self, emotion):
        try:
            music, sr_rate = self.music_generator.generate_emotion_music(emotion)
            sound = pygame.sndarray.make_sound(music)
            self.status_label.config(text=f"Playing {emotion} music...")
            chan = sound.play()
            while chan.get_busy(): pygame.time.wait(100)
            self.status_label.config(text="Ready")
        except Exception as e:
            print(f"Playback error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionDetectionApp(root)
    root.mainloop()