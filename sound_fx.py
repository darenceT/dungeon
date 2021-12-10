import pygame
from pygame import mixer


class SoundFx:

    @staticmethod
    def intro(stop=False):
        pygame.init()
        mixer.music.load('sound\Mysterious Strange Things - Yung Logos.mp3')
        mixer.music.set_volume(0.5)
        mixer.music.play(-1)

    @staticmethod
    def in_game(stop=False):
        mixer.music.load('sound\Subterranean Howl - ELPHNT.mp3')
        mixer.music.play(-1)

    @staticmethod
    def pause_menu(resume=False):
        if resume:
            mixer.music.unpause()
        else:
            mixer.music.pause()

