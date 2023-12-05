# lottery.py

import random
import pygame

def play_lottery(display_surface, balance, update_balance):
    ticket_cost = 50
    win_probability = 0.05 # winning probability for lottery should be low

    # Check if the player has enough balance to play
    if balance < ticket_cost:
        # Print message on the screen
        display_message(display_surface, "Insufficient balance to play.", 3000)
        return

    # Check if the player wins
    display_message(display_surface, f"Welcome to the lottery! Each round costs $50 to play.", 3000)
    winnings = random.randint(500, 2500)  # Generate random winnings between 500 and 2500
    if random.random() < win_probability:
        display_message(display_surface, f"Congratulations! You won ${winnings}! Your new balance is ${update_balance(winnings - ticket_cost)}.", 3000)
    else:
        display_message(display_surface, f"Sorry, you didn't win this time. Your balance is now ${update_balance(ticket_cost * -1)}.", 3000)


def display_message(display_surface, message, wait):
    # Display a message on the screen
    font = pygame.font.Font(None, 36)

    # Create a surface for the text
    text_surface = font.render(message, True, (255, 255, 255))
    
    # Create a surface for the rectangle
    rect_surface = pygame.Surface((text_surface.get_width() + 20, text_surface.get_height() + 20))
    rect_surface.set_alpha(128)  # Set alpha for opacity
    rect_surface.fill((128, 128, 128))  # Fill with grey 

    # Get the rectangle and text positions
    rect_position = (display_surface.get_width() // 2 - rect_surface.get_width() // 2, display_surface.get_height() // 2 - rect_surface.get_height() // 2)
    text_position = (rect_position[0] + 10, rect_position[1] + 10)

    # Draw the rectangle and text on the display surface
    display_surface.blit(rect_surface, rect_position)
    display_surface.blit(text_surface, text_position)

    pygame.display.flip()
    pygame.time.wait(wait)  # Display the message for 3 seconds
    display_surface.fill((0, 0, 0))
    pygame.display.flip()
