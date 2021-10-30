
# import the pygame module, so you can use it
import pygame
import random
#from paddle import Paddle
from ball import Ball
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("DeCauxl pong")
    WIDTH = 800
    HEIGHT = 480
    BORDER = 20
    VELOCITY = 5
    FPS = 60
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    fgcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")

    #Draw Top Wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (WIDTH, BORDER)))
    #Draw Bottom Wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (BORDER, HEIGHT)))
    #Draw Left Wall
    pygame.draw.rect(screen, fgcolor, pygame.Rect((0,HEIGHT-BORDER), (WIDTH, BORDER)))
    pygame.display.update() #only needed for macOS bug

    #Ball init
    x0 = WIDTH - Ball.Radius
    y0 = HEIGHT // 2
    vx0 = -random.randint(1,VELOCITY)
    vy0 = random.randint(-VELOCITY,VELOCITY)
    b0 = Ball(x0,y0,vx0,vy0,fgcolor,bgcolor,screen)
    b0.show(fgcolor)
    #pygame.draw.circle(screen, fgcolor, (x0, y0), 10)
    # define a variable to control the main loop
    pygame.display.update()
    running = True
    clock = pygame.time.Clock()
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        clock.tick(FPS)
        #Ball
        b0.update()
        pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (WIDTH, BORDER)))
        #Draw Bottom Wall
        pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (BORDER, HEIGHT)))
        #Draw Left Wall
        pygame.draw.rect(screen, fgcolor, pygame.Rect((0,HEIGHT-BORDER), (WIDTH, BORDER)))
        pygame.display.update()
     
     
if __name__=="__main__":
    main()

