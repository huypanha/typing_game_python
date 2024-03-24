import pygame
from pygame import Surface


def width(img: Surface, new_width):
    scaling_factor = new_width / img.get_width()
    new_height = int(img.get_height() * scaling_factor)
    return pygame.transform.scale(img, (new_width, new_height))


def height(img: Surface, new_height):
    scaling_factor = new_height / img.get_height()
    new_width = int(img.get_width() * scaling_factor)
    return pygame.transform.scale(img, (new_width, new_height))
