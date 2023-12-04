# lottery.py

import random
import pygame

def play_lottery(level_instance, balance):
    ticket_cost = 50
    win_probability = 0.05

    # Set a default value for balance if it is None
    if balance is None:
        balance = level_instance.money  # Use the balance from the Level instance

    # Check if the player has enough balance to play
    if balance < ticket_cost:
        # Print message on the screen
        display_message(level_instance, "Insufficient balance to play.")
        return balance

    # Deduct ticket cost from the balance
    balance -= ticket_cost

    # Check if the player wins
    if random.random() < win_probability:
        # Generate random winnings between 500 and 2500
        winnings = random.randint(500, 2500)
        balance += winnings
        # Print winning message on the screen
        display_message(level_instance, f"Congratulations! You won {winnings}! Your new balance is {balance}.")
    else:
        # Print losing message on the screen
        display_message(level_instance, f"Sorry, you didn't win this time. Your balance is now {balance}.")

    # Update the balance in the Level instance
    level_instance.money = balance

    # print("After lottery, balance:", balance)

def display_message(level_instance, message):
    # Display a message on the screen
    font = pygame.font.Font(None, 36)

    # Create a surface for the text
    text_surface = font.render(message, True, (255, 255, 255))
    
    # Create a surface for the rectangle
    rect_surface = pygame.Surface((text_surface.get_width() + 20, text_surface.get_height() + 20))
    rect_surface.set_alpha(128)  # Set alpha for opacity
    rect_surface.fill((128, 128, 128))  # Fill with grey 

    # Get the rectangle and text positions
    rect_position = (level_instance.display_surface.get_width() // 2 - rect_surface.get_width() // 2, level_instance.display_surface.get_height() // 2 - rect_surface.get_height() // 2)
    text_position = (rect_position[0] + 10, rect_position[1] + 10)

    # Draw the rectangle and text on the display surface
    level_instance.display_surface.blit(rect_surface, rect_position)
    level_instance.display_surface.blit(text_surface, text_position)

    pygame.display.flip()
    pygame.time.wait(750)  # Display the message for 750 ms




