import pygame
from menu_state import MenuState
from infrastructure import singleton as st

pygame.init()

singleton = st.Singleton.instance()
pygame.display.set_caption("Angkor Typing Game")

current_state = MenuState(singleton)
FPS = 60

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        current_state.handle_events(event)

    current_state.update()
    current_state.draw()

    # Check if state needs to be changed
    if current_state.next_state:
        current_state = current_state.next_state

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)

pygame.quit()
