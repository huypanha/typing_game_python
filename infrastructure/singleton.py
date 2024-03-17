import pygame


class Singleton:
    _instance = None
    _user_name = None
    _selected_character_index = 0
    _selected_num_letters = 3

    # sound
    _default_sound = None
    _birds_sound = None
    _num_sound_channel = 3
    _default_sound_channel = None
    _birds_sound_channel = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        pygame.init()
        self._sw = 1280
        self._sh = 720
        self.screen = pygame.display.set_mode((self._sw, self._sh))

        # sound
        pygame.mixer.set_num_channels(self._num_sound_channel)
        self._default_sound_channel = pygame.mixer.Channel(0)
        self._birds_sound_channel = pygame.mixer.Channel(1)
        self._default_sound = pygame.mixer.Sound("media/sounds/background.ogg")
        self._birds_sound = pygame.mixer.Sound("media/sounds/birds.ogg")
        self.play_default_sound()
        self.play_birds_sound()

    def get_screen(self):
        return self.screen

    def get_screen_size(self):
        return self._sw, self._sh

    def set_user_name(self, name):
        self._user_name = name

    def get_user_name(self):
        return self._user_name

    def set_character(self, index):
        self._selected_character_index = index

    def get_character_index(self):
        return self._selected_character_index

    def set_num_letters(self, value):
        self._selected_num_letters = value

    def get_num_letters(self):
        return self._selected_num_letters

    def set_birds_sound(self, new_sound):
        self._birds_sound = new_sound

    def play_default_sound(self):
        self._default_sound_channel.play(self._default_sound, loops=-1)

    def play_birds_sound(self):
        self._birds_sound_channel.play(self._birds_sound, loops=-1)

    @staticmethod
    def play_click_button():
        pygame.mixer.Channel(2).play(pygame.mixer.Sound("media/sounds/button_click.ogg"))
