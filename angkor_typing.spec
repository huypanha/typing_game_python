# -*- mode: python ; coding: utf-8 -*-
import glob

datas = [
('src/background.jpg', './src'),
('src/logo.png', './src'),
('src/muted.png', './src'),
('src/back_button.png', './src'),
('src/loading_text.png', './src'),
('src/play_button.png', './src'),
('src/play_button_hover.png', './src'),
('src/unmuted.png', './src'),
('src/characters/Monkey/Comp 1_00000.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00001.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00002.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00003.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00004.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00005.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00006.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00007.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00008.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00009.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00010.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00011.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00012.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00013.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00014.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00015.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00016.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00017.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00018.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00019.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00020.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00021.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00022.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00023.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00024.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00025.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00026.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00027.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00028.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00029.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00030.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00031.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00032.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00033.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00034.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00035.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00036.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00037.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00038.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00039.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00040.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00041.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00042.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00043.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00044.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00045.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00046.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00047.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00048.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00049.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00050.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00051.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00052.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00053.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00054.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00055.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00056.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00057.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00058.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00059.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00060.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00061.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00062.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00063.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00064.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00065.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00066.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00067.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00068.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00069.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00070.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00071.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00072.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00073.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00074.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00075.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00076.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00077.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00078.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00079.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00080.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00081.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00082.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00083.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00084.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00085.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00086.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00087.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00088.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00089.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00090.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00091.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00092.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00093.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00094.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00095.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00096.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00097.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00098.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00099.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00100.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00101.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00102.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00103.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00104.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00105.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00106.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00107.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00108.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00109.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00110.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00111.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00112.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00113.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00114.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00115.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00116.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00117.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00118.png', './src/characters/Monkey'),
('src/characters/Monkey/Comp 1_00119.png', './src/characters/Monkey'),
('src/characters/Rabbit/Comp 2_00000.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00001.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00002.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00003.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00004.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00005.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00006.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00007.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00008.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00009.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00010.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00011.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00012.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00013.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00014.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00015.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00016.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00017.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00018.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00019.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00020.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00021.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00022.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00023.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00024.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00025.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00026.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00027.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00028.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00029.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00030.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00031.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00032.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00033.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00034.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00035.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00036.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00037.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00038.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00039.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00040.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00041.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00042.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00043.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00044.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00045.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00046.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00047.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00048.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00049.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00050.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00051.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00052.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00053.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00054.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00055.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00056.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00057.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00058.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00059.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00060.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00061.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00062.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00063.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00064.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00065.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00066.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00067.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00068.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00069.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00070.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00071.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00072.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00073.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00074.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00075.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00076.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00077.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00078.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00079.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00080.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00081.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00082.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00083.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00084.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00085.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00086.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00087.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00088.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00089.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00090.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00091.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00092.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00093.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00094.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00095.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00096.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00097.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00098.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00099.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00100.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00101.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00102.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00103.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00104.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00105.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00106.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00107.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00108.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00109.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00110.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00111.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00112.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00113.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00114.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00115.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00116.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00117.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00118.png', './src/characters/Rabbit'),
('src/characters/Rabbit/Comp 2_00119.png', './src/characters/Rabbit'),
('src/choose_character/back.png', './src/choose_character'),
('src/choose_character/selecting_back.png', './src/choose_character'),
('src/choose_character/title_text.png', './src/choose_character'),
('src/enter_name/enter_name_back.png', './src/enter_name'),
('src/letter_box/incorrect/3letters/1.png', './src/letter_box/incorrect/3letters'),
('src/letter_box/incorrect/3letters/2.png', './src/letter_box/incorrect/3letters'),
('src/letter_box/incorrect/3letters/3.png', './src/letter_box/incorrect/3letters'),
('src/letter_box/incorrect/4letters/1.png', './src/letter_box/incorrect/4letters'),
('src/letter_box/incorrect/4letters/2.png', './src/letter_box/incorrect/4letters'),
('src/letter_box/incorrect/4letters/3.png', './src/letter_box/incorrect/4letters'),
('src/letter_box/incorrect/4letters/4.png', './src/letter_box/incorrect/4letters'),
('src/letter_box/incorrect/5letters/1.png', './src/letter_box/incorrect/5letters'),
('src/letter_box/incorrect/5letters/2.png', './src/letter_box/incorrect/5letters'),
('src/letter_box/incorrect/5letters/3.png', './src/letter_box/incorrect/5letters'),
('src/letter_box/incorrect/5letters/4.png', './src/letter_box/incorrect/5letters'),
('src/letter_box/incorrect/5letters/5.png', './src/letter_box/incorrect/5letters'),
('src/letter_box/incorrect/6letters/1.png', './src/letter_box/incorrect/6letters'),
('src/letter_box/incorrect/6letters/2.png', './src/letter_box/incorrect/6letters'),
('src/letter_box/incorrect/6letters/3.png', './src/letter_box/incorrect/6letters'),
('src/letter_box/incorrect/6letters/4.png', './src/letter_box/incorrect/6letters'),
('src/letter_box/incorrect/6letters/5.png', './src/letter_box/incorrect/6letters'),
('src/letter_box/incorrect/6letters/6.png', './src/letter_box/incorrect/6letters'),
('src/letter_box/normal/3letters/1.png', './src/letter_box/normal/3letters'),
('src/letter_box/normal/3letters/2.png', './src/letter_box/normal/3letters'),
('src/letter_box/normal/3letters/3.png', './src/letter_box/normal/3letters'),
('src/letter_box/normal/4letters/1.png', './src/letter_box/normal/4letters'),
('src/letter_box/normal/4letters/2.png', './src/letter_box/normal/4letters'),
('src/letter_box/normal/4letters/3.png', './src/letter_box/normal/4letters'),
('src/letter_box/normal/4letters/4.png', './src/letter_box/normal/4letters'),
('src/letter_box/normal/5letters/1.png', './src/letter_box/normal/5letters'),
('src/letter_box/normal/5letters/2.png', './src/letter_box/normal/5letters'),
('src/letter_box/normal/5letters/3.png', './src/letter_box/normal/5letters'),
('src/letter_box/normal/5letters/4.png', './src/letter_box/normal/5letters'),
('src/letter_box/normal/5letters/5.png', './src/letter_box/normal/5letters'),
('src/letter_box/normal/6letters/1.png', './src/letter_box/normal/6letters'),
('src/letter_box/normal/6letters/2.png', './src/letter_box/normal/6letters'),
('src/letter_box/normal/6letters/3.png', './src/letter_box/normal/6letters'),
('src/letter_box/normal/6letters/4.png', './src/letter_box/normal/6letters'),
('src/letter_box/normal/6letters/5.png', './src/letter_box/normal/6letters'),
('src/letter_box/normal/6letters/6.png', './src/letter_box/normal/6letters'),
('src/play/1.png', './src/play'),
('src/play/2.png', './src/play'),
('src/play/3.png', './src/play'),
('src/play/GO.png', './src/play'),
('src/play/main_menu_btn.png', './src/play'),
('src/play/main_menu_btn_hover.png', './src/play'),
('src/play/other_player_name.png', './src/play'),
('src/play/play_again_btn.png', './src/play'),
('src/play/play_again_btn_hover.png', './src/play'),
('src/play/player_name.png', './src/play'),
('src/play/race_results.png', './src/play'),
('src/play/restart_button.png', './src/play'),
('src/play/road.png', './src/play'),
('src/play/sky.png', './src/play'),
('src/play/timer_pos.png', './src/play'),
('src/select_letters/3_letters.png', './src/select_letters'),
('src/select_letters/3_letters_selected.png', './src/select_letters'),
('src/select_letters/4_letters.png', './src/select_letters'),
('src/select_letters/4_letters_selected.png', './src/select_letters'),
('src/select_letters/5_letters.png', './src/select_letters'),
('src/select_letters/5_letters_selected.png', './src/select_letters'),
('src/select_letters/6_letters.png', './src/select_letters'),
('src/select_letters/6_letters_selected.png', './src/select_letters'),
('src/select_letters/select_letter_title.png', './src/select_letters'),
('src/sounds/background.ogg', './src/sounds'),
('src/sounds/birds.ogg', './src/sounds'),
('src/sounds/button_click.ogg', './src/sounds'),
('src/sounds/countdown.ogg', './src/sounds'),
('src/sounds/countdown_end.ogg', './src/sounds'),
('src/sounds/finish.ogg', './src/sounds'),
('src/sounds/last_letter.ogg', './src/sounds'),
('src/sounds/playing.ogg', './src/sounds'),
('src/sounds/start_letter.ogg', './src/sounds'),
('src/sounds/typed_wrong.ogg', './src/sounds'),
('src/sounds/typing.ogg', './src/sounds'),
('src/submit_button.png', './src'),
('src/submit_button_hover.png', './src'),
('fonts/*', "./fonts"),
('infrastructure/*', "./infrastructure"),
('utils/*', "./utils"),
('words/*', "./words"),
('*.*', ".")
]

a = Analysis(
    ['angkor_typing.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    icon='icon.ico'
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='angkor_typing',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
    onefile=True
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='angkor_typing',
)
