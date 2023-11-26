import pygame
from os import walk

# To import image files for animations,
# output a list of surfaces converted from images files.
def import_folder(path):
    surface_list = []
    for _, _, image_files in walk(path):
        for image in image_files:
            image_surface = pygame.image.load(f'{path}/{image}').convert_alpha()
            surface_list.append(image_surface)
    return surface_list