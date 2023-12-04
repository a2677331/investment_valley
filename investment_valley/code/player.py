import pygame, sys, random
from support import *
from pygame.locals import *
import textwrap
import os



'''
This file is to setup all related functions the player (character)
''' 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, buidling_rects, display_surface, earn_money, starting_balance=1500):
        super().__init__(group)
        
        self.import_assets() # for self.animations in the following lines
        self.status = 'down_idle'
        self.frame_index = 0
        self.buidling_rects = buidling_rects

        # attributes for purchase flow
        self.show_purchase_prompt = False
        self.selected_stock = None
        self.input_active = False
        self.quantity_input = ""

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.copy().inflate((-126,-70))
        
        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
        # update money
        self.earn_money = earn_money

        # financial attributes
        self.in_stock_building = False
        self.show_purchase_prompt = False
        self.money = starting_balance

        self.stocks_owned = {
            'CocaCola (KO)': 0,
            'Apple (AAPL)': 0,
            'SPDR S&P 500 ETF Trust (SPY)': 0,
            'New Pacific Metals Corp (NEWP)': 0,
            'UnitedHealth Group Inc (UNH)': 0
        }

        # the different stock types the player can choose from/description of each
        self.stock_types = {
            'CocaCola (KO)': {'type': 'Dividend',
                              'description': 'Stocks that regularly share profits with shareholders. Dividend stocks tend to be a very good choice for long term growth, as they pay the shareholder an income on top of the stake owned in the company.'},
            'Apple (AAPL)': {'type': 'Growth',
                             'description': 'Stocks that tend to grow faster than their counterparts. However, in economic downturns, these stocks can perform very poorly, as these downturns cause questions regarding companies\' future growth.'},
            'SPDR S&P 500 ETF Trust (SPY)': {'type': 'ETF',
                                             'description': 'A collection of securities that track an underlying index. For example, SPY tracks the S&P 500 (Top 500 stocks on the market by market cap). ETFs are beneficial because they are low cost and allow for diversification. The downsides are the fees that sometimes come with the purchase of these ETFs.'},
            'New Pacific Metals Corp (NEWP)': {'type': 'Penny Stock',
                                               'description': 'Stocks that are usually less than $5 per share. These tend to be like playing the lottery. Sometimes people will hit it big, but other than that, they are a very risky investment.'},
            'UnitedHealth Group Inc (UNH)': {'type': 'Defensive',
                                             'description': 'Stocks that have very minimal risk and are generally safer investments. These stocks tend to grow way slower than growth stocks, but in times of economic downturn, they are a great way to keep capital safer.'},
        }

        # initial stock prices
        self.stock_prices = {
            'CocaCola (KO)': {'initial_price': 58, 'fluctuation_range': (1, 3), 'current_price': 58},
            'Apple (AAPL)': {'initial_price': 190, 'fluctuation_range': (5, 10), 'current_price': 190},
            'SPDR S&P 500 ETF Trust (SPY)': {'initial_price': 455, 'fluctuation_range': (3, 8), 'current_price': 455},
            'New Pacific Metals Corp (NEWP)': {'initial_price': 2, 'fluctuation_range': (0.5, 2), 'current_price': 2},
            'UnitedHealth Group Inc (UNH)': {'initial_price': 546, 'fluctuation_range': (2, 5), 'current_price': 546},
        }

        # rendering-related attrributes
        self.display_surface = display_surface
        self.show_stock_menu = False
        self.show_bank_menu = False
        self.in_bank_menu = False
        self.font = pygame.font.Font(None, 36)
        self.quantity_input = ""  # Add this line to initialize quantity_input

    def import_assets(self):
        current_file_path = os.path.abspath(__file__)
        grandparent_file_path = os.path.dirname(os.path.dirname(current_file_path))

        self.animations = {'up': [], 'up_idle': [], 'down': [], 'down_idle': [], 'left': [], 'left_idle': [],
                           'right': [], 'right_idle': []}

        # load animations images
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(f'{grandparent_file_path}/graphics/character/{animation}')
        
    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        # Directions control using arrow keys
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

        # When the player presses enter, this code check to see if they are near a building
        '''
        NOTE: the print statements are place holders for when we decide what to 
        do when the player interacts with a bulding
        '''
        posX, posY = self.pos
        posX, posY = int(posX), int(posY)
            
        if keys[pygame.K_RETURN]:

            if 325 >= posX >= 115 and 250 >= posY >= 200:
                self.in_stock_building = True
                self.show_stock_menu = True
            elif 780 >= posX >= 530 and 250 >= posY >= 200:  # Check if the player is near Real Estate building
                print("Real Estate Area")
            elif 1220 >= posX >= 960 and 250 >= posY >= 200:  ##Check if the player is near Casino building
                print("Casino Area")
            elif 400 >= posX >= 250 and 680 >= posY >= 630:  # Check if the player is near Bank building
                self.in_bank_menu = True
                self.show_bank_menu = True
            elif 1200 >= posX >= 980 and 700 >= posY >= 630:  # Check if the player is near Lottery building
                print("Lottery Area")

        if keys[pygame.K_ESCAPE]:
            if 325 >= posX >= 115 and 250 >= posY >= 200 and self.in_stock_building and self.show_stock_menu:
                self.in_stock_building = False
                self.show_stock_menu = False
            elif self.in_bank_menu:
                self.in_bank_menu = False
                self.show_bank_menu = False

    def get_status(self):
        # set status for idle animation
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

    def move(self, dt):
        # make diagonal movement same speed as straight directions
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collision('horizontal')

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collision('vertical')

    def collision(self, direction):
        # Collision detected, stop the player movement
        for building_rect in self.buidling_rects:
            if self.hitbox.colliderect(building_rect):
                if direction == "horizontal":
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = building_rect.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = building_rect.right
                    self.rect.centerx = self.hitbox.centerx
                    self.pos.x = self.hitbox.centerx

            if self.hitbox.colliderect(building_rect):
                if direction == "vertical":
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = building_rect.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = building_rect.bottom
                    self.rect.centery = self.hitbox.centery
                    self.pos.y = self.hitbox.centery


    def stock_menu(self):
        menu_rect = pygame.Rect(400, 200, 480, 400)
        pygame.draw.rect(self.display_surface, (0, 0, 0), menu_rect)
        pygame.draw.rect(self.display_surface, (255, 255, 255), menu_rect, 2)


        if self.selected_stock:
            stock_type = self.stock_types.get(self.selected_stock, {}).get('type', 'Unknown')
            stock_description = self.stock_types.get(self.selected_stock, {}).get('description', 'No description available')

            # Display stock type and description
            text_position = (menu_rect.left + 20, menu_rect.top + 20)
            self.draw_text(f"Stock Type: {stock_type}", text_position)
            text_position = (menu_rect.left + 20, menu_rect.top + 60)
            self.draw_text(f"Description:", text_position)
            text_position = (menu_rect.left + 20, menu_rect.top + 100)
            self.draw_text_multiline(stock_description, text_position, max_width=440, line_height=30)

            # Display buy option and handle input
            buy_option = "Press 'B' to Buy"
            text_position = (menu_rect.left + 20, menu_rect.bottom - 50)
            self.draw_text(buy_option, text_position)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_b]:
                self.handle_buy_input()

        else:
            # Display stock prices directly above the stock options
            stock_prices = self.get_stock_prices_text()
            prices_text_position = (menu_rect.left + 20, menu_rect.top + 20)
            self.draw_text_multiline(stock_prices, prices_text_position, max_width=440, line_height=30)

            # Display stock options
            options = [
                "1. Buy CocaCola Stock (Dividend)",
                "2. Buy Apple Stock (Growth)",
                "3. Buy SPY Stock (ETF)",
                "4. Buy NEWP Stock (Penny Stock)",
                "5. Buy UNH Stock (Defensive)",
                "0. Exit Stock Menu"
            ]

            for i, option in enumerate(options):
                text_position = (menu_rect.left + 20, menu_rect.top + 150 + i * 30)
                self.draw_text(option, text_position, font_size=18)


    def get_stock_prices_text(self):
        if self.stock_prices is None:
            return ""
        
        prices_text = ""
        for stock_name, characteristics in self.stock_prices.items():
            current_price = characteristics['current_price']
            stock_line = f"{stock_name}: ${current_price}"
            prices_text += stock_line + "\n"

        return prices_text

    def display_prices(self):
        prices_text = ""
        for stock_name, characteristics in self.stock_prices.items():
            current_price = characteristics['current_price']
            prices_text += f"{stock_name}: ${current_price}\n"

        # Check if prices_text is not empty before displaying
        if prices_text:
            # Display stock prices on the screen above the options
            menu_rect = pygame.Rect(400, 200, 480, 400)
            text_position = (menu_rect.left + 20, menu_rect.top + 120)
            self.draw_text_multiline(prices_text, text_position, max_width=440, line_height=20)
    
    def draw_text_multiline(self, text, position, max_width, line_height=30):
        font = pygame.font.Font(None, 24)  # Adjust the font size if needed
        words = text.split(' ')
        lines = []
        current_line = ''

        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '

        lines.append(current_line)

        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (255, 255, 255))
            self.display_surface.blit(text_surface, (position[0], position[1] + i * line_height))

    def handle_stock_menu_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5):
                    stock_options = {
                        pygame.K_1: 'CocaCola (KO)',
                        pygame.K_2: 'Apple (AAPL)',
                        pygame.K_3: 'SPDR S&P 500 ETF Trust (SPY)',
                        pygame.K_4: 'New Pacific Metals Corp (NEWP)',
                        pygame.K_5: 'UnitedHealth Group Inc (UNH)',
                    }
                    self.selected_stock = stock_options[event.key]
                    # Clear the menu and display purchase prompt
                    self.clear_menu()
                    self.show_purchase_prompt = True
                elif event.key == pygame.K_0:
                    self.close_stock_menu()
                    return  # Add return to exit the method and prevent further processing
                elif event.key == pygame.K_b:
                    # Clear the stock menu
                    self.clear_menu()
                    # Display purchase prompt
                    self.show_purchase_prompt = True

        # Handle quantity input
        if self.input_active and self.show_purchase_prompt:
            self.get_numeric_input()
        # Ensure that the menu is not redrawn in the next iteration
        if self.show_stock_menu or self.show_purchase_prompt:
            return

    def close_stock_menu(self):
        self.clear_menu()
        self.show_stock_menu = False
        self.show_purchase_prompt = False
        self.input_active = False
        self.selected_stock = None


    def show_stock_details(self, stock_name):
        self.selected_stock = stock_name
        stock_type = self.stock_types[stock_name]['type']
        stock_description = self.stock_types[stock_name]['description']

        print(f"Stock Type: {stock_type}")
        print(f"Description: {stock_description}")

        self.show_purchase_options(stock_name)


    def buy_stock(self, stock_name):
        stock_type = self.stock_types[stock_name]['type']
        stock_description = self.stock_types[stock_name]['description']

        print(f"Stock Type: {stock_type}")
        print(f"Description: {stock_description}")

        quantity = int(input("Enter the quantity of stocks to purchase: "))

        # Use the fluctuation range to determine the number of years to hold
        fluctuation_range = self.stock_prices[stock_name]['fluctuation_range']
        years_to_hold = random.uniform(*fluctuation_range)

        # Get the current stock price from the data
        stock_price = self.stock_prices[stock_name]['current_price']

        future_value = self.calculate_future_value(stock_type, years_to_hold, quantity)
        print(f"Future Value after {years_to_hold:.2f} years: ${future_value}")

        total_cost = stock_price * quantity
        if self.money >= total_cost:
            self.money -= total_cost
            self.stocks_owned[stock_name] += quantity
        else:
            print("Insufficient funds!")

    def handle_buy_input(self):
        # Display the performance message for the selected stock
        stock_name = self.selected_stock
        self.display_stock_performance(stock_name)

        # Reset selected_stock to None
        self.selected_stock = None

    def display_stock_performance(self, stock_name):
        # Clear the menu
        self.clear_menu()

        if stock_name == 'CocaCola (KO)':
            message = "Congratulations! Your earned $81!"
            self.earn_money(81)
        elif stock_name == 'Apple (AAPL)':
            message = "OMG! Apple has performed terribly bad. Your lost $500!"
            self.earn_money(-500)
        elif stock_name == 'SPDR S&P 500 ETF Trust (SPY)':
            message = "Great choice! SPY, being an ETF, has provided steady growth of 10% over the last 5 years. You earned $661."
            self.earn_money(661)
        elif stock_name == 'New Pacific Metals Corp (NEWP)':
            message = "It's a gamble! NEWP, being a penny stock, has shown volatility. You lost $1000!"
            self.earn_money(-1000)
        elif stock_name == 'UnitedHealth Group Inc (UNH)':
            message = "Steady and safe! UNH, being a defensive stock. You earned $1."
            self.earn_money(1)
        else:
            message = "Unknown stock selected."

        # Display the message on the game surface
        text_position = (400, 250)  # Adjust the position as needed
        max_width = 400
        self.draw_text_multiline(message, text_position, max_width=max_width)

        # Update the game display
        pygame.display.flip()
        pygame.time.wait(10000)  # Wait for 5000 milliseconds (5 seconds)


    def update_stock_prices(self):
        for stock_name, characteristics in self.stock_prices.items():
            initial_price = characteristics['initial_price']
            fluctuation_range = characteristics['fluctuation_range']

            fluctuation = random.uniform(*fluctuation_range)

            self.stock_prices[stock_name]['current_price'] = round(
                initial_price * (1 + fluctuation / 100), 2
            )

    def draw_text(self, text, position, font_size=None):
        if font_size is not None:
            font = pygame.font.Font(None, font_size)
        else:
            font = self.font
        
        text_surface = font.render(text, True, (255, 255, 255))
        self.display_surface.blit(text_surface, position)



    def clear_menu(self):
        # Clear the menu by drawing a filled rectangle over it
        menu_rect = pygame.Rect(400, 200, 480, 400)
        pygame.draw.rect(self.display_surface, (0, 0, 0), menu_rect)

    def display_purchase_prompt(self):
        purchase_rect = pygame.Rect(400, 200, 480, 400)
        pygame.draw.rect(self.display_surface, (0, 0, 0), purchase_rect)
        pygame.draw.rect(self.display_surface, (255, 255, 255), purchase_rect, 2)

        stock_name = self.selected_stock
        stock_type = self.stock_types[stock_name]['type']
        stock_description = self.stock_types[stock_name]['description']

        prompt_text = f"Stock Type: {stock_type}\nDescription: {stock_description}"
        quantity_prompt = "Enter the quantity of stocks to purchase:"

        text_position = (purchase_rect.left + 20, purchase_rect.top + 20)
        self.draw_text(prompt_text, text_position)

        text_position = (purchase_rect.left + 20, purchase_rect.top + 100)
        self.draw_text(quantity_prompt, text_position)

        text_position = (purchase_rect.left + 20, purchase_rect.top + 140)
        self.draw_text(self.quantity_input, text_position)

    def bank_menu(self):
        bank_menu_font = pygame.font.Font('../font/LycheeSoda.ttf',100)
        menu_image = pygame.image.load('../graphics/world/BankMenu.png')
        self.display_surface.blit(menu_image,(100,50))
        balance_image = bank_menu_font.render("$"+str(self.money), True, (0,0,0))
        self.display_surface.blit(balance_image, (470,600))

    def update(self, dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)
