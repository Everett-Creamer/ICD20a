#E Creamer
#05/03/2025
#While Loop Demo
import sys
print(sys.executable)
import pygame
pygame.init()

class Player():
    def __init__(self):
        #member variables taking in x,y,w,h and speed of the character
        self.x = 0
        self.y = 600
        self.w = 50
        self.h = 50
        self.speed = 10
        #takes in gravity, if it is jumping, the jump height and sets the y up to the jump heigt
        self.gravity = 2
        self.jumping = False
        self.jump_height = 30
        self.y_up = self.jump_height
        
    def update(self):
        #draws character
        pygame.draw.rect(screen, "green", (self.x, self.y, self.w, self.h))
        #detects key presses
        keys = pygame.key.get_pressed()
        #if a or d is pressed, move character in corresponding direction. If space is pressed set jumping to True
        if keys[pygame.K_BACKSPACE]:
            self.jumping = True
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        
        #if jumping is true
        if self.jumping: #https://www.youtube.com/watch?v=ST-Qq3WBZBE
            #changes y of character by y_up
            self.y -= self.y_up
            #changes y up of character by gravity
            self.y_up -= self.gravity
            #if the character has completed jump (less tahn -jump height)
            if self.y_up < - self.jump_height:
                #the character is no longer jumping
                self.jumping = False
                #set the y vilocity to the jump height
                self.y_up = self.jump_height
        
        #if the charcter drops below 720, set character to 0,0
        if self.y > 720:
            self.y = 0
            self.x = 0
        #if the characters x is less than 0, it sets it to 0
        if self.x < 0:
            self.x = 0
        #if the characters x is greater than 1280
        if self.x + self.w > 1280:
            #set chracter x to 1280
            self.x = 1280 - self.w

    #gravity function
    def gravity_func(self, Wall):
        #checks for colision within the given wall class
        if (self.x < Wall.x + Wall.w and self.x + self.w > Wall.x and Wall.y < self.y + self.h and Wall.y + Wall.h > self.y):
            #if their is collision, set the charactersx to the wall y
            self.y = Wall.y - self.h 
        else:
            #if not, apply gravity
            self.y += self.gravity


#wall class
class Wall():
    #takes member variables of x, y, w, h
    def __init__(self):
        self.x = 0
        self.y = 670
        self.w = 1000
        self.h = 20
    #draw function that draws rectangle
    def update(self):
        pygame.draw.rect(screen, "black", (self.x, self.y, self.w, self.h))

#instantiating the player, and the multiple platforms
character = Player()

ground = Wall()
platform = Wall()
platform.x = 1100
platform.y = 580

platform_2 = Wall()
platform_2.x = 900
platform_2.y = 445
platform_2.w = 150

platform_3 = Wall()
platform_3.x = 600
platform_3.y = 370
platform_3.w = 150

platform_4 = Wall()
platform_4.x = 860
platform_4.y = 240
platform_4.w = 150

platform_5 = Wall()
platform_5.x = 1115
platform_5.y = 130
platform_5.w = 150
#1115, 130

#the list of all objects you want to apply collision for
wall_list = [ground, platform, platform_2, platform_3, platform_4, platform_5]

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    screen.fill("purple")

    
    #runs all of the update functions, which draws everything
    character.update()
    ground.update()
    platform.update()
    platform_2.update()
    platform_3.update()
    platform_4.update()
    platform_5.update()

    #a for loop that loops through all of the items in the wall list
    for i in wall_list:
        #and checks if their is collision
        character.gravity_func(i)

    pygame.display.flip()
    clock.tick(60)


