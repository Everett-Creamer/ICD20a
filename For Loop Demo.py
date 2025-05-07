#E Creamer
#03/05/2025
#For Loop Demo
import pygame
#getting the users input
user_input = input("What is a sentance you want pasted? ")
pygame.init()
#setting up the screen
screen = pygame.display.set_mode((1280,720))

#a function that takes in text and a starting location, and outputs the text
def text(input, pos):
    #setting the font
    Font = pygame.font.SysFont('timesnewroman',  24)
    #setting the text
    info = Font.render(str(input), False, "black")
    #pasting text on the screen at position pos
    screen.blit(info, pos)

clock = pygame.time.Clock()




while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    #setting background to purple
    screen.fill("purple")
    #looping 100 times
    for i in range(100):
        #setting the x to 0
        text_x = 0
        #setting the y to 0 + i to x 10 so there is enough space bettween words
        text_y = 0 + i * 10
        #checking if the x went below the screen
        if text_y > 720:
            #if it has, set the y to 0, the x to 20x the length of the word
            text_y = 0
            text_x += len(user_input) * 20
        #pasting the text on the screen
        text(user_input, (text_x, text_y))

    pygame.display.flip()
    clock.tick(60)
