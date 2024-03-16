import pygame


class Singleton:
    _instance = None
    _user_name = None
    _selected_character_index = None
    _default_sound = None
    _birds_sound = None
    _num_sound_channel = 2
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

    def get_default_sound(self):
        return self._default_sound

    def set_default_sound(self, new_sound):
        self._default_sound = new_sound

    def get_birds_sound(self):
        return self._birds_sound

    def set_birds_sound(self, new_sound):
        self._birds_sound = new_sound

    def play_default_sound(self):
        self._default_sound_channel.play(self._default_sound)

    def play_birds_sound(self):
        self._birds_sound_channel.play(self._birds_sound)
