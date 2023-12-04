import pygame
import sys
from level import Level
from settings import *
from support import *
from lottery import *
from roulette import play_roulette_game

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Investment Valley")
        self.level = Level()
        self.game_active = False
        self.score = None
        self.start_time = None
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
                dt = self.clock.tick() / 1000
                if self.level.run(dt, self.start_time)[0] <= 0:
                    self.game_active = False
                    self.start_time = int(pygame.time.get_ticks() / 1000)
                    self.score = self.level.run(dt, self.start_time)[1]

                if self.level.player.in_stock_building:
                    self.level.player.stock_menu()
                    self.level.player.handle_stock_menu_input()
                    self.level.player.get_stock_prices_text()
                    self.level.player.update(dt)
            else:
                show_intro_screen(self.screen, self.score)

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
