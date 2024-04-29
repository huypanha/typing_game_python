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
        self.played_finish_sound = False
        self.other_player_next_typed_duration = 3

        # background
        self.sky_back_img = sih(pygame.image.load('src/play/sky.png').convert(), 500)

        # load road
        self.road = sih(pygame.image.load('src/play/road.png').convert_alpha(), 700)
        self.current_mov = 0
        self.road_width = 11700

        self.timer_pos_back_img = siw(pygame.image.load('src/play/timer_pos.png').convert_alpha(),
                                      self.singleton.get_screen_size()[0])

        # letter box and get all words
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
        self.other_typed_words = []
        self.current_word_is_wrong = False
        self.wrong_words = []
        self.other_wrong_words = []

        # character
        self.player_seq = None
        self.other_player_seq = None
        self.current_player_frame = 0
        self.current_other_player_frame = 0
        if singleton.get_selected_character_index() == 0:
            self.player_seq = singleton.get_characters()[0]
            self.result_player_seq = singleton.get_small_characters()[0]
            self.other_player_seq = singleton.get_characters()[1]
            self.result_other_player_seq = singleton.get_small_characters()[1]
        else:
            self.player_seq = singleton.get_characters()[1]
            self.result_player_seq = singleton.get_small_characters()[1]
            self.other_player_seq = singleton.get_characters()[0]
            self.result_other_player_seq = singleton.get_small_characters()[0]
        self.player = self.player_seq[0]
        self.other_player = self.other_player_seq[0]

        # character name
        self.name_font = pygame.font.Font('fonts/Impacted.ttf', 20)
        self.player_name_back = siw(pygame.image.load("src/play/player_name.png").convert_alpha(), 150)
        self.player_name = self.name_font.render(singleton.get_user_name(), True, (255, 255, 255))
        self.other_player_name_back = siw(pygame.image.load("src/play/other_player_name.png").convert_alpha(), 150)

        # random name
        self.other_player_name_text = None
        with open("words/names.txt") as words:
            all_name = words.readlines()
            self.other_player_name_text = all_name[rnd.randrange(len(all_name))].replace("\n", "")
            self.other_player_name = self.name_font.render(self.other_player_name_text,
                                                           True, (255, 255, 255))

        # character position
        self.player_speed = 3
        self.other_player_speed = 3
        self.player_pos = 50
        self.other_player_pos = 50
        self.other_player_pos_y = 50
        self.last_update_player_speed = datetime.datetime.now()
        self.last_update_other_player_speed = datetime.datetime.now()

        # time taken
        self.player_finish_time = None
        self.other_player_finish_time = None
        self.start_time = None
        self.wait_3s_time = datetime.datetime.now()

        # result
        self.result_back_img = siw(pygame.image.load('src/play/race_results.png').convert_alpha(),
                                   singleton.get_screen_size()[0] - 100)
        self.result_back_img_pos_y = -self.result_back_img.get_height()
        self.time_taken = None
        self.other_time_taken = None
        self.wpm = None
        self.other_wpm = None
        self.result_text_player_pos_y = None
        self.result_text_other_player_pos_y = None
        self.result_player_name_surface = None
        self.result_other_player_name_surface = None
        self.result_player_wpm_surface = None
        self.result_other_player_wpm_surface = None
        self.result_player_accuracy = None
        self.result_other_player_accuracy = None
        self.result_player_accuracy_surface = None
        self.result_other_player_accuracy_surface = None
        self.result_player_time_taken_surface = None
        self.result_other_player_time_taken_surface = None

        # result character position
        self.result_player_pos_y = None
        self.result_other_player_pos_y = None
        self.result_player = self.result_player_seq[0]
        self.result_other_player = self.result_other_player_seq[0]
        self.current_result_player_frame = 0
        self.current_result_other_player_frame = 0

        # result button
        self.result_play_again_btn_normal_img = siw(pygame.image.load('src/play/play_again_btn.png').convert_alpha(), 240)
        self.result_play_again_btn_img = self.result_play_again_btn_normal_img
        self.result_play_again_btn_hover_img = siw(pygame.image.load('src/play/play_again_btn_hover.png').convert_alpha(), 240)
        self.result_main_menu_btn_normal_img = siw(pygame.image.load('src/play/main_menu_btn.png').convert_alpha(), 240)
        self.result_main_menu_btn_img = self.result_main_menu_btn_normal_img
        self.result_main_menu_btn_hover_img = siw(pygame.image.load('src/play/main_menu_btn_hover.png').convert_alpha(), 240)
        self.result_btn_pos_x = 950
        self.result_play_again_btn_pos_y = -(self.result_back_img.get_height() - 130)
        self.result_main_menu_btn_pos_y = -(self.result_back_img.get_height() - 230)

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
                try:
                    self.typing_letters_text_surface.append(self.font.render(self.word_chars[t], True, "black"))
                except (Exception,):
                    print(self.word_chars)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if (self.restart_btn_pos_x <= event.pos[0] <= self.restart_btn_pos_x + self.singleton.sound_button_size
                    and self.restart_btn_pos_y <= event.pos[1] <= self.restart_btn_pos_y +
                    self.singleton.sound_button_size):
                self.singleton.play_click_button()
                # stop playing background sound
                self.singleton.stop_background_sound()
                # start play normal background sound and birds sound
                self.singleton.play_background_sound()
                self.singleton.play_birds_sound()
                self.next_state = select_num_letters.SelectNumLetters(self.singleton)

            # handle click play again button
            if (self.result_btn_pos_x <= event.pos[0] <= self.result_btn_pos_x
                    + self.result_play_again_btn_img.get_width() and self.result_play_again_btn_pos_y
                    <= event.pos[1] <= self.result_play_again_btn_pos_y + self.result_play_again_btn_img.get_height()):
                self.singleton.play_click_button()
                # stop playing background sound
                self.singleton.stop_background_sound()
                self.next_state = PlayState(self.singleton)

            # handle click main menu button
            if (self.result_btn_pos_x <= event.pos[0] <= self.result_btn_pos_x
                    + self.result_main_menu_btn_img.get_width() and self.result_main_menu_btn_pos_y
                    <= event.pos[1] <= self.result_main_menu_btn_pos_y + self.result_main_menu_btn_img.get_height()):
                self.singleton.play_click_button()
                # stop playing background sound
                self.singleton.stop_background_sound()
                # start play normal background sound and birds sound
                self.singleton.play_background_sound()
                self.singleton.play_birds_sound()
                self.next_state = select_num_letters.SelectNumLetters(self.singleton)

        # get user typing
        if event.type == pygame.KEYDOWN:
            # accept typing when player does not reach finish line
            if self.player_pos <= 700:
                # still accept typing after wait 3 seconds completed
                # (-self.road_width) - 1 because from debug when finished is 0 > -11701 >= -11700 is not true
                if 0 > self.current_mov >= (-self.road_width) - 10:
                    if self.word_chars[self.current_typing_letter_index].lower() == str(event.unicode).lower():
                        # play typing sound
                        self.singleton.play_typing_sound()

                        # save typed letter
                        self.typed_letters.append(event.unicode)
                        if len(self.typed_letters) == self.singleton.get_num_letters():
                            # play sound when typed the last letter
                            self.singleton.play_typing_last_letter_sound()

                            completed_word = "".join(self.typed_letters)
                            # save typed word
                            self.typed_words.append(completed_word)
                            self.get_letters()

                            # increase speed 1 when complete the word
                            if self.player_speed <= 6:
                                self.player_speed += 1
                            self.last_update_player_speed = datetime.datetime.now()

                            # add to wrong words when typing wrong in some letters of current word
                            if self.current_word_is_wrong:
                                self.wrong_words.append(completed_word)

                            self.current_word_is_wrong = False
                        else:
                            # play sound when typing first letter
                            if len(self.typed_letters) == 1:
                                self.singleton.play_typing_first_letter_sound()

                            self.current_typing_letter_index += 1

                        self.letter_box = sih(pygame.image.load(
                            f'src/letter_box/normal/{self.singleton.get_num_letters()}letters/'
                            f'{self.current_typing_letter_index + 1}.png').convert_alpha(), 100)
                    else:
                        # play wrong sound
                        self.singleton.play_typing_wrong_sound()

                        self.letter_box = sih(pygame.image.load(
                            f'src/letter_box/incorrect/{self.singleton.get_num_letters()}letters/'
                            f'{self.current_typing_letter_index + 1}.png').convert_alpha(), 100)

                        # decrease speed 1 when typed incorrect letter
                        if self.player_speed >= 3:
                            self.player_speed -= 1
                        self.last_update_player_speed = datetime.datetime.now()

                        # set current typing word is wrong
                        self.current_word_is_wrong = True

                    # re-render text surface
                    self.get_text_surface()

        # hover
        if event.type == pygame.MOUSEMOTION:
            # handle hover on play again button
            if (self.result_btn_pos_x <= event.pos[0] <= self.result_btn_pos_x
                    + self.result_play_again_btn_img.get_width() and self.result_play_again_btn_pos_y
                    <= event.pos[1] <= self.result_play_again_btn_pos_y + self.result_play_again_btn_img.get_height()):
                self.result_play_again_btn_img = self.result_play_again_btn_hover_img
            else:
                self.result_play_again_btn_img = self.result_play_again_btn_normal_img

            # handle hover on main menu button
            if (self.result_btn_pos_x <= event.pos[0] <= self.result_btn_pos_x
                    + self.result_main_menu_btn_img.get_width() and self.result_main_menu_btn_pos_y
                    <= event.pos[1] <= self.result_main_menu_btn_pos_y + self.result_main_menu_btn_img.get_height()):
                self.result_main_menu_btn_img = self.result_main_menu_btn_hover_img
            else:
                self.result_main_menu_btn_img = self.result_main_menu_btn_normal_img

    def update(self):

        # wait 3 seconds
        total_sec = (datetime.datetime.now() - self.wait_3s_time).total_seconds()

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

            # create pos text
            self.pos_text = self.font.render("-/2", True, (255, 255, 255))
        else:
            # set started time
            if self.start_time is None:
                self.start_time = datetime.datetime.now()

            # clear time text
            self.time_img = None

            # play background sound
            self.singleton.play_background_sound("src/sounds/playing.ogg")

            # move background
            if -self.current_mov <= self.road_width:
                self.current_mov -= self.player_speed
                self.sky_mov -= .5
            elif self.player_pos <= 700:
                self.player_pos += self.player_speed
            elif -self.current_mov >= self.road_width and self.player_pos >= 700:
                # when player finish
                self.player_speed = 0
                if self.player_finish_time is None:
                    self.player_finish_time = datetime.datetime.now()

            # create timer text
            time_dif = datetime.datetime.now() - self.start_time
            time_dif = datetime.datetime(1, 1, 1) + time_dif
            if self.player_finish_time is None or self.other_player_finish_time is None:
                self.timer_text = self.font.render("{}".format(time_dif.strftime("%M:%S")), True, (255, 255, 255))

            # create pos text
            if -self.current_mov >= self.other_player_pos:
                self.pos_text = self.font.render("1/2", True, (255, 255, 255))
            else:
                self.pos_text = self.font.render("2/2", True, (255, 255, 255))

            # update other player position
            if self.other_player_pos <= self.road_width + 700:
                self.other_player_pos_y = (self.other_player_pos + self.current_mov) + self.other_player_speed
                self.other_player_pos += self.other_player_speed
            elif -self.current_mov <= self.road_width:
                self.other_player_pos_y = (self.other_player_pos + self.current_mov) - self.player_speed
                self.other_player_pos -= self.other_player_speed
            elif self.other_player_pos >= self.road_width + 700 and -self.current_mov >= self.road_width:
                if self.other_player_finish_time is None:
                    self.other_player_finish_time = datetime.datetime.now()

        # render text surface
        self.get_text_surface()

        # animate character
        if 50 < self.other_player_pos <= self.road_width + 700:
            self.other_player = self.other_player_seq[self.current_other_player_frame]
            self.current_other_player_frame = (self.current_other_player_frame + 1) % len(self.other_player_seq)

        if self.player_pos - 50 < -self.current_mov + (self.player_pos - 50) <= self.road_width + 650:
            self.player = self.player_seq[self.current_player_frame]
            self.current_player_frame = (self.current_player_frame + 1) % len(self.player_seq)

        # random other player speed every 3 seconds and random typed correct and wrong words
        if ((datetime.datetime.now() - self.last_update_other_player_speed).total_seconds() >=
                self.other_player_next_typed_duration and self.player_finish_time is None
                and self.other_player_finish_time is None):
            old_speed = self.other_player_speed
            self.other_player_speed = rnd.randrange(4, 9)
            self.last_update_other_player_speed = datetime.datetime.now()

            # used for count typed letters to calculate word per minutes
            self.other_typed_words.append(1)

            # generate correct or wrong words base on it speed changes
            if self.other_player_speed < old_speed:
                # can add 1 or other characters when typed wrong word, because we just its length only
                self.other_wrong_words.append(1)

            # random next random speed and typed word for other player duration
            self.other_player_next_typed_duration = rnd.randrange(2, 5)

        # decrease player speed
        if (datetime.datetime.now() - self.last_update_player_speed).total_seconds() >= 3 and self.player_speed >= 3:
            self.player_speed -= 1
            self.last_update_player_speed = datetime.datetime.now()

        if self.player_finish_time is not None and self.other_player_finish_time is not None:
            # play finish sound
            if not self.played_finish_sound:
                self.singleton.play_finish_sound()
                self.played_finish_sound = True

            # animate result background
            if self.result_back_img_pos_y <= 10:
                self.result_back_img_pos_y += 20

            # animate result character
            self.result_player = self.result_player_seq[self.current_result_player_frame]
            self.current_result_player_frame = (self.current_result_player_frame + 1) % len(self.result_player_seq)
            self.result_other_player = self.result_other_player_seq[self.current_result_other_player_frame]
            self.current_result_other_player_frame = ((self.current_result_other_player_frame + 1) %
                                                      len(self.result_other_player_seq))

            # calculate result
            self.time_taken = self.player_finish_time - self.start_time
            self.other_time_taken = self.other_player_finish_time - self.start_time
            self.wpm = len(self.typed_words) / (self.time_taken.total_seconds() / 60)
            self.other_wpm = len(self.other_typed_words) / (self.other_time_taken.total_seconds() / 60)
            if len(self.typed_words) == 0:
                self.result_player_accuracy = 0
            else:
                self.result_player_accuracy = 100 - (len(self.wrong_words) * 100) / len(self.typed_words)
            self.result_other_player_accuracy = 100 - (len(self.other_wrong_words) * 100) / len(self.other_typed_words)

            if self.wpm > self.other_wpm:
                # init result text
                if self.result_text_player_pos_y is None and self.result_text_other_player_pos_y is None:
                    self.result_text_player_pos_y = -(self.result_back_img.get_height() - 200)
                    self.result_text_other_player_pos_y = -(self.result_back_img.get_height() - 370)

                # init all player position
                if self.result_player_pos_y is None and self.result_other_player_pos_y is None:
                    self.result_player_pos_y = -(self.result_back_img.get_height() - 190)
                    self.result_other_player_pos_y = -(self.result_back_img.get_height() - 330)

                # animate character position
                if self.result_player_pos_y <= 190:
                    self.result_player_pos_y += 20
                if self.result_other_player_pos_y <= 350:
                    self.result_other_player_pos_y += 20

                # animate result text
                if self.result_text_player_pos_y <= 230:
                    self.result_text_player_pos_y += 20
                if self.result_text_other_player_pos_y <= 386:
                    self.result_text_other_player_pos_y += 20
            else:
                # init result text
                if self.result_text_player_pos_y is None and self.result_text_other_player_pos_y is None:
                    self.result_text_player_pos_y = -(self.result_back_img.get_height() - 370)
                    self.result_text_other_player_pos_y = -(self.result_back_img.get_height() - 200)

                # init all player position
                if self.result_player_pos_y is None and self.result_other_player_pos_y is None:
                    self.result_player_pos_y = -(self.result_back_img.get_height() - 330)
                    self.result_other_player_pos_y = -(self.result_back_img.get_height() - 190)

                # animate character position
                if self.result_player_pos_y <= 350:
                    self.result_player_pos_y += 20
                if self.result_other_player_pos_y <= 190:
                    self.result_other_player_pos_y += 20

                # animate result text
                if self.result_text_player_pos_y <= 386:
                    self.result_text_player_pos_y += 20
                if self.result_text_other_player_pos_y <= 230:
                    self.result_text_other_player_pos_y += 20

            # name
            self.result_player_name_surface = self.font.render(self.singleton.get_user_name(), True, "red")
            self.result_other_player_name_surface = self.font.render(self.other_player_name_text, True, "red")

            # Word per minutes
            self.result_player_wpm_surface = self.font.render(str(self.wpm).split('.')[0] + " WPM", True, "black")
            self.result_other_player_wpm_surface = self.font.render(str(self.other_wpm).split('.')[0] + " WPM",
                                                                    True, "black")

            # Accuracy
            self.result_player_accuracy_surface = self.font.render(
                str(self.result_player_accuracy).split('.')[0] + " %", True, "red")
            self.result_other_player_accuracy_surface = self.font.render(
                str(self.result_other_player_accuracy).split('.')[0] + " %", True, "red")

            # Accuracy
            self.result_player_time_taken_surface = self.font.render(
                str(self.time_taken.total_seconds() / 60).split('.')[0].rjust(2, '0') + ":"
                + str(self.time_taken.total_seconds() % 60).split('.')[0].rjust(2, '0'), True, "black")
            self.result_other_player_time_taken_surface = self.font.render(
                str(self.other_time_taken.total_seconds() / 60).split('.')[0].rjust(2, '0') + ":"
                + str(self.other_time_taken.total_seconds() % 60).split('.')[0].rjust(2, '0'), True, "black")

            # animate result button
            if self.result_play_again_btn_pos_y <= 150:
                self.result_play_again_btn_pos_y += 20
            if self.result_main_menu_btn_pos_y <= 230:
                self.result_main_menu_btn_pos_y += 20

    def draw(self):
        # draw sky
        for x in range(3):
            self.singleton.get_screen().blit(self.sky_back_img,
                                             (x * self.sky_back_img.get_width() + self.sky_mov, -70))

        self.singleton.get_screen().blit(self.road, (self.current_mov, 20))

        # draw object when not finish the game
        if self.result_back_img_pos_y <= 10:
            self.singleton.get_screen().blit(self.timer_pos_back_img, (0, 0))

            # render text
            self.singleton.get_screen().blit(self.timer_text, (70, 40))
            self.singleton.get_screen().blit(self.pos_text, (self.singleton.get_screen_size()[0] - 90, 40))

            # draw position
            # start pos = self.singleton.get_screen_size()[0] * .25 = 320
            # end pos = self.singleton.get_screen_size()[0] * .75 = 960

            # % = ((current - start) * 100) / (current - start)
            road_pos_percent = (self.current_mov * 100) / -self.road_width
            other_player_pos_percent = (self.other_player_pos * 100) / (self.road_width + 700)
            # current point pos = start + (% * (end - start))
            pygame.draw.circle(self.singleton.get_screen(), (255, 0, 0),
                               (self.start_pos + ((other_player_pos_percent * (self.end_pos - self.start_pos)) / 100),
                                55), 8)
            pygame.draw.circle(self.singleton.get_screen(), (0, 255, 0),
                               (self.start_pos + ((road_pos_percent * (self.end_pos - self.start_pos)) / 100), 55), 8)

            # draw word to typing
            self.singleton.get_screen().blit(self.letter_box, ((self.singleton.get_screen_size()[0] / 2) -
                                                               self.letter_box.get_width() / 2,
                                                               self.singleton.get_screen_size()[1] -
                                                               (self.letter_box.get_height())))
            self.typing_letter_pos_x = self.first_letter_pos
            for t in range(self.singleton.get_num_letters()):
                try:
                    x = (self.typing_letter_pos_x + 22.5) - (self.typing_letters_text_surface[t].get_width() / 2)
                    self.singleton.get_screen().blit(self.typing_letters_text_surface[t],
                                                     (x, self.singleton.get_screen_size()[1] -
                                                      (self.typing_letters_text_surface[t].get_height() * 2)))
                    self.typing_letter_pos_x += 55
                except (Exception,):
                    print(self.typing_letters_text_surface)

            # restart button
            self.singleton.get_screen().blit(self.restart_btn_img, (self.restart_btn_pos_x, self.restart_btn_pos_y))

            # draw characters
            self.singleton.get_screen().blit(self.other_player, (self.other_player_pos_y,
                                                                 (self.singleton.get_screen_size()[1] * .25)))
            self.singleton.get_screen().blit(self.player,
                                             (self.player_pos, (self.singleton.get_screen_size()[1] * .53)))

            # draw character name
            self.singleton.get_screen().blit(self.other_player_name_back,
                                             (self.other_player_pos_y, (self.singleton.get_screen_size()[1] * .32)))
            self.singleton.get_screen().blit(self.other_player_name, (self.other_player_pos_y - 5 +
                                                                      ((self.other_player_name_back.get_width() / 2) -
                                                                       (self.other_player_name.get_width() / 2)),
                                                                      (self.singleton.get_screen_size()[1] * .32)))
            self.singleton.get_screen().blit(self.player_name_back,
                                             (self.player_pos, (self.singleton.get_screen_size()[1] * .60)))
            self.singleton.get_screen().blit(self.player_name,
                                             (self.player_pos - 5 + ((self.player_name_back.get_width() / 2) -
                                                                     (self.player_name.get_width() / 2)),
                                              (self.singleton.get_screen_size()[1] * .60)))

            # draw waiting 3 seconds
            if self.time_img is not None:
                self.singleton.get_screen().blit(self.time_img, ((self.singleton.get_screen_size()[0] / 2) -
                                                                 (self.time_img.get_width() / 2),
                                                                 (self.singleton.get_screen_size()[1] / 2) -
                                                                 (self.time_img.get_height() * .20)))

        if self.player_finish_time is not None and self.other_player_finish_time is not None:
            # draw result background
            self.singleton.get_screen().blit(self.result_back_img, (50, self.result_back_img_pos_y))

            # draw character result
            self.singleton.get_screen().blit(self.result_player, (40, self.result_player_pos_y))
            self.singleton.get_screen().blit(self.result_other_player, (40, self.result_other_player_pos_y))

            # draw player name
            self.singleton.get_screen().blit(self.result_player_name_surface, (250, self.result_text_player_pos_y))
            self.singleton.get_screen().blit(self.result_other_player_name_surface,
                                             (250, self.result_text_other_player_pos_y))

            # draw WPM
            self.singleton.get_screen().blit(self.result_player_wpm_surface, (450, self.result_text_player_pos_y))
            self.singleton.get_screen().blit(self.result_other_player_wpm_surface,
                                             (450, self.result_text_other_player_pos_y))

            # draw accuracy
            self.singleton.get_screen().blit(self.result_player_accuracy_surface, (620, self.result_text_player_pos_y))
            self.singleton.get_screen().blit(self.result_other_player_accuracy_surface,
                                             (620, self.result_text_other_player_pos_y))

            # draw time taken
            self.singleton.get_screen().blit(self.result_player_time_taken_surface,
                                             (760, self.result_text_player_pos_y))
            self.singleton.get_screen().blit(self.result_other_player_time_taken_surface,
                                             (760, self.result_text_other_player_pos_y))

            # draw result button
            self.singleton.get_screen().blit(self.result_play_again_btn_img,
                                             (self.result_btn_pos_x, self.result_play_again_btn_pos_y))
            self.singleton.get_screen().blit(self.result_main_menu_btn_img,
                                             (self.result_btn_pos_x, self.result_main_menu_btn_pos_y))
