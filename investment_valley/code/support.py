import pygame
from os import walk

'''
This file is to provide supporting functions for all the other files.
'''

# To import image files and output a list of surfaces converted from images files for for character animations.
# used in player.py
def import_folder(path):
    surface_list = []
    for _, _, image_files in walk(path):
        for image in image_files:
            image_surface = pygame.image.load(f'{path}/{image}').convert_alpha()
            surface_list.append(image_surface)
    return surface_list

# To display time left for each round of the game
# used in level.py
def display_time_left(screen, start_time):
    text_font = pygame.font.Font('font/LycheeSoda.ttf', 40)
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    time_left = 300 - current_time # set as 300 seconds time limit per round
    time_surface = text_font.render(f'TIME LEFT: {time_left}', False, (200,200,200)).convert()
    time_rect = time_surface.get_rect(center=(1280/2,25))
    screen.blit(time_surface, time_rect)
    return time_left
    
# To display Intro screen
# used in game.py
def show_intro_screen(screen, score):
    # game title
    title_font = pygame.font.Font('font/LycheeSoda.ttf', 100)
    game_title_surface = title_font.render("Investment Valley", False, "#ffffff").convert()
    game_title_rect = game_title_surface.get_rect(center = (1280/2,220))

    # game instruction
    text_font = pygame.font.Font('font/LycheeSoda.ttf', 30)
    instruction_surface = text_font.render("Press space to start", False, (111,196,169)).convert()
    instruction_rect = instruction_surface.get_rect(center = (1280/2,330))

    # draw intro screen
    screen.fill("black")
    screen.blit(game_title_surface, game_title_rect)
    
    # show different screens before initial play and other play
    if score == 0:
        # show instrction when first time played
        screen.blit(instruction_surface, instruction_rect)
    else:
        # display updated game score
        score_surface = text_font.render(f'Your last score: {score}', False, (111,196,169)).convert()
        score_rect = score_surface.get_rect( center=(400,330) )
        screen.blit(score_surface, score_rect)