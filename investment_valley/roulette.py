# roulette.py

import random
import pygame
from pygame.locals import QUIT

def get_player_choice(display_surface, prompt):
    font = pygame.font.Font(None, 36)
    input_text = ""
    input_rect_choice = pygame.Rect(10, display_surface.get_height() // 2, 300, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text_surface = font.render(prompt, True, (255, 255, 255))
    width = max(200, text_surface.get_width() + 10)
    input_rect_choice.w = width
    cursor = pygame.Rect(input_rect_choice.topright, (3, input_rect_choice.height))
    input_active = True

    while input_active:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_choice.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    text_surface = font.render(input_text, True, color)
                    width = max(200, text_surface.get_width() + 10)
                    input_rect_choice.w = width
                    cursor.topleft = (input_rect_choice.topright[0], input_rect_choice.topright[1] + 2)
        pygame.draw.rect(display_surface, color, input_rect_choice, 2)
        display_surface.blit(text_surface, (input_rect_choice.x + 5, input_rect_choice.y + 5))
        if active:
            pygame.draw.rect(display_surface, color, cursor)
        pygame.display.flip()

    return input_text.strip().lower()

def get_player_bet(display_surface):
    font = pygame.font.Font(None, 36)
    input_text = ""
    input_rect_bet = pygame.Rect(10, display_surface.get_height() // 2 + 50, 300, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text_surface = font.render("Enter your bet amount: ", True, (255, 255, 255))
    width = max(200, text_surface.get_width() + 10)
    input_rect_bet.w = width
    cursor = pygame.Rect(input_rect_bet.topright, (3, input_rect_bet.height))
    input_active = True

    while input_active:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect_bet.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    text_surface = font.render(input_text, True, color)
                    width = max(200, text_surface.get_width() + 10)
                    input_rect_bet.w = width
                    cursor.topleft = (input_rect_bet.topright[0], input_rect_bet.topright[1] + 2)
        pygame.draw.rect(display_surface, color, input_rect_bet, 2)
        display_surface.blit(text_surface, (input_rect_bet.x + 5, input_rect_bet.y + 5))
        if active:
            pygame.draw.rect(display_surface, color, cursor)
        pygame.display.flip()

    return int(input_text.strip())

def spin_roulette_wheel():
    return random.randint(0, 36)

def determine_color(number):
    if number == 0:
        return "Green"
    elif number % 2 == 1:
        return "Red"
    else:
        return "Black"

def display_message(display_surface, message, color=(255, 255, 255)):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(display_surface.get_width() // 2, display_surface.get_height() // 2))
    display_surface.fill((0, 0, 0))
    display_surface.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

def display_roulette_result(level_instance, display_surface, result_number, result_color, user_choice, bet_amount):
    font = pygame.font.Font(None, 36)

    result_message = f"The result is {result_number} ({result_color})."
    user_message = f"You chose {user_choice} and bet {bet_amount}."

    text_surface_result = font.render(result_message, True, (255, 255, 255))
    text_surface_user = font.render(user_message, True, (255, 255, 255))

    text_rect_result = text_surface_result.get_rect(center=(display_surface.get_width() // 2, display_surface.get_height() // 2 - 30))
    text_rect_user = text_surface_user.get_rect(center=(display_surface.get_width() // 2, display_surface.get_height() // 2 + 30))

    display_surface.fill((0, 0, 0))
    display_surface.blit(text_surface_result, text_rect_result)
    display_surface.blit(text_surface_user, text_rect_user)
    pygame.display.flip()
    pygame.time.wait(2000)

    if user_choice.isdigit():  # Player bet on a number
        user_choice = int(user_choice)
        if user_choice == result_number:
            display_message(display_surface, "Congratulations! You guessed the number correctly!", (0, 255, 0))
            winnings = 35 * bet_amount
            level_instance.money += winnings
        else:
            display_message(display_surface, "Sorry, you didn't guess the number correctly. Better luck next time!", (255, 0, 0))
            level_instance.money -= bet_amount
    elif user_choice in ["red", "black"]:  # Player bet on a color
        if user_choice == result_color.lower():
            display_message(display_surface, "Congratulations! You guessed the color correctly!", (0, 255, 0))
            winnings = 2 * bet_amount
            level_instance.money += winnings
        else:
            display_message(display_surface, "Sorry, you didn't guess the color correctly. Better luck next time!", (255, 0, 0))
            level_instance.money -= bet_amount

def play_roulette_game(level_instance, display_surface):
    user_choice = get_player_choice(display_surface, "Choose a number (0-36) or a color (Red/Black): ")

    if user_choice.isdigit() or user_choice in ["red", "black"]:
        if level_instance.money <= 0:
            display_message(display_surface, "You don't have enough money to place a bet.", (255, 0, 0))
        else:
            bet_amount = get_player_bet(display_surface)
            display_message(display_surface, "Spinning the roulette wheel...", (255, 255, 255))

            result_number = spin_roulette_wheel()
            result_color = determine_color(result_number)

            display_roulette_result(level_instance, display_surface, result_number, result_color, user_choice, bet_amount)
    else:
        display_message(display_surface, "Invalid choice. Please choose a valid number or color.", (255, 0, 0))
