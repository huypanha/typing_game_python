import pygame

import scale_img_width as siw


class ChooseCharacterState:
    next_state = None
    clicked_submit_button = None
    selected_index = 0

    def __init__(self, singleton):
        self.singleton = singleton

        # background
        self.back_img = pygame.image.load('media/menu/back.jpg').convert()
        self.back_img = pygame.transform.scale(self.back_img, self.singleton.get_screen_size())

        # get name background
        self.get_name_back_img = siw.scale_img_width(
            pygame.image.load('media/choose_character/selecting_back.png').convert_alpha(), 500)

        # animate get name background
        self.get_name_back_y = -450

        # play button
        self.submit_button_img = siw.scale_img_width(
            pygame.image.load('media/enter_name/button_submit.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.submit_button_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

    def handle_events(self, event):
        # handle click button
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.submit_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.submit_button_img.get_height():
                self.clicked_submit_button = True

    def update(self):
        if self.get_name_back_y < 0 and not self.clicked_submit_button:
            self.get_name_back_y += 15
        elif self.get_name_back_y >= -450 and self.clicked_submit_button:
            self.get_name_back_y -= 15

        if self.button_pos_y > 500 and not self.clicked_submit_button:
            self.button_pos_y -= 15
        elif self.button_pos_y <= 800 and self.clicked_submit_button:
            self.button_pos_y += 15

        if self.clicked_submit_button and self.get_name_back_y <= -500:
            pass
            # self.next_state = EnterNameState(self.screen, self.win_width, self.win_height)

    def draw(self):
        self.singleton.get_screen().blit(self.back_img, (0, 0))
        self.singleton.get_screen().blit(self.get_name_back_img,
                                         ((self.singleton.get_screen_size()[0] / 2) - (
                                                 self.get_name_back_img.get_width() / 2),
                                          self.get_name_back_y))

        self.singleton.get_screen().blit(self.submit_button_img,
                                         (self.button_pos_x, self.button_pos_y))
