#E Creamer
#2/05/2025
#If statment demo
import pygame
pygame.init()

#player class
class Player():
    def __init__(self):
        #member variables taking in x,y,w,h and speed of the character
        self.x = 0
        self.y = 0
        self.w = 50
        self.h = 100
        self.speed = 10
        
    def update(self):
        pygame.draw.rect(screen, "green", (self.x, self.y, self.w, self.h))
        #detects key presses
        keys = pygame.key.get_pressed()
        #if the key pressed is w, a, s or d it moves the character in the corresponding direction, https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-tutorial-movement
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        #checks to see if the x and y value is outside the screen, and if it is, sets the x/y value to the closest point on screen
        if self.x < 0:
            self.x = 0
        elif self.x > 1280 - self.w:
            self.x = 1280 - self.w
        elif self.y < 0:
            self.y = 0
        elif self.y > 720 - self.h:
            self.y = 720 - self.h
#door class
class Door():
    def __init__(self):
        #member variables x,y,w,h and weather the door is open
        self.x = 740
        self.y = 180
        self.w = 141
        self.h = 224
        self.door_open = False
    #function to update the door image and hit box, this takes in the player class and key class
    def update(self, Player, Key):
        #if the door is not open
        if not self.door_open:
            #draw a hit box
            pygame.draw.rect(screen, "yellow", (self.x, self.y, self.w, self.h))
            #load a door img
            close_door = pygame.image.load("Close Door.png")
            #put dooor img on screen
            screen.blit(close_door, (self.x, self.y))
            #checks if the player picked up the key, if so
            if (Player.x < self.x + self.w and Player.x + Player.w > self.x and self.y < Player.y + Player.h and self.y + self.h > Player.y) and Key.has_key == True :
                #set the door to open
                self.door_open = True
        else:
            #when the door is open, load the door is open img onto the screen
            open_door = pygame.image.load("Open Door.png")
            screen.blit(open_door, (self.x, self.y))
#key class
class Key():
    def __init__(self):
        #members variable that takes in the x,y,w,h and if the user has a key
        self.x = 1000
        self.y = 200
        self.w = 50
        self.h = 50
        self.has_key = False
    #update function that draws the hitbox
    def update(self, Player):
        #properly loads font and the correct text
        Font = pygame.font.SysFont('timesnewroman',  24)
        info = Font.render("KEY", False, "black")
        #draws rectangle with Key text in it
        pygame.draw.rect(screen, "cyan", (self.x, self.y, self.w, self.h))
        screen.blit(info, (self.x, self.y))
        #if the player collides with the key, the key has been picked up
        if (Player.x < self.x + self.w and Player.x + 1 > self.x and self.y < Player.y + 1 and self.y + self.h > Player.y):
            self.has_key = True

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
#setting character, main door and main key to corresponding classes
character = Player()
main_door = Door()
main_key = Key()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    screen.fill("purple")



    #calling the update function, and giving each function the proper parameters
    main_door.update(character, main_key)
    main_key.update(character)
    character.update()

    pygame.display.flip()  
    clock.tick(60)         