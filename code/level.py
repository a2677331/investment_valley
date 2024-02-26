import pygame
from player import Player
from support import *
from sprites import * 
from menu import Menu 

'''
This file is to draw the game level layout
'''

class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        
        # player's starting balance 
        self.balance = 1500
        
        # buildings' position and size for collision detection
        self.stock_building_rect = pygame.Rect(130, 101, 179, 90)
        self.real_estate_rect = pygame.Rect(553, 117, 197, 85)
        self.casino_rect = pygame.Rect(987, 145, 206, 65)
        self.bank_rect = pygame.Rect(261, 550, 117, 82)
        self.lottery_rect = pygame.Rect(1007, 570, 165, 75)

        # background music in playing the game
        self.level_music = load_background_music('bg.mp3', 0.2)
        self.level_music.play(-1)
        
        # setup background image, player and buidlings surfaces
        self.level_setup()
        
        # buidling menu and interaction
        self.buidling_active = False
        self.building_name = None
        
    def level_setup(self):
        # background image
        Generic((0,50), pygame.image.load(f'{grandparent_file_path}/graphics/world/ground.png').convert_alpha(), self.all_sprites)

        # building detection rects list
        buidling_rect_list = [self.stock_building_rect, self.real_estate_rect, self.casino_rect, self.bank_rect, self.lottery_rect]

        # player
        self.player = Player((640,360), buidling_rect_list, self.toggle_building, self.all_sprites)

        # menu
        self.menu = Menu(self.player, self.toggle_building, self.modify_money_by)
    
    def toggle_building(self, building_name=None):
        """ enable player to toggle building """
        self.buidling_active = not self.buidling_active
        self.building_name = building_name               # update building name in menu
    
    def modify_money_by(self, value=None):
        """ Function to update the player's balance in the game """
        if value is not None:
            self.balance += value
        return self.balance
        
    def run(self, dt, start_time):
        # drawing logic
        self.display_surface.fill("black") # so don't accidentally see previous frame
        self.all_sprites.draw(self.display_surface)
        
        # when menu is opened, show menu and stop all other updates
        if self.buidling_active:
            self.menu.update(self.building_name)
        # otherwise, run all other game level update
        else:
            self.all_sprites.update(dt)
            self.menu = Menu(self.player, self.toggle_building, self.modify_money_by) # reinitialize menu states avoid showing the last page of the menu
        return display_status_bar(self.display_surface, start_time, self.balance)