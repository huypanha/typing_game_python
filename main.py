import pygame
from menu_state import MenuState

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Angkor Typing Game")

menu_state = MenuState(GAME_SCREEN, WINDOW_WIDTH, WINDOW_HEIGHT)

current_state = menu_state
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
