import pygame, sys, random
from support import *
from pygame.locals import *



'''
This file is to setup all related functions the player (character)
''' 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, buidling_rects, display_surface, starting_balance=1500):
        super().__init__(group)
        
        self.import_assets() # for self.animations in the following lines
        self.status = 'down_idle'
        self.frame_index = 0
        self.buidling_rects = buidling_rects

        # general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.copy().inflate((-126,-70))
        
        # movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

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
        self.font = pygame.font.Font(None, 36)
        self.quantity_input = ""  # Add this line to initialize quantity_input

    def import_assets(self):
        self.animations = {'up': [], 'up_idle': [], 'down': [], 'down_idle': [], 'left': [], 'left_idle': [],
                           'right': [], 'right_idle': []}

        # load animations images
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(f'graphics/character/{animation}')

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
        if keys[pygame.K_s]:
            posX, posY = self.pos
            posX, posY = int(posX), int(posY)
            if 325 >= posX >= 115 and 250 >= posY >= 200:
                self.in_stock_building = True
                self.show_stock_menu = True
            elif 780 >= posX >= 530 and 250 >= posY >= 200:  # Check if the player is near Real Estate building
                print("Real Estate Area")
            elif 1220 >= posX >= 960 and 250 >= posY >= 200:  ##Check if the player is near Casino building
                print("Casino Area")
            elif 400 >= posX >= 250 and 680 >= posY >= 630:  # Check if the player is near Bank building
                print("Bank Area")
            elif 1200 >= posX >= 980 and 700 >= posY >= 630:  # Check if the player is near Lottery building
                print("Lottery Area")

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

        # Display stock price and description for the selected stock
        if self.selected_stock:
            stock_name = self.selected_stock
            stock_type = self.stock_types[stock_name]['type']
            stock_description = self.stock_types[stock_name]['description']
            price_text = f"Stock Type: {stock_type}\nDescription: {stock_description}"
            text_position = (menu_rect.left + 20, menu_rect.top + 20)
            self.draw_text(price_text, text_position)

        # Display stock options (1-5)
        options = [
            f"1. Buy CocaCola Stock ({self.stock_types['CocaCola (KO)']['type']})",
            f"2. Buy Apple Stock ({self.stock_types['Apple (AAPL)']['type']})",
            f"3. Buy SPY Stock ({self.stock_types['SPDR S&P 500 ETF Trust (SPY)']['type']})",
            f"4. Buy NEWP Stock ({self.stock_types['New Pacific Metals Corp (NEWP)']['type']})",
            f"5. Buy UNH Stock ({self.stock_types['UnitedHealth Group Inc (UNH)']['type']})"
        ]

        for i, option in enumerate(options):
            text_position = (menu_rect.left + 20, menu_rect.top + 100 + i * 40)
            self.draw_text(option, text_position)

        # Display purchase options
        purchase_options = [
            "6. Buy",
            "7. Exit"
        ]

        for i, option in enumerate(purchase_options):
            text_position = (menu_rect.left + 20, menu_rect.top + 300 + i * 40)
            self.draw_text(option, text_position)

    #handles the stock menu input
    def handle_stock_menu_input(self):
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # Check if a number key (1-5) is pressed to select a stock
                if K_1 <= event.key <= K_5:
                    stock_index = event.key - K_1
                    stocks = list(self.stock_types.keys())
                    self.selected_stock = stocks[stock_index]
                elif event.key == K_6:
                    self.show_purchase_prompt = True
                elif event.key == K_7:
                    self.show_stock_menu = False
                elif event.key == K_RETURN:
                    if self.show_purchase_prompt:
                        # Buy the selected stock when Enter is pressed
                        self.buy_stock(self.selected_stock)
                        self.show_purchase_prompt = False


    def display_stock_prices(self):
        for i, (stock_name, characteristics) in enumerate(self.stock_prices.items()):
            current_price = characteristics['current_price']
            text = f"{stock_name}: ${current_price}"

            # Display stock prices on the screen for each stock
            text_position = (10, 10 + i * 20)
            self.draw_text(text, text_position)

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

    def update_stock_prices(self):
        for stock_name, characteristics in self.stock_prices.items():
            initial_price = characteristics['initial_price']
            fluctuation_range = characteristics['fluctuation_range']

            fluctuation = random.uniform(*fluctuation_range)

            self.stock_prices[stock_name]['current_price'] = round(
                initial_price * (1 + fluctuation / 100), 2
            )

    def calculate_future_value(self, stock_name, stock_type, years, quantity):
        growth_rate = 0.0  # Default growth rate

        if stock_type == 'Dividend':
            # Dividends yield 3.5% of stock owned as income annually
            dividend_yield = 0.035
            annual_income = quantity * self.stock_prices[stock_name]['current_price'] * dividend_yield
            future_value = quantity * (1 + growth_rate) ** years + annual_income
        elif stock_type == 'Growth':
            # Growth stocks grow fast (15%) a year but may have a huge dump in the case of a recession
            growth_rate = 0.15
            if random.random() < 0.1:  # 10% chance of a huge dump
                growth_rate -= 0.45  # Reduce growth rate by 45% during a dump
            future_value = quantity * (1 + growth_rate) ** years
        elif stock_type == 'Penny Stock':
            # Penny stocks lose a lot of money (sort of a lottery type of stock)
            growth_rate = -0.2  # Placeholder, adjust as needed
            future_value = quantity * (1 + growth_rate) ** years
        elif stock_type == 'Defensive':
            # Defensive stocks grow slow but often dont lose much value during economic downturn
            growth_rate = 0.03
            future_value = quantity * (1 + growth_rate) ** years
        elif stock_type == 'ETF':
            # ETFs grow about 10% over long periods of time
            growth_rate = 0.10
            future_value = quantity * (1 + growth_rate) ** years
        else:
            # Default growth for unknown stock types
            future_value = quantity * (1 + growth_rate) ** years

        return round(future_value, 2)

    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, (255, 255, 255))
        self.display_surface.blit(text_surface, position)

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

    def update(self, dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)
