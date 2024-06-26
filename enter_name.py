import pygame

import select_num_letters
from utils import scale_img as siw


class EnterNameState:
    next_state = None
    clicked_submit_button = None
    is_first_enter_name = True
    text_surface = None

    def __init__(self, singleton):
        self.singleton = singleton
        self.get_name = 'Enter your name'
        self.get_name_result = 'Enter your name'
        self.font = pygame.font.Font('fonts/Jacenta.otf', 35)

        # get name background
        self.get_name_back_img = siw.width(
            pygame.image.load('src/enter_name/enter_name_back.png').convert_alpha(), 500)

        # animate get name background
        self.get_name_back_y = -450

        # submit button
        self.submit_button_normal_img = siw.width(pygame.image.load('src/submit_button.png').convert_alpha(), 150)
        self.submit_button_img = self.submit_button_normal_img
        self.submit_button_hover_img = siw.width(pygame.image.load('src/submit_button_hover.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.submit_button_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if self.is_first_enter_name:
                self.get_name_result = ''
                self.is_first_enter_name = False
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                if self.get_name_result != 'Enter your name' and len(self.get_name_result) >= 3:
                    self.clicked_submit_button = True
                    self.singleton.play_click_button()
            elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                self.get_name_result = self.get_name_result[:-1]
            else:
                if len(self.get_name_result) <= 11:
                    self.get_name_result += event.unicode

            if len(self.get_name_result) > 22:
                self.get_name = self.get_name_result[len(self.get_name_result) - 22:]
            else:
                self.get_name = self.get_name_result

        # handle click button
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.submit_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.submit_button_img.get_height():
                if self.get_name_result != 'Enter your name' and len(self.get_name_result) >= 3:
                    self.clicked_submit_button = True
                self.singleton.play_click_button()

        if event.type == pygame.MOUSEMOTION:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.submit_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.submit_button_img.get_height():
                self.submit_button_img = self.submit_button_hover_img
            else:
                self.submit_button_img = self.submit_button_normal_img

    def update(self):
        if self.get_name_back_y < 0 and not self.clicked_submit_button:
            self.get_name_back_y += 15
        elif self.get_name_back_y >= -500 and self.clicked_submit_button:
            self.get_name_back_y -= 15
            if self.clicked_submit_button and self.get_name_back_y <= -500:
                self.singleton.set_user_name(self.get_name_result)
                self.next_state = select_num_letters.SelectNumLetters(self.singleton)

        self.text_surface = self.font.render(self.get_name, True, (255, 255, 255))

        if self.button_pos_y > 500 and not self.clicked_submit_button:
            self.button_pos_y -= 15
        elif self.button_pos_y <= 800 and self.clicked_submit_button:
            self.button_pos_y += 15

    def draw(self):
        self.singleton.get_screen().blit(self.singleton.default_back_img, (0, 0))
        self.singleton.get_screen().blit(self.get_name_back_img, ((self.singleton.get_screen_size()[0] / 2) -
                                                                  (self.get_name_back_img.get_width() / 2),
                                                                  self.get_name_back_y))
        # draw text area
        if self.get_name_back_y >= 0:
            self.singleton.get_screen().blit(self.text_surface, ((self.singleton.get_screen_size()[0] / 2) -
                                                                 (self.text_surface.get_width() / 2), 255))

        self.singleton.get_screen().blit(self.submit_button_img, (self.button_pos_x, self.button_pos_y))
