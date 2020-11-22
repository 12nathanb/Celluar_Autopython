import pygame

class Cell:
    
    

    def __init__(self, x, y, size, state, screen):
        
        self.x = x
        self.y = y
        self.state = state
        self.screen = screen
        self.size = size
        self.age = 0
       
        

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
        GREEN1 = (255, 13, 0)
        GREEN2 = (232, 12, 0)
        GREEN3 = (217, 13, 2)
        GREEN4 = (201, 10, 0)
        GREEN5 = (181, 11, 2)
        GREEN6 = (163, 10, 2)
        GREEN7 = (145, 7, 0)
        GREEN8 = (128, 6, 0)
        GREEN9 = (110, 5, 0)
        GREEN10 = (94, 4, 0)
        
        RED = (222, 28, 18)
        
        if self.state == "DEAD":
            self.age  = 0
            self.color = BLACK
        else:
            self.age  = self.age  + 1
            
        if self.state == "ALIVE":
            if self.age == 1:
                self.color = GREEN1

            if self.age == 2:
                self.color = GREEN2

            if self.age == 3:
                self.color = GREEN3
            
            if self.age == 4:
                self.color = GREEN4

            if self.age == 5:
                self.color = GREEN5

            if self.age == 6:
                self.color = GREEN6

            if self.age == 7:
                self.color = GREEN7
            
            if self.age == 8:
                self.color = GREEN8
            
            if self.age == 9:
                self.color = GREEN9
            
            if self.age == 10:
                self.color = GREEN10

            if self.age > 10:
                self.color = BLACK