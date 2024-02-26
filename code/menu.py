import pygame
from settings import *
from support import *
from data import *
import random


class Menu:

    def __init__(self, player, toggle_building, modify_money_by):
        pygame.init()
        pygame.mixer.init() # for music effect
        
        # general setup
        self.player = player
        self.toggle_building = toggle_building
        self.display_surface = pygame.display.get_surface()
        self.title_font = pygame.font.Font(f'{grandparent_file_path}/font/LycheeSoda.ttf', 50) # font for the title
        self.dialog_font = pygame.font.Font(None, 30)  # font for the dialog text
        self.player_luck = random.random()              # random number range from 0 to 1 for luck
        
        # menu options
        _, self.title_height = self.title_font.size('title sample text') # get the title text's height
        _, self.dialog_height = self.dialog_font.size('dialog sample text') # get the title text's height
        self.padding = 10
        self.menu_width = SCREEN_WIDTH / 2 # menu window width
        self.menu_height = SCREEN_HEIGHT / 2 + self.title_height + self.padding * 2  # menu window height

        # user inputs
        self.pressed_b = False
        self.pressed_1 = False
        self.pressed_2 = False
        self.pressed_3 = False
        self.pressed_4 = False
        self.pressed_5 = False
        
        # money balance setup
        self.modify_money_by = modify_money_by  # update money of the player
        self.current_balance = self.modify_money_by()
        self.money_updated = False #  a flag to update player's moeny, Important! Using a flag to update moeny that can avoid updating it multiple times!

        # stock estate setup
        self.stock_win_possibility = None
        
        # real estate setup 
        self.estate_win_possibility = None
        
        # casino setup
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)
        self.dice3 = random.randint(1, 6)
        self.casino_dices_sum = self.dice1 + self.dice2 + self.dice3
        self.casino_bet = 50

        # lottery setup
        self.lottery_win_probability = 0.14
        self.lottery_winnings = random.randint(500, 2500)  # Generate random winnings between 500 and 2500
        self.lottery_bet = 50

        # sound effects
        self.sound_played = False # flag to indicate if the sound has been played
        self.win_sound = pygame.mixer.Sound(f'{grandparent_file_path}/audio/win.mp3') # winning sound
        self.lose_sound = pygame.mixer.Sound(f'{grandparent_file_path}/audio/lose.mp3')  # lose sound
        self.win_sound.set_volume(0.2)
        self.lose_sound.set_volume(0.8)
    
    # Generate wrapped text within the max width limit, output a list of wrapped text.
    def wrap_text(self, text, max_width, line_change_symbol="${linechange}$"):
        words = text.split()
        lines = []  # the lines of text to output within max width limit
        current_line = words[0] # the current line of text within the max width limit
        
        for word in words[1:]:
            text_line = current_line + " " + word
            text_line_width, _ = self.dialog_font.size(text_line)
            
            if word == line_change_symbol: # change to next line if meets line change symbol
                lines.append(current_line)
                current_line = ""
            elif text_line_width <= max_width: # if text width less than width limit
                current_line = text_line
            else:
                lines.append(current_line)
                current_line = word
                
        lines.append(current_line)          # don't forget the last current_line that is not yet added
        lines = [s.lstrip() for s in lines] # trim left unnecessary space for each line
        return lines

    
    def draw_wrapped_text(self, font_style, text, rect):
        lines = self.wrap_text(text, rect.width-7*self.padding) # get wrapped text within the max width limit
        y = rect.y + self.padding # the starting vertical position plus padding
        
        for line in lines:
            if font_style == "dialog style":
                text_surface = self.dialog_font.render(line, True, 'black') # Render black text
                title_height = y + self.title_height + self.padding*2  # give vertical space for title, so dialog text
                text_rect = text_surface.get_rect(x=rect.x+self.padding*4, y=title_height)   # create a rectangle around the text surface
            elif font_style == "title style":
                text_surface = self.title_font.render(line, True, "black")
                text_rect = text_surface.get_rect(x=rect.x+self.padding, y=rect.top+self.padding)   # y: the starting vertical position plus padding
                text_rect.centerx = rect.centerx # Draw the title text surface centered on the rectangle
            elif font_style == "title style bottom":
                text_surface = self.title_font.render(line, True, "black")
                text_rect = text_surface.get_rect(x=rect.x+self.padding, y=rect.bottom-self.padding*6)   # Create a rectangle around the text surface
                text_rect.centerx = rect.centerx # Draw the title text surface centered on the rectangle
            else:
                print("ERROR: unkonwn text type, stop running")
                return
            
            self.display_surface.blit(text_surface, text_rect)
            y += text_rect.height + self.padding

    def draw_menu(self, title_text, content_text, title_after_dialog=None):
        # Define the menu surface as black color with white border
        menu_rect = pygame.Rect((SCREEN_WIDTH-self.menu_width)/2, (SCREEN_HEIGHT-self.menu_height)/2, self.menu_width, self.menu_height) # center the menu window, and setup menu height and width
        pygame.draw.rect(self.display_surface, 'white', menu_rect, 0, 4)  # fill the rectangle with color
        pygame.draw.rect(self.display_surface, 'black', menu_rect, 4, 4)  # draw the bordered on rectangle

        # draw intro text on menu window
        self.draw_wrapped_text("title style", title_text, menu_rect)            # draw title text
        self.draw_wrapped_text("dialog style", content_text, menu_rect)         # draw dialog text
        if title_after_dialog:
            self.draw_wrapped_text("title style bottom", title_after_dialog, menu_rect)         # draw dialog text
            
    def adjust_balance(self, value):
        """ 
        Function to use a flag to update player's moeny, 
        Important! Using a flag to update moeny that can avoid updating it multiple times!
        """
        if not self.money_updated: # if money not yet updated
            # update the moeny, and reset the flag
            self.modify_money_by(value)
            self.money_updated = True
    
    def play_sound(self, sound):
        if not self.sound_played: # if money not yet updated
            # update the moeny, and reset the flag
            sound.play()
            self.sound_played = True
    
    def draw_intro_menu(self, building, option=None):
        if option is None:
            # draw an intro menu
            self.draw_menu(building["intro menu"]["name"], building["intro menu"]["content"])
        else:
            # show option menu when user presses option in the intro menu
            self.draw_menu(building[option]["name"], building[option]["content"], building[option]["next option"])
    
    def process_casino_menu(self, condition, option, bet, gain):
        content = CASINO["content"].replace("[dice1]", str(self.dice1)).replace("[dice2]", str(self.dice2)).replace("[dice3]", str(self.dice3))

        if condition: # lose if even result
            result = CASINO[option]["result_good"]
            result = result.replace("[total]", str(self.dice1 + self.dice2 + self.dice3)).replace("[?]", str(gain))
            sound = self.win_sound
            bet_to_adjust = gain
        else:
            result = CASINO[option]["result_bad"]
            result = result.replace("[total]", str(self.dice1 + self.dice2 + self.dice3)).replace("[?]", str(bet))
            sound = self.lose_sound
            bet_to_adjust = bet * -1

        self.adjust_balance(bet_to_adjust)
        self.draw_menu(CASINO["title"], content+result, "Press ESC to exit")
        self.play_sound(sound)
    
    def process_lottery_menu(self, option):
        if self.player_luck < self.lottery_win_probability: # lose if even result
            sound = self.win_sound
            balance_to_adjust = self.lottery_winnings
            result = LOTTERY[option]["result_good"].replace("[gain]", str(self.lottery_winnings)).replace("[?]", str(self.current_balance + balance_to_adjust))
        else:
            sound = self.lose_sound
            balance_to_adjust =  self.lottery_bet * -1
            result = LOTTERY[option]["result_bad"].replace("[?]", str(self.current_balance + balance_to_adjust))

        self.adjust_balance(balance_to_adjust)
        self.draw_menu(LOTTERY["title"], result, "Press ESC to exit")
        self.play_sound(sound)
        
        
    # process user input in the menu
    def process_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:   # control open and close menu
            self.toggle_building()
        elif keys[pygame.K_1] and not (self.pressed_2 or self.pressed_3 or self.pressed_4 or self.pressed_5):
            self.pressed_1 = True
        elif keys[pygame.K_2] and not (self.pressed_1 or self.pressed_3 or self.pressed_4 or self.pressed_5):
            self.pressed_2 = True
        elif keys[pygame.K_3] and not (self.pressed_1 or self.pressed_2 or self.pressed_4 or self.pressed_5):
            self.pressed_3 = True
        elif keys[pygame.K_4] and not (self.pressed_1 or self.pressed_2 or self.pressed_3 or self.pressed_5):
            self.pressed_4 = True
        elif keys[pygame.K_5] and not (self.pressed_1 or self.pressed_2 or self.pressed_3 or self.pressed_4):
            self.pressed_5 = True


    def process_menu_of(self, building, option, win_prosibility):
        # response to buy action (pressing the 'B' key) under the buy menu
        keys = pygame.key.get_pressed()
        if keys[pygame.K_b]:
            self.pressed_b = True
        
        if self.pressed_b:
            if self.player_luck <= win_prosibility:
                profit = round(self.current_balance * building[option]["profit_ratio"])
                good_description = building[option]["result_good"].replace("[?]", str(round(self.current_balance * building[option]["profit_ratio"])))
                self.play_sound(self.win_sound)
                self.adjust_balance(round(self.current_balance * building[option]["profit_ratio"]))                        # increase balance
                self.draw_menu(building[option]["name"], good_description, f"Your earned ${profit}.") # draw the result menu
            else:
                lost = round(self.current_balance * building[option]["lose_ratio"])
                bad_description = building[option]["result_bad"].replace("[?]", str(lost))
                self.play_sound(self.lose_sound)
                self.adjust_balance(lost * -1)                        # increase balance
                self.draw_menu(building[option]["name"], bad_description, f"Your lost ${lost}.") # draw the result menu


    def show_menu(self, building_name):
        option = None # which menu option from the intro menu
        
        # STOCK
        if building_name == STOCK["intro menu"]["name"] and option is None:
            self.draw_intro_menu(STOCK)
            # response to '1~5' keys pressed, under the beginning menu
            if self.pressed_1:
                option = "option 1" # CocaCola stock
                self.stock_win_possibility = 0.52
            elif self.pressed_2:
                option = "option 2" # Apple Stock
                self.stock_win_possibility = 0.53
            elif self.pressed_3:
                option = "option 3" # SPDR 500
                self.stock_win_possibility = 0.54
            elif self.pressed_4:
                option = "option 4" # penny stock
                self.stock_win_possibility = 0.3
            elif self.pressed_5:
                option = "option 5" # defensive stock
                self.stock_win_possibility = 0.51
            self.draw_intro_menu(STOCK, option) # draw correspoinding menu
            self.process_menu_of(STOCK, option, self.stock_win_possibility)
                      
                       
        # REAL-ESTATE
        elif building_name == REAL_ESTATE["intro menu"]["name"] and option is None:
            self.draw_intro_menu(REAL_ESTATE)
            # response to '1~5' keys pressed, under the beginning menu
            if self.pressed_1:
                option = "option 1"
                self.estate_win_possibility = 0.55
            elif self.pressed_2:
                option = "option 2"
                self.estate_win_possibility = 0.57
            elif self.pressed_3:
                option = "option 3"
                self.estate_win_possibility = 0.40
            elif self.pressed_4:
                option = "option 4"
                self.estate_win_possibility = 0.51
            elif self.pressed_5:
                option = "option 5"
                self.estate_win_possibility = 0.30
            self.draw_intro_menu(REAL_ESTATE, option) # draw correspoinding menu
            self.process_menu_of(REAL_ESTATE, option, self.estate_win_possibility)
        
        
        # CASINO
        elif building_name == CASINO["intro menu"]["name"] and option is None:
            self.draw_intro_menu(CASINO)
            
            # response to '1~5' keys pressed, under the beginning menu
            if self.pressed_1:
                option = "option 1"
                win_condition = self.casino_dices_sum % 2 == 0
                gain = self.casino_bet
                self.process_casino_menu(win_condition, option, self.casino_bet, gain)
            elif self.pressed_2:
                option = "option 2"
                win_condition = self.casino_dices_sum % 2 != 0
                gain = self.casino_bet
                self.process_casino_menu(win_condition, option, self.casino_bet, gain)
            elif self.pressed_3:
                option = "option 3"
                win_condition = self.dice1 + self.dice2 + self.dice3 > 9
                gain = self.casino_bet * 2
                self.process_casino_menu(win_condition, option, self.casino_bet, gain)                
            elif self.pressed_4:
                option = "option 4"
                win_condition = self.dice1 + self.dice2 + self.dice3 <= 9
                gain = self.casino_bet * 2
                self.process_casino_menu(win_condition, option, self.casino_bet, gain)          
            elif self.pressed_5:
                option = "option 5"
                win_condition = self.dice1 + self.dice2 + self.dice3 == 18
                gain = self.casino_bet * 2
                self.process_casino_menu(win_condition, option, self.casino_bet, gain)
                
                
        # LOTTERY
        elif building_name == LOTTERY["intro menu"]["name"] and option is None:
            self.draw_intro_menu(LOTTERY)

            # response to '1~5' keys pressed, under the beginning menu
            if self.pressed_1:
                option = "option 1"
                self.process_lottery_menu(option)
            else:
                # reset unwantted keys pressed
                self.pressed_2 = False
                self.pressed_3 = False
                self.pressed_4 = False
                self.pressed_5 = False
                

    def update(self, building_name):
        self.process_input()
        self.show_menu(building_name)