import pygame
from pygame import Surface


def scale_img_height(img: Surface, new_height):
    scaling_factor = new_height / img.get_height()
    new_width = int(img.get_width() * scaling_factor)
    return pygame.transform.scale(img, (new_width, new_height))
