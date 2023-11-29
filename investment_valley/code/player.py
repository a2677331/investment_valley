import pygame
from support import *

'''
This file is to setup all related functions the player (character)
''' 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, buidling_rects):
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

    def import_assets(self):
        self.animations = {'up': [], 'up_idle': [], 'down':[], 'down_idle': [], 'left':[], 'left_idle':[], 'right':[], 'right_idle':[],
                           'up_axe': []}

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

        #When the player presses enter, this code check to see if they are near a building
        '''
        NOTE: the print statements are place holders for when we decide what to 
        do when the player interacts with a bulding
        '''
        if keys[pygame.K_RETURN]:
            posX,posY=self.pos #Assigns the x and y of the players position to a variable
            posX,posY=int(posX),int(posY) #Typecasts the floats to ints so they can be compared
            if 325>=posX>=115 and 250>=posY>=200: #Check if the player is near Stock building
                print("Stock Area")
            elif 780>=posX>=530 and 250>=posY>=200: #Check if the player is near Real Estate building
                print("Real Estate Area")
            elif 1220>=posX>=960 and 250>=posY>=200: ##Check if the player is near Casino building
                print("Casino Area")
            elif 400>=posX>=250 and 680>=posY>=630: #Check if the player is near Bank building
                print("Bank Area")
            elif 1200>=posX>=980 and 700>=posY>=630: #Check if the player is near Lottery building
                print("Lottery Area")
        
    def get_status(self):
        # set statusfor idle animation
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
                    if self.direction.x > 0: # moving right
                        self.hitbox.right = building_rect.left
                    if self.direction.x < 0: # moving left
                        self.hitbox.left = building_rect.right
                    self.rect.centerx = self.hitbox.centerx
                    self.pos.x = self.hitbox.centerx
            
            if self.hitbox.colliderect(building_rect):
                if direction == "vertical":
                    if self.direction.y > 0: # moving down
                        self.hitbox.bottom = building_rect.top
                    if self.direction.y < 0: # moving up
                        self.hitbox.top = building_rect.bottom
                    self.rect.centery = self.hitbox.centery
                    self.pos.y = self.hitbox.centery

    def update(self, dt):
        self.input()
        self.get_status()
        self.move(dt)
        self.animate(dt)
        
