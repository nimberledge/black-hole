from math import *
import pygame
import colour as col
import button

class game_circle(object):
    
    def __init__(self, radius = None, centre = (0,0), colour = col.BLACK, value = None):
        self.radius = radius
        self.centre = centre
        self.x = centre[0]
        self.y = centre[1]
        self.colour = colour
        self.value = value
        self.text = str(self.value)
        self.generate_tbox()

    def generate_tbox(self):
        x = int(self.x-(self.radius/sqrt(2)))
        y = int(self.y-(self.radius/sqrt(2)))
        w = 2*sqrt(2)*self.radius
        fnt = pygame.font.SysFont('Times New Roman', 15)
        self.tbox = button.button(self.text, x, y, w, w, self.colour, col.WHITE, fnt)

    def draw_circle(self, screen):
        pygame.draw.circle(screen, self.colour, self.centre, self.radius)
        tbox.draw(screen)

    def is_clicked(self, mpos):
        if (self.x - self.radius) < mpos[0] < (self.x + self.radius) and (self.y - self.radius) < mpos[1] < (self.y + self.radius):
            return True
        return False

    def update_circle(self, colour, value):
        self.colour = colour
        self.value = value


    

    
        
        
        
