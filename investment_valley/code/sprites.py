import pygame

'''
To provide a genearal sprite layout for the game, 
used in level.py to load and display background image
'''

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)