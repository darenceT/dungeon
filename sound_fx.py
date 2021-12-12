from clear_screen import ClearScreen
import pygame
from pygame import mixer
from pathlib import Path

class SoundFx:

    def __pick_option(self):
        while True:
            pick = input("                    Enter your pick: ").strip()
            if not pick.isnumeric():
                print("Only integers 0 or greater accepted")
                continue
            if int(pick) > 3:
                print('Only integers between 0 to 3 accepted')
                continue
            return int(pick)

    @staticmethod
    def intro(stop=False):
        pygame.init()
        mixer.music.load(Path('sound/Mysterious Strange Things - Yung Logos_short.mp3'))
        mixer.music.set_volume(0.7)
        mixer.music.play(-1)

    @staticmethod
    def options():
        pick = -1
        while pick != 0:
            ClearScreen()
            print("\n\n\n\n                     DUNGEON CRAWLER\n\n\n"
                  "                            * Sound Options *\n\n\n"
                  "                     [1] Turn music off\n"
                  "                     [2] Game Instructions\n"
                  "                     [3] Sound options\n"
                  "                     [0] Exit Game\n\n")
            break

    @staticmethod
    def in_game(stop=False):
        mixer.music.load(Path('sound/Subterranean Howl - ELPHNT_short.mp3'))
        mixer.music.play(-1)

    @staticmethod
    def pause_menu(resume=False):
        # mixer.music.load('sound\Mind And Eye Journey - Emily A. Sprague.mp3')
        # mixer.music.play(-1)
        if resume:
            mixer.music.unpause()
        else:
            mixer.music.pause()

    @staticmethod
    def lose():
        pass
        # mixer.music.load(Path('sound/{insert here}.mp3'))
        # mixer.music.play(-1)

    @staticmethod
    def win():
        pass
        # mixer.music.load(Path('sound/{insert here}.mp3'))
        # mixer.music.play(-1)