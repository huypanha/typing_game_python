import pygame

import play
import select_num_letters
from utils import scale_img as siw


class ChooseCharacterState:
    next_state = None
    clicked_submit_button = None
    selected_index = 0
    is_back = False

    def __init__(self, singleton):
        self.singleton = singleton

        # title
        self.title_text = siw.width(
            pygame.image.load('src/choose_character/title_text.png').convert_alpha(), 800)

        # character background
        self.ch_1_back_img = siw.width(
            pygame.image.load('src/choose_character/selecting_back.png').convert_alpha(), 450)
        self.ch_2_back_img = siw.width(
            pygame.image.load('src/choose_character/back.png').convert_alpha(), 450)

        # character
        self.current_frame_ch1 = 0
        self.ch1 = self.singleton.get_characters()[0][self.current_frame_ch1]

        self.current_frame_ch2 = 0
        self.ch2 = self.singleton.get_characters()[1][self.current_frame_ch2]

        # animate
        self.ch_back_pos_y = -450
        self.title_text_pos_y = -200
        self.ch_pos_y = -500

        # submit button
        self.submit_button_normal_img = siw.width(pygame.image.load('src/submit_button.png').convert_alpha(), 150)
        self.submit_button_img = self.submit_button_normal_img
        self.submit_button_hover_img = siw.width(pygame.image.load('src/submit_button_hover.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.submit_button_img.get_width() / 2)
        self.ch1_back_pos_x = (self.singleton.get_screen_size()[0] / 4) - (self.ch_1_back_img.get_width() / 2)
        self.ch2_back_pos_x = (self.singleton.get_screen_size()[0] / 2.5) + (self.ch_2_back_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

        # back button
        self.back_btn_img = siw.width(pygame.image.load('src/back_button.png').convert_alpha(),
                                      self.singleton.sound_button_size)
        self.back_btn_pos_x = 20
        self.back_btn_pos_y = (self.singleton.get_screen_size()[1] - 20 - self.back_btn_img.get_height())

    def handle_events(self, event):
        # handle click button
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.submit_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.submit_button_img.get_height():
                self.clicked_submit_button = True
                self.singleton.play_click_button()

            if self.back_btn_pos_x <= event.pos[0] <= self.back_btn_pos_x + self.back_btn_img.get_width() and \
                    self.back_btn_pos_y <= event.pos[1] <= self.back_btn_pos_y + self.back_btn_img.get_height():
                self.clicked_submit_button = True
                self.is_back = True
                self.singleton.play_click_button()

            # handle click for first character
            if self.ch1_back_pos_x <= event.pos[0] <= self.ch1_back_pos_x + self.ch_1_back_img.get_width() and \
                    self.ch_back_pos_y <= event.pos[1] <= self.ch_back_pos_y + self.ch_1_back_img.get_height():
                self.ch_1_back_img = siw.width(
                    pygame.image.load('src/choose_character/selecting_back.png').convert_alpha(), 450)
                self.ch_2_back_img = siw.width(
                    pygame.image.load('src/choose_character/back.png').convert_alpha(), 450)
                self.selected_index = 0
                self.singleton.play_click_button()

            # handle click for second character
            if self.ch2_back_pos_x <= event.pos[0] <= self.ch2_back_pos_x + self.ch_2_back_img.get_width() and \
                    self.ch_back_pos_y <= event.pos[1] <= self.ch_back_pos_y + self.ch_2_back_img.get_height():
                self.ch_2_back_img = siw.width(
                    pygame.image.load('src/choose_character/selecting_back.png').convert_alpha(), 450)
                self.ch_1_back_img = siw.width(
                    pygame.image.load('src/choose_character/back.png').convert_alpha(), 450)
                self.selected_index = 1
                self.singleton.play_click_button()

        if event.type == pygame.MOUSEMOTION:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.submit_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.submit_button_img.get_height():
                self.submit_button_img = self.submit_button_hover_img
            else:
                self.submit_button_img = self.submit_button_normal_img

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
                if self.is_back:
                    self.next_state = select_num_letters.SelectNumLetters(self.singleton)
                else:
                    self.singleton.set_selected_character_index(self.selected_index)
                    self.singleton.stop_background_sound()
                    self.singleton.stop_birds_sound()
                    self.next_state = play.PlayState(self.singleton)

        # animate character
        if self.ch_pos_y < 300 and not self.clicked_submit_button:
            self.ch_pos_y += 20
        elif self.ch_pos_y >= -400 and self.clicked_submit_button:
            self.ch_pos_y -= 20

        # animate button submit
        if self.button_pos_y > 600 and not self.clicked_submit_button:
            self.button_pos_y -= 10
        elif self.button_pos_y <= 800 and self.clicked_submit_button:
            self.button_pos_y += 10

        # animate character 1
        self.ch1 = self.singleton.get_characters()[0][self.current_frame_ch1]
        self.current_frame_ch1 = (self.current_frame_ch1 + 1) % len(self.singleton.get_characters()[0])

        # animate character 2
        self.ch2 = self.singleton.get_characters()[1][self.current_frame_ch2]
        self.current_frame_ch2 = (self.current_frame_ch2 + 1) % len(self.singleton.get_characters()[1])

    def draw(self):
        self.singleton.get_screen().blit(self.singleton.default_back_img, (0, 0))
        self.singleton.get_screen().blit(self.title_text, ((self.singleton.get_screen_size()[0] / 2) - (
                                                 self.title_text.get_width() / 2), self.title_text_pos_y))

        # draw character background
        self.singleton.get_screen().blit(self.ch_1_back_img, (self.ch1_back_pos_x, self.ch_back_pos_y))
        self.singleton.get_screen().blit(self.ch_2_back_img, (self.ch2_back_pos_x, self.ch_back_pos_y))

        # draw character
        self.singleton.get_screen().blit(self.ch1, ((self.singleton.get_screen_size()[0] * .22) -
                                                    (self.ch1.get_width() / 2), self.ch_pos_y))
        self.singleton.get_screen().blit(self.ch2, ((self.singleton.get_screen_size()[0] * .72) -
                                                    (self.ch1.get_width() / 2), self.ch_pos_y))

        # draw submit button
        self.singleton.get_screen().blit(self.submit_button_img,
                                         (self.button_pos_x, self.button_pos_y))

        # draw back button
        self.singleton.get_screen().blit(self.back_btn_img,
                                         (self.back_btn_pos_x, self.back_btn_pos_y))
