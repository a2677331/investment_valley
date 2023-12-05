import pygame, sys 
from level import Level
from settings import *
from support import *
from pygame.locals import *
from lottery import *
from roulette import play_roulette_game

'''
This file is about initial setup, 
to start the game or display intro screen depending on whether the game is active or not
'''

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # setup game window
        self.clock = pygame.time.Clock() # for animation
        pygame.display.set_caption("Investment Valley") # set show game title
        self.level = Level()     # game level laytout
        self.game_active = False # detect if the game is being played or in intro screen status
        self.score = None        # money score
        self.start_time = None   # game start time for counting each round of the game
        self.money = 1500

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.game_active:
                            self.game_active = True
                            self.start_time = int(pygame.time.get_ticks() / 1000)
                    elif event.key == pygame.K_l:
                        if self.game_active:
                            self.money = play_lottery(self.level, self.money)
                    elif event.key == pygame.K_r:
                        if self.game_active:
                            play_roulette_game(self.level, self.screen)

            if self.game_active:
                # run the game
                dt = self.clock.tick() / 1000

                if self.level.run(dt, self.start_time)[0] <= 0:
                    self.game_active = False
                    self.start_time = int(pygame.time.get_ticks() / 1000) # reset the game start time
                    self.score = self.level.run(dt, self.start_time)[1]   # get money score from the game previusly played

                if self.level.player.in_stock_building:
                    if self.level.player.show_stock_menu:
                        self.level.player.stock_menu()
                        self.level.player.handle_stock_menu_input()
                        self.level.player.get_stock_prices_text()
                        self.level.player.update(dt)
            else:
                # show intro screen
                show_intro_screen(self.screen, self.score)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.game_active = True
                    self.start_time = int(pygame.time.get_ticks() / 1000)    # initialize game start time
            
            pygame.display.update() # update everything


if __name__ == '__main__':
    game = Game()
    game.run()  # initialize the game
