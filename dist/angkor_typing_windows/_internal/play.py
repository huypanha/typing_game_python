import datetime
import pygame.image
import random as rnd

import select_num_letters
from utils.scale_img import width as siw, height as sih


class PlayState:
    def __init__(self, singleton):
        self.singleton = singleton
        self.next_state = None
        self.clicked_play_button = False
        self.sky_mov = 0
        self.timer_text = None
        self.pos_text = None
        self.time_img = None

        # background
        self.sky_back_img = sih(pygame.image.load('src/play/sky.png').convert(), 500)

        # load road
        self.road = sih(pygame.image.load('src/play/road.png').convert_alpha(), 700)
        self.current_mov = 0
        self.road_width = 11700

        self.timer_pos_back_img = siw(pygame.image.load('src/play/timer_pos.png').convert_alpha(),
                                      self.singleton.get_screen_size()[0])

        # letter box
        if singleton.get_num_letters() == 3:
            self.letter_box = sih(pygame.image.load('src/letter_box/normal/3letters/1.png').convert_alpha(), 100)
            with open("words/3letters.txt") as words:
                self.all_words = words.readlines()
            self.first_letter_pos = (singleton.get_screen_size()[0] / 2) - 80
        elif singleton.get_num_letters() == 4:
            self.letter_box = sih(pygame.image.load('src/letter_box/normal/4letters/1.png').convert_alpha(), 100)
            with open("words/4letters.txt") as words:
                self.all_words = words.readlines()
            self.first_letter_pos = (singleton.get_screen_size()[0] / 2) - 105
        elif singleton.get_num_letters() == 5:
            self.letter_box = sih(pygame.image.load('src/letter_box/normal/5letters/1.png').convert_alpha(), 100)
            with open("words/5letters.txt") as words:
                self.all_words = words.readlines()
            self.first_letter_pos = (singleton.get_screen_size()[0] / 2) - 135
        elif singleton.get_num_letters() == 6:
            self.letter_box = sih(pygame.image.load('src/letter_box/normal/6letters/1.png').convert_alpha(), 100)
            with open("words/6letters.txt") as words:
                self.all_words = words.readlines()
            self.first_letter_pos = (singleton.get_screen_size()[0] / 2) - 160

        # text
        self.font = pygame.font.Font('fonts/Impacted.ttf', 30)
        self.typing_letters_text_surface = []
        self.typing_letter_pos_x = self.first_letter_pos
        self.word_chars = []
        self.get_letters()

        # pos
        self.start_pos = self.singleton.get_screen_size()[0] * .25
        self.end_pos = self.singleton.get_screen_size()[0] * .75

        self.first_opened_time = datetime.datetime.now()

        # use for play sound when changed time img
        self.old_time_img_num = 0

        # restart button
        self.restart_btn_img = siw(pygame.image.load("src/play/restart_button.png").convert_alpha(),
                                   singleton.sound_button_size)
        self.restart_btn_pos_x = 20
        self.restart_btn_pos_y = (singleton.get_screen_size()[1] - (singleton.get_sound_button_img().get_width() + 20))

        # typing
        self.current_typing_letter_index = 0
        # store all typed words
        self.typed_words = []
        # store all typed current word letters
        self.typed_letters = []

    def get_letters(self):
        # random new word
        self.word_chars = self.all_words[rnd.randrange(len(self.all_words))].upper()
        # remove new random word to avoid typing the same word in one round
        self.all_words.remove(self.word_chars.lower())
        # reset position of letters for typing at the bottom
        self.typing_letter_pos_x = self.first_letter_pos
        # reset typed letters
        self.typed_letters = []
        self.typing_letters_text_surface = []
        self.current_typing_letter_index = 0

    def get_text_surface(self):
        # clear old rendered surface
        self.typing_letters_text_surface = []
        # create typing words text
        for t in range(self.singleton.get_num_letters()):
            # change the text color when it has a background other than white
            if t == self.current_typing_letter_index:
                self.typing_letters_text_surface.append(self.font.render(self.word_chars[t], True, "white"))
            else:
                self.typing_letters_text_surface.append(self.font.render(self.word_chars[t], True, "black"))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if (self.restart_btn_pos_x <= event.pos[0] <= self.restart_btn_pos_x + self.singleton.sound_button_size
                    and self.restart_btn_pos_y <= event.pos[1] <= self.restart_btn_pos_y +
                    self.singleton.sound_button_size):
                self.singleton.play_click_button()
                # stop playing background sound
                self.singleton.stop_background_sound()
                # start play normal background sound and birth sound
                self.singleton.play_background_sound()
                self.singleton.play_birds_sound()
                self.next_state = select_num_letters.SelectNumLetters(self.singleton)

        # get user typing
        if event.type == pygame.KEYDOWN:
            # accept typing after wait 3 seconds completed
            if 0 > self.current_mov > -self.road_width:
                if self.word_chars[self.current_typing_letter_index].lower() == str(event.unicode).lower():
                    # save typed letter
                    self.typed_letters.append(event.unicode)
                    if len(self.typed_letters) == self.singleton.get_num_letters():
                        self.typed_words.append("".join(self.typed_letters))
                        self.get_letters()
                    else:
                        self.current_typing_letter_index += 1

                    self.letter_box = sih(pygame.image.load(
                        f'src/letter_box/normal/{self.singleton.get_num_letters()}letters/'
                        f'{self.current_typing_letter_index + 1}.png').convert_alpha(), 100)
                else:
                    self.letter_box = sih(pygame.image.load(
                        f'src/letter_box/incorrect/{self.singleton.get_num_letters()}letters/'
                        f'{self.current_typing_letter_index + 1}.png').convert_alpha(), 100)

                # re-render text surface
                self.get_text_surface()

    def update(self):
        # wait 3 seconds
        total_sec = (datetime.datetime.now() - self.first_opened_time).total_seconds()
        if total_sec <= 4:
            new_time_num = 0

            if total_sec <= 1:
                self.time_img = sih(pygame.image.load('src/play/3.png').convert_alpha(), 200)
                new_time_num = 1
            elif total_sec <= 2:
                self.time_img = sih(pygame.image.load('src/play/2.png').convert_alpha(), 200)
                new_time_num = 2
            elif total_sec <= 3:
                self.time_img = sih(pygame.image.load('src/play/1.png').convert_alpha(), 200)
                new_time_num = 3
            elif total_sec <= 4:
                self.time_img = sih(pygame.image.load('src/play/GO.png').convert_alpha(), 200)
                new_time_num = 4

            # play sound
            if self.old_time_img_num != new_time_num:
                if new_time_num == 4:
                    self.singleton.play_countdown_end_sound()
                else:
                    self.singleton.play_countdown_sound()
                self.old_time_img_num = new_time_num

            self.timer_text = self.font.render("00:00", True, (255, 255, 255))

            # set started time
            self.singleton.set_game_start_time(datetime.datetime.now())
        else:
            # clear time text
            self.time_img = None

            # play background sound
            self.singleton.play_background_sound("src/sounds/playing.ogg")

            # move background
            if self.current_mov >= -self.road_width:
                self.current_mov -= 5
                self.sky_mov -= .5

            # create timer text
            time_dif = datetime.datetime.now() - self.singleton.get_game_start_time()
            time_dif = datetime.datetime(1, 1, 1) + time_dif
            self.timer_text = self.font.render("{}".format(time_dif.strftime("%M:%S")), True, (255, 255, 255))

        # create pos text
        self.pos_text = self.font.render("1/2", True, (255, 255, 255))

        # render text surface
        self.get_text_surface()

    def draw(self):
        # draw sky
        for x in range(3):
            self.singleton.get_screen().blit(self.sky_back_img,
                                             (x * self.sky_back_img.get_width() + self.sky_mov * 5, -70))

        self.singleton.get_screen().blit(self.road, (self.current_mov, 20))
        self.singleton.get_screen().blit(self.timer_pos_back_img, (0, 0))

        # render text
        self.singleton.get_screen().blit(self.timer_text, (70, 40))
        self.singleton.get_screen().blit(self.pos_text, (self.singleton.get_screen_size()[0] - 90, 40))

        # draw position
        # start pos = self.singleton.get_screen_size()[0] * .25 = 320
        # end pos = self.singleton.get_screen_size()[0] * .75 = 960

        # % = ((current - start) * 100) / (current - start)
        road_pos_percent = (self.current_mov * 100) / -self.road_width
        # current point pos = start + (% * (end - start))
        pygame.draw.circle(self.singleton.get_screen(), (255, 0, 0), (self.singleton.get_screen_size()[0] * .25, 55), 8)
        pygame.draw.circle(self.singleton.get_screen(), (0, 255, 0),
                           (self.start_pos + ((road_pos_percent * (self.end_pos - self.start_pos)) / 100), 55), 8)

        # draw word to typing
        self.singleton.get_screen().blit(self.letter_box, ((self.singleton.get_screen_size()[0] / 2) -
                                                           self.letter_box.get_width() / 2,
                                                           self.singleton.get_screen_size()[1] -
                                                           (self.letter_box.get_height())))
        self.typing_letter_pos_x = self.first_letter_pos
        for t in range(self.singleton.get_num_letters()):
            x = (self.typing_letter_pos_x + 22.5) - (self.typing_letters_text_surface[t].get_width() / 2)
            self.singleton.get_screen().blit(self.typing_letters_text_surface[t],
                                             (x, self.singleton.get_screen_size()[1] -
                                              (self.typing_letters_text_surface[t].get_height() * 2)))
            self.typing_letter_pos_x += 55

        # restart button
        self.singleton.get_screen().blit(self.restart_btn_img, (self.restart_btn_pos_x, self.restart_btn_pos_y))

        if self.time_img is not None:
            self.singleton.get_screen().blit(self.time_img, ((self.singleton.get_screen_size()[0] / 2) -
                                                             (self.time_img.get_width() / 2),
                                                             (self.singleton.get_screen_size()[1] / 2) -
                                                             (self.time_img.get_height() * .20)))
