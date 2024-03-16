import pygame

from utils import scale_img_width as siw


class ChooseCharacterState:
    next_state = None
    clicked_submit_button = None
    selected_index = 0

    def __init__(self, singleton):
        self.singleton = singleton

        # background
        self.back_img = pygame.image.load('media/menu/back.jpg').convert()
        self.back_img = pygame.transform.scale(self.back_img, self.singleton.get_screen_size())

        # title
        self.title_text = siw.scale_img_width(
            pygame.image.load('media/choose_character/title_text.png').convert_alpha(), 800)

        # character background
        self.ch_1_back_img = siw.scale_img_width(
            pygame.image.load('media/choose_character/selecting_back.png').convert_alpha(), 450)
        self.ch_2_back_img = siw.scale_img_width(
            pygame.image.load('media/choose_character/back.png').convert_alpha(), 450)

        # character
        self.ch1 = siw.scale_img_width(
            pygame.image.load('media/choose_character/img.jpeg').convert(), 300)
        self.ch2 = siw.scale_img_width(
            pygame.image.load('media/choose_character/img.jpeg').convert(), 300)

        # animate
        self.ch_back_pos_y = -450
        self.title_text_pos_y = -200
        self.ch_pos_y = -350

        # play button
        self.submit_button_img = siw.scale_img_width(
            pygame.image.load('media/enter_name/button_submit.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.submit_button_img.get_width() / 2)
        self.ch1_back_pos_x = (self.singleton.get_screen_size()[0] / 4) - (self.ch_1_back_img.get_width() / 2)
        self.ch2_back_pos_x = (self.singleton.get_screen_size()[0] / 2.5) + (self.ch_2_back_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

    def handle_events(self, event):
        # handle click button
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.submit_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.submit_button_img.get_height():
                self.clicked_submit_button = True

            # handle click for first character
            if self.ch1_back_pos_x <= event.pos[0] <= self.ch1_back_pos_x + self.ch_1_back_img.get_width() and \
                    self.ch_back_pos_y <= event.pos[1] <= self.ch_back_pos_y + self.ch_1_back_img.get_height():
                self.ch_1_back_img = siw.scale_img_width(
                    pygame.image.load('media/choose_character/selecting_back.png').convert_alpha(), 450)
                self.ch_2_back_img = siw.scale_img_width(
                    pygame.image.load('media/choose_character/back.png').convert_alpha(), 450)
                self.selected_index = 0

            # handle click for second character
            if self.ch2_back_pos_x <= event.pos[0] <= self.ch2_back_pos_x + self.ch_2_back_img.get_width() and \
                    self.ch_back_pos_y <= event.pos[1] <= self.ch_back_pos_y + self.ch_2_back_img.get_height():
                self.ch_2_back_img = siw.scale_img_width(
                    pygame.image.load('media/choose_character/selecting_back.png').convert_alpha(), 450)
                self.ch_1_back_img = siw.scale_img_width(
                    pygame.image.load('media/choose_character/back.png').convert_alpha(), 450)
                self.selected_index = 1

    def update(self):
        # animate title
        if self.title_text_pos_y < 50 and not self.clicked_submit_button:
            self.title_text_pos_y += 10
        elif self.title_text_pos_y >= -200 and self.clicked_submit_button:
            self.title_text_pos_y -= 10

        # animate character background
        if self.ch_back_pos_y < 170 and not self.clicked_submit_button:
            self.ch_back_pos_y += 20
        elif self.ch_back_pos_y >= -450 and self.clicked_submit_button:
            self.ch_back_pos_y -= 20
            if self.clicked_submit_button and self.ch_back_pos_y <= -450:
                self.singleton.set_user_name(self.ch_back_pos_y)
                self.next_state = ChooseCharacterState(self.singleton)

        # animate character
        if self.ch_pos_y < 270 and not self.clicked_submit_button:
            self.ch_pos_y += 20
        elif self.ch_pos_y >= -400 and self.clicked_submit_button:
            self.ch_pos_y -= 20

        # animate button submit
        if self.button_pos_y > 600 and not self.clicked_submit_button:
            self.button_pos_y -= 10
        elif self.button_pos_y <= 800 and self.clicked_submit_button:
            self.button_pos_y += 10

    def draw(self):
        self.singleton.get_screen().blit(self.back_img, (0, 0))
        self.singleton.get_screen().blit(self.title_text,
                                         ((self.singleton.get_screen_size()[0] / 2) - (
                                                 self.title_text.get_width() / 2), self.title_text_pos_y))

        # draw character background
        self.singleton.get_screen().blit(self.ch_1_back_img, (self.ch1_back_pos_x, self.ch_back_pos_y))
        self.singleton.get_screen().blit(self.ch_2_back_img, (self.ch2_back_pos_x, self.ch_back_pos_y))

        # draw character
        self.singleton.get_screen().blit(self.ch1, ((self.singleton.get_screen_size()[0] / 4) -
                                                    (self.ch1.get_width() / 2), self.ch_pos_y))
        self.singleton.get_screen().blit(self.ch2, ((self.singleton.get_screen_size()[0] / 1.93) +
                                                    (self.ch2.get_width() / 2), self.ch_pos_y))

        self.singleton.get_screen().blit(self.submit_button_img,
                                         (self.button_pos_x, self.button_pos_y))
