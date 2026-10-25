"""
Module Name: MP3 Audio Player
Description: Plays an MP3 audio file using the pygame library, with optional volume control.
Author: Kollier
"""

import os
import time
import pygame

def play_mp3(file_path: str, volume: float = 0.8) -> None:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(
            f"Audio file not found: '{file_path}'"
        )

    if not 0.0 <= volume <= 1.0:
        raise ValueError("Volume must be between 0.0 and 1.0.")

    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        print(f"Playing: {os.path.basename(file_path)}")

        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

        print("Playback finished.")

    except pygame.error as error:
        print(f"Error playing the audio file: {error}")

    finally:
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit()

if __name__ == "__main__":
    audio_path = input("Enter the path of the MP3 file: ").strip()

    try:
        play_mp3(audio_path)

    except FileNotFoundError as error:
        print(f"Error: {error}")

    except ValueError as error:
        print(f"Error: {error}")