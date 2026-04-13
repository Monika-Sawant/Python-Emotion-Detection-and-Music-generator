"""
Audio playback engine with multiple backend support
"""

import os
import subprocess
import platform
import time
import sys

def play_music(file):
    """
    Play audio file with automatic backend selection
    
    Args:
        file (str): Path to audio file
        
    Raises:
        FileNotFoundError: If audio file doesn't exist
    """
    
    path = os.path.abspath(file)
    
    # Verify file exists
    if not os.path.isfile(path):
        raise FileNotFoundError(f"❌ Audio file not found: {path}")
    
    # Verify file has content
    file_size = os.path.getsize(path)
    if file_size < 100:
        raise FileNotFoundError(f"❌ Audio file is empty or too small: {file_size} bytes")
    
    print(f"📂 File: {os.path.basename(path)}")
    print(f"💾 Size: {file_size / (1024 * 1024):.2f} MB")
    
    system = platform.system()
    success = False
    
    # Try OS-specific players first
    if system == "Windows":
        success = _play_windows(path)
    elif system == "Darwin":  # macOS
        success = _play_macos(path)
    elif system == "Linux":
        success = _play_linux(path)
    
    if not success:
        # Fallback to pygame
        success = _play_pygame(path)
    
    if not success:
        raise RuntimeError(
            "❌ Could not play audio file.\n"
            "   Please install: pip install pygame\n"
            "   Or install a system audio player (ffplay, mpv, etc.)"
        )


def _play_windows(path):
    """Play audio on Windows using built-in player"""
    try:
        # Use Windows Media Player or winsound
        try:
            import winsound
            print("🔊 Using Windows Media Player...")
            winsound.PlaySound(path, winsound.SND_FILENAME)
            return True
        except ImportError:
            # Fallback to PowerShell
            cmd = f'Add-Type -AssemblyName PresentationCore; (New-Object System.Windows.Media.MediaPlayer).Open("{path}"); Start-Sleep -Seconds 10'
            subprocess.run(
                ["powershell", "-Command", cmd],
                timeout=60
            )
            return True
    except Exception as e:
        print(f"   Windows player failed: {e}")
        return False


def _play_macos(path):
    """Play audio on macOS"""
    try:
        print("🔊 Using afplay...")
        subprocess.run(
            ["afplay", path],
            timeout=120,
            check=True
        )
        return True
    except Exception as e:
        print(f"   macOS player failed: {e}")
        return False


def _play_linux(path):
    """Play audio on Linux"""
    players = ["mpv", "ffplay", "paplay", "aplay"]
    
    for player in players:
        try:
            print(f"🔊 Using {player}...")
            subprocess.run(
                [player, path],
                timeout=120,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired, subprocess.CalledProcessError):
            continue
    
    return False


def _play_pygame(path):
    """Fallback: Play audio using pygame"""
    try:
        import pygame
        
        print("🔊 Using pygame audio engine...")
        pygame.init()
        pygame.mixer.init()
        
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        
        # Show playback progress
        duration = pygame.mixer.Sound(path).get_length()
        print(f"⏱️  Duration: {duration:.1f} seconds")
        
        # Play with progress indicator
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
        pygame.quit()
        return True
        
    except ImportError:
        print("   ❌ pygame not installed")
        return False
    except Exception as e:
        print(f"   pygame playback failed: {e}")
        return False


def show_playback_status():
    """Display colorful playback status"""
    statuses = ["🎵", "🎶", "🎼", "♪", "♫"]
    for status in statuses * 3:
        print(f"\r{status} Now playing...", end="", flush=True)
        time.sleep(0.1)
    print("\n")
