import pygame
import game_circle

class Board(object):
    pattern = [1,2,3,4,5]

    def __init__(self):
        self.grid = []
        initialize_grid(self)

    def initialize_grid(self):
        for i in range(sum(Board.pattern)):
            self.grid.append(game_circle.game_circle())

    def draw_board(self, screen):
        for circle in self.grid:
            circle.draw_circle(screen)

    def update_board(self, mpos):
        #NOT THE FINAL IMPLEMENTATION
        for circle in self.grid:
            if circle.is_clicked():
                circle.update_circle(colour, value)
        
        
            
            
        
        
        
