import pygame
from support import *

'''
This file is to setup the player (character)
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
        self.animations = {'up': [], 'up_idle': [], 'down':[], 'down_idle': [], 'left':[], 'left_idle':[], 'right':[], 'right_idle':[]}

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
        
        # Directions
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
    
    def get_status(self):
        # set statusfor idle animation
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'
        
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

        