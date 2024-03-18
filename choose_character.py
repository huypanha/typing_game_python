import pygame

from utils import scale_img_width as siw
from select_num_letters import SelectNumLetters


class ChooseCharacterState:
    next_state = None
    clicked_submit_button = None
    selected_index = 0

    def __init__(self, singleton):
        self.singleton = singleton

        # background
        self.back_img = pygame.image.load('media/back.jpg').convert()
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
        self.ch1_seq = []
        for i in range(120):
            self.ch1_seq.append(siw.scale_img_width(pygame.image.load('media/characters/Monkey/Comp 1_{}.png'
                                                                      .format(str(i).rjust(5, "0"))).convert_alpha(),
                                                    1000))
        self.current_frame_ch1 = 0
        self.ch1 = self.ch1_seq[self.current_frame_ch1]

        self.ch2_seq = []
        for i in range(120):
            self.ch2_seq.append(siw.scale_img_width(pygame.image.load('media/characters/Rabbit/Comp 2_{}.png'
                                                                      .format(str(i).rjust(5, "0"))).convert_alpha(),
                                                    1000))
        self.current_frame_ch2 = 0
        self.ch2 = self.ch2_seq[self.current_frame_ch2]

        # animate
        self.ch_back_pos_y = -450
        self.title_text_pos_y = -200
        self.ch_pos_y = -1000

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
                self.singleton.play_click_button()

            # handle click for first character
            if self.ch1_back_pos_x <= event.pos[0] <= self.ch1_back_pos_x + self.ch_1_back_img.get_width() and \
                    self.ch_back_pos_y <= event.pos[1] <= self.ch_back_pos_y + self.ch_1_back_img.get_height():
                self.ch_1_back_img = siw.scale_img_width(
                    pygame.image.load('media/choose_character/selecting_back.png').convert_alpha(), 450)
                self.ch_2_back_img = siw.scale_img_width(
                    pygame.image.load('media/choose_character/back.png').convert_alpha(), 450)
                self.selected_index = 0
                self.singleton.play_click_button()

            # handle click for second character
            if self.ch2_back_pos_x <= event.pos[0] <= self.ch2_back_pos_x + self.ch_2_back_img.get_width() and \
                    self.ch_back_pos_y <= event.pos[1] <= self.ch_back_pos_y + self.ch_2_back_img.get_height():
                self.ch_2_back_img = siw.scale_img_width(
                    pygame.image.load('media/choose_character/selecting_back.png').convert_alpha(), 450)
                self.ch_1_back_img = siw.scale_img_width(
                    pygame.image.load('media/choose_character/back.png').convert_alpha(), 450)
                self.selected_index = 1
                self.singleton.play_click_button()

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
                if self.selected_index == 0:
                    self.singleton.set_character(self.ch1_seq)
                elif self.selected_index == 1:
                    self.singleton.set_character(self.ch2_seq)
                self.next_state = SelectNumLetters(self.singleton)

        # animate character
        if self.ch_pos_y < 100 and not self.clicked_submit_button:
            self.ch_pos_y += 20
        elif self.ch_pos_y >= -400 and self.clicked_submit_button:
            self.ch_pos_y -= 20

        # animate button submit
        if self.button_pos_y > 600 and not self.clicked_submit_button:
            self.button_pos_y -= 10
        elif self.button_pos_y <= 800 and self.clicked_submit_button:
            self.button_pos_y += 10

        # animate character 1
        self.ch1 = self.ch1_seq[self.current_frame_ch1]
        self.current_frame_ch1 = (self.current_frame_ch1 + 1) % len(self.ch1_seq)

        # animate character 2
        self.ch2 = self.ch2_seq[self.current_frame_ch2]
        self.current_frame_ch2 = (self.current_frame_ch2 + 1) % len(self.ch2_seq)

    def draw(self):
        self.singleton.get_screen().blit(self.back_img, (0, 0))
        self.singleton.get_screen().blit(self.title_text, ((self.singleton.get_screen_size()[0] / 2) - (
                                                 self.title_text.get_width() / 2), self.title_text_pos_y))

        # draw character background
        self.singleton.get_screen().blit(self.ch_1_back_img, (self.ch1_back_pos_x, self.ch_back_pos_y))
        self.singleton.get_screen().blit(self.ch_2_back_img, (self.ch2_back_pos_x, self.ch_back_pos_y))

        # draw character
        self.singleton.get_screen().blit(self.ch1, ((self.singleton.get_screen_size()[0] / 4) -
                                                    (self.ch1.get_width() / 2), self.ch_pos_y))
        self.singleton.get_screen().blit(self.ch2, ((self.singleton.get_screen_size()[0] / 2) - 150, self.ch_pos_y))

        self.singleton.get_screen().blit(self.submit_button_img,
                                         (self.button_pos_x, self.button_pos_y))
