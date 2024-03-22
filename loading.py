import pygame.image

from utils import scale_img_width as siw
from enter_name import EnterNameState


class LoadingState:
    def __init__(self, singleton):
        self.singleton = singleton
        self.next_state = None
        self.coefficient_progress = 0
        self.load_completed = False
        self.clicked_play_button = False

        # game text logo
        self.logo_img = siw.scale_img_width(pygame.image.load('media/logo.png').convert_alpha(), 1000)

        # animate logo
        self.logo_pos_y = 50

        # play button
        self.play_button_img = siw.scale_img_width(pygame.image.load('media/play_button.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.play_button_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

    def load_images(self):
        for i in range(120):
            self.singleton.get_character1().append(siw.scale_img_width(pygame.image.load(
                'media/characters/Monkey/Comp 1_{}.png'.format(str(i).rjust(5, "0"))).convert_alpha(), 1200))
            self.coefficient_progress = i / 240

        for i in range(120):
            self.singleton.get_character2().append(siw.scale_img_width(pygame.image.load(
                'media/characters/Rabbit/Comp 2_{}.png'.format(str(i).rjust(5, "0"))).convert_alpha(), 1200))
            self.coefficient_progress = (i + 120) / 240

            # when reached to the last image
            if i >= 119:
                self.load_completed = True

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.play_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.play_button_img.get_height():
                self.clicked_play_button = True
                self.singleton.play_click_button()

    def update(self):
        if self.load_completed:
            # animate logo
            if self.logo_pos_y >= -300 and self.clicked_play_button:
                self.logo_pos_y -= 15

            # animate button
            if self.button_pos_y > 500 and not self.clicked_play_button:
                self.button_pos_y -= 15
            elif self.button_pos_y <= 800 and self.clicked_play_button:
                self.button_pos_y += 15
                if self.clicked_play_button and self.button_pos_y >= 800:
                    self.next_state = EnterNameState(self.singleton)

    def draw(self):
        self.singleton.get_screen().blit(self.singleton.default_back_img, (0, 0))
        self.singleton.get_screen().blit(self.logo_img, ((self.singleton.get_screen_size()[0] / 2)
                                                         - (self.logo_img.get_width() / 2), self.logo_pos_y))

        if self.load_completed:
            # Draw play button
            self.singleton.get_screen().blit(self.play_button_img,
                                             (self.button_pos_x, self.button_pos_y))
        else:
            # Draw progress bar
            pygame.draw.rect(self.singleton.get_screen(), "orange",
                             (200, 500, self.singleton.get_screen_size()[0] - 400, 30), 3, border_radius=50)
            pygame.draw.rect(self.singleton.get_screen(), "#9ade00",
                             (204, 504, (self.singleton.get_screen_size()[0] - 406) * self.coefficient_progress, 23),
                             border_radius=50)
