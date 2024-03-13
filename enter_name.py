import pygame

from typing_game import scale_img_width as siw


class EnterNameState:
    def __init__(self, screen, win_width, win_height):
        self.screen = screen
        self.win_width = win_width
        self.win_height = win_height
        self.next_state = None
        self.clicked_submit_button = None
        self.get_name = 'Enter your name'
        self.get_name_result = 'Enter your name'
        self.font = pygame.font.Font('fonts/SubwayCircleDemo.otf', 30)
        self.is_first_enter_name = True
        self.text_surface = None

        # background
        self.back_img = pygame.image.load('media/menu/back.jpg').convert()
        self.back_img = pygame.transform.scale(self.back_img, (self.win_width, self.win_height))

        # get name background
        self.get_name_back_img = siw.scale_img_width(
            pygame.image.load('media/enter_name/enter_name_back.png').convert_alpha(), 500)

        # animate get name background
        self.get_name_back_y = -450

        # play button
        self.submit_button_img = siw.scale_img_width(
            pygame.image.load('media/enter_name/button_submit.png').convert_alpha(), 150)

        # use for handle click event
        self.button_pos_x = (self.win_width / 2) - (self.submit_button_img.get_width() / 2)

        # animate button
        self.button_pos_y = 800

    def handle_events(self, event):
        if event.type == pygame.KEYDOWN:
            if self.is_first_enter_name:
                self.get_name_result = ''
                self.is_first_enter_name = False
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                pass
            elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                self.get_name_result = self.get_name_result[:-1]
            else:
                self.get_name_result += event.unicode

            if len(self.get_name_result) > 22:
                self.get_name = self.get_name_result[len(self.get_name_result) - 22:]
            else:
                self.get_name = self.get_name_result

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

        self.text_surface = self.font.render(self.get_name, True, (255, 255, 255))

        if self.button_pos_y > 500 and not self.clicked_submit_button:
            self.button_pos_y -= 15
        elif self.button_pos_y <= 800 and self.clicked_submit_button:
            self.button_pos_y += 15

        if self.clicked_submit_button and self.get_name_back_y <= -500:
            self.next_state = EnterNameState(self.screen, self.win_width, self.win_height)

    def draw(self):
        self.screen.blit(self.back_img, (0, 0))
        self.screen.blit(self.get_name_back_img,
                         ((self.win_width / 2) - (self.get_name_back_img.get_width() / 2), self.get_name_back_y))
        if self.get_name_back_y >= 0:
            self.screen.blit(self.text_surface, ((self.win_width / 2) - 150, 250))

        self.screen.blit(self.submit_button_img,
                         (self.button_pos_x, self.button_pos_y))
