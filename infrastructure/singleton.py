import pygame
import threading


class Singleton:
    __instance = None
    __user_name = None
    __selected_num_letters = 3
    threads = None

    # sound
    __default_sound = None
    __birds_sound = None
    __num_sound_channel = 3
    __default_sound_channel = None
    __birds_sound_channel = None

    # characters
    __ch1_seq = []
    __ch2_seq = []
    __selected_character_index = 0

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self):
        pygame.init()
        self.__sw = 1280
        self.__sh = 720
        self.screen = pygame.display.set_mode((self.__sw, self.__sh))

        # sound
        pygame.mixer.set_num_channels(self.__num_sound_channel)
        self.__default_sound_channel = pygame.mixer.Channel(0)
        self.__birds_sound_channel = pygame.mixer.Channel(1)
        self.__default_sound = pygame.mixer.Sound("media/sounds/background.ogg")
        self.__birds_sound = pygame.mixer.Sound("media/sounds/birds.ogg")
        # self.play_default_sound()
        # self.play_birds_sound()

    def get_screen(self):
        return self.screen

    def get_screen_size(self):
        return self.__sw, self.__sh

    def set_user_name(self, name):
        self.__user_name = name

    def get_user_name(self):
        return self.__user_name

    def set_num_letters(self, value):
        self.__selected_num_letters = value

    def get_num_letters(self):
        return self.__selected_num_letters

    def set_birds_sound(self, new_sound):
        self.__birds_sound = new_sound

    def play_default_sound(self):
        self.__default_sound_channel.play(self.__default_sound, loops=-1)

    def play_birds_sound(self):
        self.__birds_sound_channel.play(self.__birds_sound, loops=-1)

    @staticmethod
    def play_click_button():
        pass
        # pygame.mixer.Channel(2).play(pygame.mixer.Sound("media/sounds/button_click.ogg"))

    def start_thread(self, target):
        self.threads = threading.Thread(target=target)
        self.threads.start()

    # character
    def set_character1(self, value):
        self.__ch1_seq = value

    def get_character1(self):
        return self.__ch1_seq

    def set_character2(self, value):
        self.__ch2_seq = value

    def get_character2(self):
        return self.__ch2_seq

    def set_selected_character_index(self, value):
        self.__selected_character_index = value

    def get_selected_character_index(self):
        return self.__selected_character_index
