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
        
        # money earned by user
        self.money = 0

    def setup(self):
        # background image
        Generic((0,50), pygame.image.load("graphics/world/ground.png").convert_alpha(), self.all_sprites)

        # buildings' position and size for collision detection
        building1_rect = pygame.Rect(130, 101, 179, 90)
        building2_rect = pygame.Rect(553, 117, 197, 85)
        building3_rect = pygame.Rect(987, 145, 206, 65)
        building4_rect = pygame.Rect(261, 550, 117, 82)
        building5_rect = pygame.Rect(1007, 570, 165, 75)
        buidling_rects = [building1_rect, building2_rect, building3_rect, building4_rect, building5_rect]
        
        # player
        self.player = Player((640,360), self.all_sprites, buidling_rects, display_surface)
                             
    def run(self, dt, start_time):
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt) # update every sprite in setup()

        # Check if the player is in the stock building
        if self.player.in_stock_building:
            self.player.stock_menu()
            self.player.handle_stock_menu_input()

            # Display stock prices on the screen
            self.player.display_stock_prices()
            
        return display_status_bar(self.display_surface, start_time, self.money)

