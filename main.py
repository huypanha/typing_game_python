import pygame
from infrastructure import singleton as st
from loading import LoadingState

pygame.init()

singleton = st.Singleton.instance()
pygame.display.set_caption("Angkor Typing Game")

current_state = LoadingState(singleton)
FPS = 60

# load all characters at the first time
singleton.start_thread(current_state.load_images)

# sound button
sound_button_pos_x = (singleton.get_screen_size()[0] -
                                   (singleton.get_sound_button_img().get_width() + 20))
sound_button_pos_y = (singleton.get_screen_size()[1] -
                                   (singleton.get_sound_button_img().get_width() + 20))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        current_state.handle_events(event)

        if event.type == pygame.MOUSEBUTTONUP:
            if (sound_button_pos_x <= event.pos[0] <= sound_button_pos_x + singleton.sound_button_size
                    and sound_button_pos_y <= event.pos[1] <= sound_button_pos_y + singleton.sound_button_size):
                singleton.toggle_mute_normal_sound()

    current_state.update()
    current_state.draw()

    singleton.get_screen().blit(singleton.get_sound_button_img(), (sound_button_pos_x, sound_button_pos_y))

    # Check if state needs to be changed
    if current_state.next_state:
        current_state = current_state.next_state

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
