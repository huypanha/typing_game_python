import pygame


class Singleton:
    _instance = None
    _user_name = None

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

    def get_screen(self):
        return self.screen

    def get_screen_size(self):
        return self._sw, self._sh

    def set_user_name(self, name):
        self._user_name = name

    def get_user_name(self):
        return self._user_name
