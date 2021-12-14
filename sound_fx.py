import pygame
from pygame import mixer
from pathlib import Path


class SoundFx:
    """
    Constructor/instance included so that a tracker can be used for sound options,
    to turn off and on the sound & music.
    """
    def __init__(self):
        self.__is_running = True
        pygame.init()
        mixer.Channel(0).set_volume(0.75)

    @property
    def is_running(self):
        return self.__is_running

    @is_running.setter
    def is_running(self, change):
        if isinstance(change, bool):
            self.__is_running = change
        else:
            raise TypeError("Only boolean param accepted")

    def turn_off(self):
        self.__is_running = False
        mixer.quit()

    def turn_on(self, in_game=False):
        if isinstance(in_game, bool):
            self.__is_running = True
            mixer.init()
            if in_game:
                self.in_game()
            else:
                self.intro()
        else:
            raise TypeError("Only boolean param accepted")

    def low_volume(self):
        if self.__is_running:
            mixer.music.set_volume(0.1)
            mixer.Channel(0).set_volume(0.25)  # play at 100% volume

    def normal_volume(self):
        if self.__is_running:
            mixer.music.set_volume(0.4)
            mixer.Channel(0).set_volume(0.75)  # play at 50% volume

    def high_volume(self):
        if self.__is_running:
            mixer.music.set_volume(0.7)
            mixer.Channel(0).set_volume(1)  # play at 50% volume

    def intro(self):
        if self.__is_running:
            mixer.music.load(Path('sound/Mysterious Strange Things - Yung Logos_short.mp3'))
            mixer.music.set_volume(0.5)
            mixer.music.play(-1)

    def in_game(self):
        if self.__is_running:
            mixer.music.load(Path('sound/Subterranean Howl - ELPHNT_short.mp3'))
            mixer.music.set_volume(0.5)
            mixer.music.play(-1)

    def pause_menu(self, resume=False):
        if resume:
            mixer.music.unpause()
        else:
            mixer.music.pause()

    def lose(self):
        if self.__is_running:
            mixer.music.load(Path('sound/gameover.mp3'))
            mixer.music.play(-1)

    def win(self):
        if self.__is_running:
            mixer.music.load(Path('sound/win.mp3'))
            mixer.music.play(-1)

    
    def enter_room(self):
        """
        Sound for entering each room
        Credit https://stackoverflow.com/questions/53617967/play-music-and-sound-effects-on-top-of-each-other-pygame
        """
        if self.__is_running:
            # play a sound on channel 0 with a max time of 600 milliseconds
            mixer.Channel(0).play(pygame.mixer.Sound(Path('sound', 'enter_room.mp3')), maxtime=600)
            # channel.set_volume(0.5)  # play at 50% volume

    def pillar(self):
        if self.__is_running:
            mixer.Channel(1).play(pygame.mixer.Sound(Path('sound', 'pillar.mp3')), maxtime=600)
    
    def pit(self):
        if self.__is_running:
            mixer.Channel(1).play(pygame.mixer.Sound(Path('sound', 'pit.mp3')), maxtime=600)
            