import datetime

import pygame.image

from utils.scale_img_width import scale_img_width as siw
from utils.scale_img_height import scale_img_height as sih


class PlayState:
    def __init__(self, singleton):
        self.singleton = singleton
        self.next_state = None
        self.clicked_play_button = False
        self.sky_mov = 5
        self.timer_text = None
        self.pos_text = None

        # background
        self.sky_back_img = sih(pygame.image.load('media/game/sky.png').convert(),
                                500)

        # load road
        self.road = sih(pygame.image.load('media/game/road.png').convert_alpha(), 700)
        self.current_mov = 10
        self.road_width = 11700

        self.timer_pos_back_img = siw(pygame.image.load('media/game/timer_pos.png').convert_alpha(),
                                      self.singleton.get_screen_size()[0])

        # letter box
        if singleton.get_num_letters() == 3:
            self.letter_box = sih(pygame.image.load('media/game/3_letters_box.png').convert_alpha(), 100)
        elif singleton.get_num_letters() == 4:
            self.letter_box = sih(pygame.image.load('media/game/4_letters_box.png').convert_alpha(), 100)
        elif singleton.get_num_letters() == 5:
            self.letter_box = sih(pygame.image.load('media/game/5_letters_box.png').convert_alpha(), 100)
        elif singleton.get_num_letters() == 6:
            self.letter_box = sih(pygame.image.load('media/game/6_letters_box.png').convert_alpha(), 100)

        # text
        self.font = pygame.font.Font('fonts/LarkeNeueBold.ttf', 30)

        # pos
        self.start_pos = self.singleton.get_screen_size()[0] * .25
        self.end_pos = self.singleton.get_screen_size()[0] * .75

        singleton.set_game_start_time(datetime.datetime.now())

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            # if self.button_pos_x <= event.pos[0] <= self.button_pos_x + self.play_button_img.get_width() and \
            #         self.button_pos_y <= event.pos[1] <= self.button_pos_y + self.play_button_img.get_height():
            #     self.clicked_play_button = True
            self.singleton.play_click_button()

    def update(self):
        # move background
        if self.current_mov >= -self.road_width:
            self.current_mov -= 5
            self.sky_mov += .5

        # create timer text
        time_dif = datetime.datetime.now() - self.singleton.get_game_start_time()
        time_dif = datetime.datetime(1, 1, 1) + time_dif
        self.timer_text = self.font.render("{}".format(time_dif.strftime("%M:%S")), True, (255, 255, 255))

        # create pos text
        self.pos_text = self.font.render("1/2", True, (255, 255, 255))

    def draw(self):
        # draw sky
        for x in range(10):
            self.singleton.get_screen().blit(self.sky_back_img,
                                             (x * self.sky_back_img.get_width() - self.sky_mov * 5, -70))

        self.singleton.get_screen().blit(self.road, (self.current_mov, 20))
        self.singleton.get_screen().blit(self.timer_pos_back_img, (0, 0))
        self.singleton.get_screen().blit(self.letter_box, ((self.singleton.get_screen_size()[0] / 2) -
                                                           self.letter_box.get_width() / 2,
                                                           self.singleton.get_screen_size()[1] -
                                                           (self.letter_box.get_height())))

        # render text
        self.singleton.get_screen().blit(self.timer_text, (70, 45))
        self.singleton.get_screen().blit(self.pos_text, (self.singleton.get_screen_size()[0] - 90, 45))

        # draw position
        # start pos = self.singleton.get_screen_size()[0] * .25 = 320
        # end pos = self.singleton.get_screen_size()[0] * .75 = 960

        # % = ((current - start) * 100) / (current - start)
        road_pos_percent = (self.current_mov * 100) / -self.road_width
        # current point pos = start + (% * (end - start))
        pygame.draw.circle(self.singleton.get_screen(), (255, 0, 0),
                           (self.singleton.get_screen_size()[0] * .25, 55), 8)
        pygame.draw.circle(self.singleton.get_screen(), (0, 255, 0),
                           (self.start_pos + ((road_pos_percent * (self.end_pos - self.start_pos)) / 100), 55), 8)
