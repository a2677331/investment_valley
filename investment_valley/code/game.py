import pygame, sys 
from level import Level
from settings import *
from support import *

'''
This file is about initial setup, 
to start the game or display intro screen depending on whether the game is active or not
'''

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Investment Valley") # set show game title
        self.level = Level()
        self.game_active = False
        self.score = 0      # money score
        self.start_time = 0 # set game start time
        self.money = None   # player's moeny score

    def run(self):
        while True:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                                
            if self.game_active:
                # run the game
                dt = self.clock.tick() / 1000
                if self.level.run(dt, self.start_time)[0] <= 0: # if time is up, end the game
                    self.game_active = False
                    self.start_time = int(pygame.time.get_ticks() / 1000) # reset start time

                    if self.level.player.in_stock_building:
                        self.level.player.stock_menu()
                        self.level.player.handle_stock_menu_input()
            else:
                # show intro screen
                show_intro_screen(self.screen, self.score)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.game_active = True
            
            pygame.display.update() # update everything


if __name__ == '__main__':
    game = Game()
    game.run()  # initialize the game
