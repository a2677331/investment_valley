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
        building1_rect = pygame.Rect(130, 31, 179, 100)
        building2_rect = pygame.Rect(553, 47, 197, 105)
        building3_rect = pygame.Rect(987, 75, 206, 85)
        building4_rect = pygame.Rect(261, 480, 117, 92)
        building5_rect = pygame.Rect(1007, 500, 165, 90)
        buidling_rects = [building1_rect, building2_rect, building3_rect, building4_rect, building5_rect]
        
        # player
        self.player = Player((640, 360), self.all_sprites, buidling_rects)
                             
    def run(self, dt):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt) # update every sprite in setup()


        ## For testing building collision
        # building1_rect = pygame.Rect(130, 31, 179, 100)
        # building2_rect = pygame.Rect(553, 47, 197, 105)
        # building3_rect = pygame.Rect(987, 75, 206, 85)
        # building4_rect = pygame.Rect(261, 480, 117, 92)
        # building5_rect = pygame.Rect(1007, 500, 165, 90)

        # pygame.draw.rect(self.display_surface, 'black', building1_rect)
        # pygame.draw.rect(self.display_surface, 'black', building2_rect)
        # pygame.draw.rect(self.display_surface, 'black', building3_rect)
        # pygame.draw.rect(self.display_surface, 'black', building4_rect)
        # pygame.draw.rect(self.display_surface, 'black', building5_rect)
