import pygame.image

from enter_name import EnterNameState
from utils import scale_img_width as siw


class SelectNumLevel:
    def __init__(self, singleton):
        self.singleton = singleton
        self.next_state = None
        self.clicked_play_button = False

        # background
        self.back_img = pygame.image.load('media/menu/back.jpg').convert()
        self.back_img = pygame.transform.scale(self.back_img, self.singleton.get_screen_size())

        # game text logo
        self.logo_img = siw.scale_img_width(pygame.image.load('media/menu/logo.png').convert_alpha(), 1000)

        self.animation_speed = 15

        # animate logo
        self.logo_pos_y = -300

        # play button
        self.play_button_img = siw.scale_img_width(pygame.image.load('media/menu/play_button.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.play_button_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.play_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.play_button_img.get_height():
                self.clicked_play_button = True

    def update(self):
        if self.logo_pos_y < 50 and not self.clicked_play_button:
            self.logo_pos_y += self.animation_speed
        elif self.logo_pos_y >= -300 and self.clicked_play_button:
            self.logo_pos_y -= self.animation_speed

        if self.button_pos_y > 500 and not self.clicked_play_button:
            self.button_pos_y -= self.animation_speed
        elif self.button_pos_y <= 800 and self.clicked_play_button:
            self.button_pos_y += self.animation_speed

        if self.clicked_play_button and self.logo_pos_y <= -300:
            self.next_state = EnterNameState(self.singleton)

    def draw(self):
        self.singleton.get_screen().blit(self.back_img, (0, 0))
        self.singleton.get_screen().blit(self.logo_img,
                         ((self.singleton.get_screen_size()[0] / 2) - (self.logo_img.get_width() / 2), self.logo_pos_y))
        self.singleton.get_screen().blit(self.play_button_img,
                         (self.button_pos_x, self.button_pos_y))
