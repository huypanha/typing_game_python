import pygame
import threading
from utils import scale_img as siw


class Singleton:
    __instance = None
    __user_name = None
    __selected_num_letters = 3

    # loading
    threads = None

    # sound
    __birds_sound = None
    __click_button_sound = None
    __default_sound_channel = None
    __birds_sound_channel = None
    __num_sound_channel = 6
    """
    Number of channel:
    0: Background
    1: Second sound (birth)
    2: Button Click and typing sound
    3: Countdown
    4: Typing letter power and wrong
    5: Finish sound
    """

    # sound button
    __is_muted = False
    __mute_unmute_button_img = None

    # characters
    __character_seq_list = []
    __selected_character_index = 0
    __small_character_seq_list = []
    __small_selected_character_index = 0

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
        self.__birds_sound = pygame.mixer.Sound("src/sounds/birds.ogg")
        self.__click_button_sound = pygame.mixer.Sound("src/sounds/button_click.ogg")
        self.play_background_sound()
        self.play_birds_sound()

        # sound button
        self.sound_button_size = 50
        self.__mute_unmute_button_img = siw.width(pygame.image.load("src/unmuted.png").convert_alpha(),
                                                  self.sound_button_size)

        # background
        self.default_back_img = pygame.transform.scale(pygame.image.load('src/background.jpg').convert(),
                                                       self.get_screen_size())

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

    # sound
    def set_birds_sound(self, new_sound):
        self.__birds_sound = new_sound

    def play_background_sound(self, path="src/sounds/background.ogg"):
        if not self.__is_muted and not self.__default_sound_channel.get_busy():
            self.__default_sound_channel.play(pygame.mixer.Sound(path), loops=-1)

    def play_birds_sound(self):
        if not self.__is_muted:
            self.__birds_sound_channel.play(self.__birds_sound, loops=-1)

    def stop_background_sound(self):
        self.__default_sound_channel.stop()

    def stop_birds_sound(self):
        self.__birds_sound_channel.stop()

    def play_click_button(self):
        if not self.__is_muted:
            pygame.mixer.Channel(2).play(self.__click_button_sound)

    def play_typing_sound(self):
        if not self.__is_muted:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("src/sounds/typing.ogg"))

    def play_finish_sound(self):
        if not self.__is_muted:
            pygame.mixer.Channel(5).play(pygame.mixer.Sound("src/sounds/finish.ogg"))

    def play_countdown_sound(self):
        if not self.__is_muted:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("src/sounds/countdown.ogg"))

    def play_countdown_end_sound(self):
        if not self.__is_muted:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("src/sounds/countdown_end.ogg"))

    def toggle_mute_normal_sound(self):
        if self.__is_muted:
            self.__is_muted = not self.__is_muted
            self.__mute_unmute_button_img = siw.width(pygame.image.load("src/unmuted.png").convert_alpha(),
                                                      self.sound_button_size)
            self.play_background_sound()
            self.play_birds_sound()
        else:
            self.__is_muted = not self.__is_muted
            self.__mute_unmute_button_img = siw.width(pygame.image.load("src/muted.png").convert_alpha(),
                                                      self.sound_button_size)
            self.stop_background_sound()
            self.stop_birds_sound()

    def toggle_mute_playing_sound(self):
        if self.__is_muted:
            self.__is_muted = not self.__is_muted
            self.__mute_unmute_button_img = siw.width(pygame.image.load("src/unmuted.png").convert_alpha(),
                                                      self.sound_button_size)
            self.play_background_sound("src/sounds/playing.ogg")
        else:
            self.__is_muted = not self.__is_muted
            self.__mute_unmute_button_img = siw.width(pygame.image.load("src/muted.png").convert_alpha(),
                                                      self.sound_button_size)
            self.stop_background_sound()

    def play_typing_first_letter_sound(self):
        if not self.__is_muted:
            pygame.mixer.Channel(4).play(pygame.mixer.Sound("src/sounds/start_letter.ogg"))

    def play_typing_last_letter_sound(self):
        if not self.__is_muted:
            pygame.mixer.Channel(4).play(pygame.mixer.Sound("src/sounds/last_letter.ogg"))

    def play_typing_wrong_sound(self):
        if not self.__is_muted:
            pygame.mixer.Channel(4).play(pygame.mixer.Sound("src/sounds/typed_wrong.ogg"))

    def get_sound_button_img(self):
        return self.__mute_unmute_button_img

    def start_thread(self, target):
        self.threads = threading.Thread(target=target)
        self.threads.start()

    # character
    def get_characters(self):
        return self.__character_seq_list

    def get_small_characters(self):
        return self.__small_character_seq_list

    def set_selected_character_index(self, value):
        self.__selected_character_index = value

    def get_selected_character_index(self):
        return self.__selected_character_index
