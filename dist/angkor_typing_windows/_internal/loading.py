import pygame.image

from utils import scale_img as siw
from enter_name import EnterNameState


class LoadingState:
    def __init__(self, singleton):
        self.singleton = singleton
        self.next_state = None
        self.coefficient_progress = 0
        self.load_completed = False
        self.clicked_play_button = False
        self.number_of_jobs = 480

        # play text logo
        self.logo_img = siw.width(pygame.image.load('src/logo.png').convert_alpha(), 1000)

        # animate logo
        self.logo_pos_y = 50

        # play button
        self.play_button_normal_img = siw.width(pygame.image.load('src/play_button.png').convert_alpha(), 150)
        self.play_button_img = self.play_button_normal_img
        self.play_button_hover_img = siw.width(pygame.image.load('src/play_button_hover.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.singleton.get_screen_size()[0] / 2) - (self.play_button_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

        # result characters
        self.result_player_character = None
        self.result_other_player_character = None

        # text
        self.font = pygame.font.Font('fonts/BigSpace.ttf', 40)
        self.text_surface = self.font.render("LOADING...", True, "#9ade00")

        # loading text
        self.loading_text_img = pygame.image.load("src/loading_text.png")

    def load_images(self):
        for i in range(120):
            if len(self.singleton.get_characters()) == 0:
                self.singleton.get_characters().append([])
            self.singleton.get_characters()[0].append(siw.width(pygame.image.load(
                'src/characters/Monkey/Comp 1_{}.png'.format(str(i).rjust(5, "0"))).convert_alpha(), 350))
            self.coefficient_progress = i / self.number_of_jobs

        for i in range(120):
            if len(self.singleton.get_characters()) == 1:
                self.singleton.get_characters().append([])
            self.singleton.get_characters()[1].append(siw.width(pygame.image.load(
                'src/characters/Rabbit/Comp 2_{}.png'.format(str(i).rjust(5, "0"))).convert_alpha(), 350))
            self.coefficient_progress = (i + 120) / self.number_of_jobs

        # get result character
        for i in range(120):
            if len(self.singleton.get_small_characters()) == 0:
                self.singleton.get_small_characters().append([])
            self.singleton.get_small_characters()[0].append(siw.width(pygame.image.load(
                'src/characters/Monkey/Comp 1_{}.png'.format(str(i).rjust(5, "0"))).convert_alpha(), 200))
            self.coefficient_progress = (i + 240) / self.number_of_jobs

        # get result character
        for i in range(120):
            if len(self.singleton.get_small_characters()) == 1:
                self.singleton.get_small_characters().append([])
            self.singleton.get_small_characters()[1].append(siw.width(pygame.image.load(
                'src/characters/Rabbit/Comp 2_{}.png'.format(str(i).rjust(5, "0"))).convert_alpha(), 200))
            self.coefficient_progress = (i + 360) / self.number_of_jobs

            # when reached to the last image
            if i >= 119:
                self.load_completed = True

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.play_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.play_button_img.get_height():
                self.clicked_play_button = True
                self.singleton.play_click_button()

        if event.type == pygame.MOUSEMOTION:
            if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.play_button_img.get_width() and \
                    self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.play_button_img.get_height():
                self.play_button_img = self.play_button_hover_img
            else:
                self.play_button_img = self.play_button_normal_img

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
            # Draw loading text
            self.singleton.get_screen().blit(self.loading_text_img, ((self.singleton.get_screen_size()[0] / 2) -
                                                                 (self.loading_text_img.get_width() / 2), 440))

            # Draw progress bar
            pygame.draw.rect(self.singleton.get_screen(), "orange",
                             (200, 500, self.singleton.get_screen_size()[0] - 400, 30), 3, border_radius=50)
            pygame.draw.rect(self.singleton.get_screen(), "#9ade00",
                             (204, 504, (self.singleton.get_screen_size()[0] - 406) * self.coefficient_progress, 23),
                             border_radius=50)
