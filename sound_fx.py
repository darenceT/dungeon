from clear_screen import ClearScreen
import pygame
from pygame import mixer
from pathlib import Path

class SoundFx:

    def __init__(self):
        pygame.init()
        self.__is_running = False

    @property
    def is_running(self):
        return self.__is_running
    
    @is_running.setter
    def is_running(self, bool):
        self.is_running = bool

    # @staticmethod
    def intro(self):
        self.__is_running = True
        mixer.music.load(Path('sound/Mysterious Strange Things - Yung Logos_short.mp3'))
        mixer.music.set_volume(0.6)
        mixer.music.play(-1)

    @staticmethod
    def in_game():
        mixer.music.load(Path('sound/Subterranean Howl - ELPHNT_short.mp3'))
        mixer.music.play(-1)

    @staticmethod
    def pause_menu(resume=False):
        if resume:
            mixer.music.unpause()
        else:
            mixer.music.pause()

    @staticmethod
    def lose():
        mixer.music.load(Path('sound/gameover.mp3'))
        mixer.music.play(-1)

    @staticmethod
    def win():
        mixer.music.load(Path('sound/win.mp3'))
        mixer.music.play(-1)

    
    @staticmethod
    def enter_room():
        """
        Sound for entering each room
        Credit https://stackoverflow.com/questions/53617967/play-music-and-sound-effects-on-top-of-each-other-pygame
        """
        # play a sound on channel 0 with a max time of 600 milliseconds
        mixer.Channel(0).play(pygame.mixer.Sound(Path('sound', 'enter_room.mp3')), maxtime=600)
        # channel.set_volume(0.5)  # play at 50% volume

    @staticmethod
    def pillar():
        mixer.Channel(1).play(pygame.mixer.Sound(Path('sound', 'pillar.mp3')), maxtime=600)
    
    @staticmethod
    def pit():
        mixer.Channel(1).play(pygame.mixer.Sound(Path('sound', 'pit.mp3')), maxtime=600)