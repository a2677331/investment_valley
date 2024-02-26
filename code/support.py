import pygame
from settings import *

'''
This file is to provide supporting functions for all the other files.
'''


# background music
def load_background_music(music_file, volume):
    pygame.mixer.music.load(f'{grandparent_file_path}/audio/{music_file}')
    pygame.mixer.music.set_volume(volume) # set volume
    return pygame.mixer.music

# To import image files and output a list of surfaces converted from images files for for character animations.
# used in player.py
def import_folder(path):
    surface_list = []
    for _, _, image_files in os.walk(path):
        for image in image_files:
            image_surface = pygame.image.load(f'{path}/{image}').convert_alpha()
            surface_list.append(image_surface)
    return surface_list

# Function to convert seconds to minutes
# used in function display_status_bar()
def seconds_to_minutes(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes)}:{int(seconds):02d}"

# To display status bar on the top screen, showing the money earned and time left
# used in level.py
def display_status_bar(screen, start_time, money):
    # display time left for each round of the game 
    text_font = pygame.font.Font(f'{grandparent_file_path}/font/LycheeSoda.ttf', 40)
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    seconds_left = 300 - current_time # set as 5 minutes time limit per round
    time_surface = text_font.render(f'Time Left: {seconds_to_minutes(seconds_left)}', False, (200,200,200)).convert()
    time_rect = time_surface.get_rect(center=(SCREEN_WIDTH/2,25))
    screen.blit(time_surface, time_rect)

    # display money earned by user
    money_surface = text_font.render(f'Money Earned: ${money}', False, (200,200,200)).convert()
    money_rect = time_surface.get_rect(center=(200,25))
    screen.blit(money_surface, money_rect)
    return seconds_left, money


# To display Intro screen
# show different screens before initial play and other play
# used in game.py
def draw_intro_screen(screen, score):
    
    # game title furface
    title_font = pygame.font.Font(f'{grandparent_file_path}/font/LycheeSoda.ttf', 130)
    game_title_surface = title_font.render("Investment Valley", False, "#2979b9").convert()
    game_title_rect = game_title_surface.get_rect(center = (SCREEN_WIDTH/2,180))
    
    # draw intro screen
    screen.fill("black")
    screen.blit(game_title_surface, game_title_rect)
    
    # game instruction text
    text_font = pygame.font.Font(f'{grandparent_file_path}/font/LycheeSoda.ttf', 50)
    
    # score surface
    if score:
        score_surface = text_font.render(f'Your last score: {score}', False, (111,196,169)).convert()
        score_rect = score_surface.get_rect( center=(1280/2,330) )
        screen.blit(score_surface, score_rect) # money score

    # Instruction surface 1
    instruction_surface = text_font.render("Press [Space] to start", False, ("white")).convert()
    instruction_rect = instruction_surface.get_rect(center = (1280/2,380))
    screen.blit(instruction_surface, instruction_rect) # retry instruction

    # Instruction surface 2
    text_font = pygame.font.Font(f'{grandparent_file_path}/font/LycheeSoda.ttf', 30)
    instruction_surface2 = text_font.render("Use [Arrow keys] to move character", False, ("grey")).convert()
    instruction_rect2 = instruction_surface2.get_rect(center = (1280/2,630))
    screen.blit(instruction_surface2, instruction_rect2)

    # Instruction surface 3
    instruction_surface3 = text_font.render("Press [Enter] to interact with buildings", False, ("grey")).convert()
    instruction_rect3 = instruction_surface3.get_rect(center = (1280/2-3,660))
    screen.blit(instruction_surface3, instruction_rect3)
    