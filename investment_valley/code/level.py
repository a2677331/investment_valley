import pygame
from player import Player
from support import *
from sprites import * 

'''
This file is to draw the game layout
'''

# Function to draw a rounded rectangle
def draw_rounded_rect(surface, color, rect, radius):
    pygame.draw.rect(surface, color, rect, border_radius=radius)

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        
        # setup background image, player and buidlings surfaces
        self.setup()

    def setup(self):
        # background image
        Generic((0,50), pygame.image.load("graphics/world/ground.png").convert_alpha(), self.all_sprites)

        # buildings' position and size for collision detection
        building1_rect = pygame.Rect(130, 101, 179, 100)
        building2_rect = pygame.Rect(553, 117, 197, 105)
        building3_rect = pygame.Rect(987, 145, 206, 85)
        building4_rect = pygame.Rect(261, 550, 117, 92)
        building5_rect = pygame.Rect(1007, 570, 165, 90)
        buidling_rects = [building1_rect, building2_rect, building3_rect, building4_rect, building5_rect]
        
        # player
        self.player = Player((640,360), self.all_sprites, buidling_rects)
                             
    def run(self, dt, start_time):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt) # update every sprite in setup()
        return display_time_left(self.display_surface, start_time)

