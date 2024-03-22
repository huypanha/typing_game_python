import pygame.image

from utils import scale_img_width as siw
from utils import scale_img_height as sih


class PlayState:
    def __init__(self, singleton):
        self.singleton = singleton
        self.next_state = None
        self.clicked_play_button = False
        self.sky_mov = 5

        # background
        self.sky_back_img = sih.scale_img_height(pygame.image.load('media/game/sky.png').convert(),
                                                 500)

        # game text logo
        self.logo_img = siw.scale_img_width(pygame.image.load('media/logo.png').convert_alpha(), 1000)

        self.animation_speed = 15

        # animate logo
        self.logo_pos_y = -300

        # play button
        self.play_button_img = siw.scale_img_width(pygame.image.load('media/play_button.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.play_button_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

        # load road
        self.road = sih.scale_img_height(pygame.image.load('media/game/road.png').convert_alpha(), 700)
        self.back_mov = 10

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.play_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.play_button_img.get_height():
                self.clicked_play_button = True
                self.singleton.play_click_button()

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
            self.next_state = PlayState(self.singleton)

        if self.back_mov >= -11700:
            self.back_mov -= 5
            self.sky_mov += .5

    def draw(self):

        # draw sky
        for x in range(10):
            self.singleton.get_screen().blit(self.sky_back_img,
                                             (x * self.sky_back_img.get_width() - self.sky_mov * 5, -70))

        self.singleton.get_screen().blit(self.road, (self.back_mov, 20))
