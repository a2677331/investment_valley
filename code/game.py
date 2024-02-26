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
        self.game_setup()
    
    
    def game_setup(self):
        # set show game title
        pygame.display.set_caption("Investment Valley")
        
        # setup game paramaters
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # setup game window
        self.clock = pygame.time.Clock() # for animation

        # # background music for game intro screens
        self.intro_music = load_background_music('music.mp3', 0.5)
        self.intro_music.play(-1)  # NOTE: cannot be put into run() function, else won't run!

        # audio effect for space key
        self.success_sound = pygame.mixer.Sound(f'{grandparent_file_path}/audio/success.wav')
        self.success_sound.set_volume(0.2)



    # handle space key pressed on intro screen, and create game level
    def handle_space_key(self, game_active, start_time):
        keys = pygame.key.get_pressed() # key disctionary
        level = None # game level will be generated by pressed space key
        
        if keys[pygame.K_SPACE]:
            self.success_sound.play()  # start sound effect for space key
            self.intro_music.fadeout(250)   # stop the intro music
            game_active = True
            level = Level()           # NOTE: Level(): create game level only when space key is pressed, otherwise will creat errors!
            start_time = int(pygame.time.get_ticks() / 1000)    # re-initialize game start time
        
        return game_active, start_time, level


    def run_game(self, game_active, start_time, score, level):
        dt = self.clock.tick() / 1000         # for smoothing the animation
        
        # The round time is up, end the game
        if level.run(dt, start_time)[0] <= 0:
            game_active = False
            start_time = int(pygame.time.get_ticks() / 1000) # reset the game start time
            score = level.run(dt, start_time)[1]   # get player's balance score from the game previusly played
            level.level_music.fadeout(250)         # stop the game music when game ends
            load_background_music('music.mp3', 0.5) # NOTE: why need this line??? -> because pygame.mixer.music can only load one file!
            self.intro_music.play(-1)
            
        return game_active, start_time, score
    
    
    def handle_game_exit(self):
        for event in pygame.event.get():
            # quit the game safely
            if event.type == pygame.QUIT:
                pygame.quit()
                pygame.time.delay(200)  # Wait for 200 milliseconds
                sys.exit()
        
        
    # to run the main game loop
    def run(self):
        game_active = False # deside if the game is being played or in intro screen status
        score = None        # player's balance score
        start_time = None   # game's starting time for counting each round of the game
        level = None        # game level has not been initialized yet
    
        # the main game loop
        while True:
            # so game can exit safely
            self.handle_game_exit()
                     
            # Run the intro screen first
            if not game_active:
                # show intro screen
                draw_intro_screen(self.screen, score)
                game_active, start_time, level = self.handle_space_key(game_active, start_time) # when space key is pressed, genearte a new game level
            else:
                # run the game if space key is pressed
                game_active, start_time, score = self.run_game(game_active, start_time, score, level) # the game level is used to run game and output scores
            
            # update everything's update() function
            pygame.display.update()




if __name__ == '__main__':
    game = Game() # initialize the game
    game.run()    # run the game 