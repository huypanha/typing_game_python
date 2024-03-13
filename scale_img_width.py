import pygame
from pygame import Surface


def scale_img_width(img: Surface, new_width):
    scaling_factor = new_width / img.get_width()
    new_height = int(img.get_height() * scaling_factor)
    return pygame.transform.scale(img, (new_width, new_height))
