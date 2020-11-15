import pygame

class Cell:
    
    

    def __init__(self, x, y, size, state, screen):
        
        self.x = x
        self.y = y
        self.state = state
        self.screen = screen
        self.size = size

       
        

    def draw(self):
        pygame.draw.rect(self.screen, self.color , (self.size * self.x, self.size * self.y, self.size, self.size))
       
    def getX(self):
        return self.x / self.size
    
    def getY(self):
        return self.y / self.size

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        
    def setSearch(self, color):
        
        self.color = color
    def setColor(self):
        BLACK = ( 0, 0, 0)
        WHITE = ( 255, 255, 255)
        if self.state == "DEAD":
            self.color = WHITE
        else:
            self.color = BLACK