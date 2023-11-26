import pygame
from player import Player
from support import *
from sprites import * 

'''
This file is to draw the game
'''
class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        
        self.setup()

    def setup(self):
        # background image
        Generic((0,0), pygame.image.load("graphics/world/ground.png").convert_alpha(), self.all_sprites)
        
        # buildings' position and size for collision detection
        building1_rect = pygame.Rect(130, 31, 179, 129)
        building2_rect = pygame.Rect(553, 47, 197, 142)
        building3_rect = pygame.Rect(987, 75, 206, 114)
        building4_rect = pygame.Rect(261, 480, 117, 129)
        building5_rect = pygame.Rect(1007, 500, 165, 125)
        buidling_rects = [building1_rect, building2_rect, building3_rect, building4_rect, building5_rect]
        
        # player
        self.player = Player((640, 360), self.all_sprites, buidling_rects)
                             
    def run(self, dt):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt) # update every sprite in setup()