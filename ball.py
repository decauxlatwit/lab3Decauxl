import pygame
class Ball:
    #pass
    Radius = 10

    def __init__(self, x, y, vx, vy, fgcolor, bgcolor, screen):
        #instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.bgcolor = bgcolor
        self.fgcolor = fgcolor
        self.screen = screen

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.Radius)

    def update(self):
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgcolor)
        if (self.x < 20):
            self.vx = -self.vx
        if (self.y < 20 or self.y > 460):
            self.vy = -self.vy