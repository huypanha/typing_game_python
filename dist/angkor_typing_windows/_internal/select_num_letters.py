import pygame

from utils import scale_img as siw
from choose_character import ChooseCharacterState


class SelectNumLetters:
    next_state = None
    clicked_play_button = None

    def __init__(self, singleton):
        self.singleton = singleton

        # title
        self.title_img = siw.width(
            pygame.image.load('src/select_letters/select_letter_title.png').convert_alpha(), 800)

        # letters button
        self.btn3_letters = siw.width(
            pygame.image.load('src/select_letters/3_letters.png').convert_alpha(), 300)
        self.btn4_letters = siw.width(
            pygame.image.load('src/select_letters/4_letters.png').convert_alpha(), 300)
        self.btn5_letters = siw.width(
            pygame.image.load('src/select_letters/5_letters.png').convert_alpha(), 300)
        self.btn6_letters = siw.width(
            pygame.image.load('src/select_letters/6_letters.png').convert_alpha(), 300)

        self.change_select_button(self.singleton.get_num_letters())

        # animate
        self.row1_btn_pos_y = -350
        self.row2_btn_pos_y = -300
        self.title_img_pos_y = -200

        # play button
        self.play_btn_img = siw.width(
            pygame.image.load('src/play_button.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.play_btn_img.get_width() / 2)
        self.left_pos_x = (self.singleton.get_screen_size()[0] / 2) - 350
        self.right_pos_x = (self.singleton.get_screen_size()[0] / 2) + 50

        # animate button
        self.button_pos_y = 800

    def handle_events(self, event):
        # handle click button
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.play_btn_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.play_btn_img.get_height():
                self.clicked_play_button = True
                self.singleton.play_click_button()

            # handle click for 3 letters
            if self.left_pos_x <= event.pos[0] <= self.left_pos_x + self.btn3_letters.get_width() and \
                    self.row1_btn_pos_y <= event.pos[1] <= self.row1_btn_pos_y + self.btn3_letters.get_height():
                self.change_select_button(3)
                self.singleton.play_click_button()

            # handle click for 4 letters
            if self.right_pos_x <= event.pos[0] <= self.right_pos_x + self.btn4_letters.get_width() and \
                    self.row1_btn_pos_y <= event.pos[1] <= self.row1_btn_pos_y + self.btn4_letters.get_height():
                self.change_select_button(4)
                self.singleton.play_click_button()

            # handle click for 5 letters
            if self.left_pos_x <= event.pos[0] <= self.left_pos_x + self.btn5_letters.get_width() and \
                    self.row2_btn_pos_y <= event.pos[1] <= self.row2_btn_pos_y + self.btn5_letters.get_height():
                self.change_select_button(5)
                self.singleton.play_click_button()

            # handle click for 6 letters
            if self.right_pos_x <= event.pos[0] <= self.right_pos_x + self.btn6_letters.get_width() and \
                    self.row2_btn_pos_y <= event.pos[1] <= self.row2_btn_pos_y + self.btn6_letters.get_height():
                self.change_select_button(6)
                self.singleton.play_click_button()

    def change_select_button(self, new_number):
        # change old selected button to normal state
        if self.singleton.get_num_letters() == 3:
            self.btn3_letters = siw.width(
                pygame.image.load('src/select_letters/3_letters.png').convert_alpha(), 300)
        elif self.singleton.get_num_letters() == 4:
            self.btn4_letters = siw.width(
                pygame.image.load('src/select_letters/4_letters.png').convert_alpha(), 300)
        elif self.singleton.get_num_letters() == 5:
            self.btn5_letters = siw.width(
                pygame.image.load('src/select_letters/5_letters.png').convert_alpha(), 300)
        elif self.singleton.get_num_letters() == 6:
            self.btn6_letters = siw.width(
                pygame.image.load('src/select_letters/6_letters.png').convert_alpha(), 300)

        # change new selected button to selected state
        if new_number == 3:
            self.btn3_letters = siw.width(
                pygame.image.load('src/select_letters/3_letters_selected.png').convert_alpha(), 300)
        elif new_number == 4:
            self.btn4_letters = siw.width(
                pygame.image.load('src/select_letters/4_letters_selected.png').convert_alpha(), 300)
        elif new_number == 5:
            self.btn5_letters = siw.width(
                pygame.image.load('src/select_letters/5_letters_selected.png').convert_alpha(), 300)
        elif new_number == 6:
            self.btn6_letters = siw.width(
                pygame.image.load('src/select_letters/6_letters_selected.png').convert_alpha(), 300)

        # update new selected letter number
        self.singleton.set_num_letters(new_number)

    def update(self):
        # animate title
        if self.title_img_pos_y < 50 and not self.clicked_play_button:
            self.title_img_pos_y += 10
        elif self.title_img_pos_y >= -200 and self.clicked_play_button:
            self.title_img_pos_y -= 10

        # animate letter button
        if self.row1_btn_pos_y < 200 and not self.clicked_play_button:
            self.row1_btn_pos_y += 20
        elif self.row1_btn_pos_y >= -350 and self.clicked_play_button:
            self.row1_btn_pos_y -= 20

        # animate letter button row 2
        if self.row2_btn_pos_y < 350 and not self.clicked_play_button:
            self.row2_btn_pos_y += 20
        elif self.row2_btn_pos_y >= -250 and self.clicked_play_button:
            self.row2_btn_pos_y -= 20
            if self.clicked_play_button and self.row2_btn_pos_y <= -250:
                self.next_state = ChooseCharacterState(self.singleton)

        # animate button submit
        if self.button_pos_y > 500 and not self.clicked_play_button:
            self.button_pos_y -= 10
        elif self.button_pos_y <= 800 and self.clicked_play_button:
            self.button_pos_y += 10

    def draw(self):
        self.singleton.get_screen().blit(self.singleton.default_back_img, (0, 0))
        self.singleton.get_screen().blit(self.title_img,
                                         ((self.singleton.get_screen_size()[0] / 2) - (
                                                 self.title_img.get_width() / 2), self.title_img_pos_y))

        # draw letter button
        self.singleton.get_screen().blit(self.btn3_letters, (self.left_pos_x, self.row1_btn_pos_y))
        self.singleton.get_screen().blit(self.btn4_letters, (self.right_pos_x, self.row1_btn_pos_y))
        self.singleton.get_screen().blit(self.btn5_letters, (self.left_pos_x, self.row2_btn_pos_y))
        self.singleton.get_screen().blit(self.btn6_letters, (self.right_pos_x, self.row2_btn_pos_y))

        self.singleton.get_screen().blit(self.play_btn_img,
                                         (self.button_pos_x, self.button_pos_y))
