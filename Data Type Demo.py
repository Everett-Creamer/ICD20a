#E Creamer
#2/05/2025
#Demo of data types, interactive
import pygame

pygame.init()
#a class to make boxes
class Box():
    def __init__(self):
        #meber varaibles like x,y,w,h of box, and what info there will be
        self.x = 0
        self.y = 0
        self.w = 250
        self.h = 150
        self.info = ""
        #function that draws box
    def update(self):
        #gets the x and y of mouse
        posx, posy = pygame.mouse.get_pos()
        #http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5 for text
        
        #properly loads font and the correct text
        Font = pygame.font.SysFont('timesnewroman',  15)
        info = Font.render(str(self.info), False, "black")
        #draws the box
        pygame.draw.rect(screen, "white", (self.x, self.y, self.w, self.h))
        #puts text in the box
        screen.blit(info, [self.x, self.y])
        #checks to see if the mouse is over the box and if left click is being pressed
        if (posx < self.x + self.w and posx + 1 > self.x and self.y < posy + 1 and self.y + self.h > posy) and pygame.mouse.get_pressed()[0]:
            #setting the x and y to the x and y of mouse, then offsetting it so you can move the box up
            self.x = int(posx) - 20
            self.y = int(posy) - 20


#creating the 4 different boxxes
int_ = Box()
int_.x = 426
int_.y = 180
int_.info = "An int data type is a data type that hold whole numbers"

float_ = Box()
float_.x = 852
float_.y = 180
float_.info = "A float is a data type that holds small whole numbers and decimal numbers"

string = Box()
string.x = 640
string.y = 270
string.info = "A string is a data type that holds characters. Strings can be numbers, but the numbers would hold no number value unless it gets turned into a int or float"

spare = Box()
spare.w = 300
spare.info = "A bool is a data type that holds true or false"

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
#while loop
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit


    #setting background to black
    screen.fill("black")
    #updating the 4 box
    spare.update()
    
    int_.update()
    
    float_.update()
    
    string.update()
    

    pygame.display.flip()
    clock.tick(144)         