import pygame
import random
from cell import Cell

def nearestNeigbour(c, x, y):
    #x = int(c.getX())
    #y = int(c.getY())
    s = c.getState()
    

    if x > 0 and x < gridSize - 1 and  y > 0 and y < gridSize - 1:
        counter = 0

        

        if cellArray[(x - 1)][(y - 1)].getState() == "ALIVE":
            counter = counter + 1
           

        if cellArray[(x)][(y - 1)].getState() == "ALIVE": 
            counter = counter + 1
           

        if cellArray[(x + 1)][(y - 1)].getState() == "ALIVE": 
            counter = counter + 1
            

        if cellArray[(x - 1)][(y)].getState() == "ALIVE": 
            counter = counter + 1
           

        if cellArray[(x + 1)][(y)].getState() == "ALIVE": 
            counter = counter + 1
            

        if cellArray[(x - 1)][(y + 1)].getState() == "ALIVE": 
            counter = counter + 1
            

        if cellArray[(x)][(y + 1)].getState() == "ALIVE": 
            counter = counter + 1
            

        if cellArray[(x + 1)][(y + 1)].getState() == "ALIVE": 
            counter = counter + 1
           

        if cellArray[x][y].getState() == "ALIVE" and counter < 2:
            nextSetStateArray[x][y] = "DEAD"

        elif cellArray[x][y].getState() == "ALIVE" and counter == 2:
            nextSetStateArray[x][y] = "ALIVE"

        elif cellArray[x][y].getState() == "ALIVE" and counter == 3:
            nextSetStateArray[x][y] = "ALIVE"

        elif cellArray[x][y].getState() == "ALIVE" and counter > 3:
            nextSetStateArray[x][y] = "DEAD"

        elif cellArray[x][y].getState() == "DEAD" and counter == 3:
            nextSetStateArray[x][y] = "ALIVE"

    
    


pygame.init()
clock = pygame.time.Clock()
screenSize = 500
gridSize = 50
cellSize = screenSize / gridSize
screen = pygame.display.set_mode((screenSize, screenSize))

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

cellArray = [[Cell for i in range(gridSize)] for j in range(gridSize)]

stateArray = ["ALIVE", "DEAD"]

nextSetStateArray = [ [" "]* gridSize for i in range(gridSize)]

for i in range(gridSize):
    for j in range(gridSize):
        ranInt = random.randint(0, 1)
        cellArray[i][j] = Cell(j , i , cellSize, stateArray[ranInt], screen)
        nextSetStateArray[i][j] = cellArray[i][j].getState()
        cellArray[i][j].setColor()
        #cellArray.append()
        

running = True

while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    # Fill the background with white

    screen.fill(WHITE)
    #test.draw()
    #for x in cellArray:
        
       # x.draw()
    
    for i in range(gridSize):
        for j in range(gridSize):
           
            cellArray[i][j].draw()
            cellArray[i][j].setColor()
            nearestNeigbour(cellArray[i][j], i, j)
    
    for i in range(gridSize):
            for j in range(gridSize):
                cellArray[i][j].setState(nextSetStateArray[i][j])
    
    if event.type == pygame.MOUSEBUTTONDOWN:

        for i in range(gridSize):
            for j in range(gridSize):
                state1 = cellArray[i][j].getState()
                nearestNeigbour(cellArray[i][j], i, j)
                state2 = cellArray[i][j].getState()
                print("STATE 1: {} STATE 2: {}".format(state1, state2))
        
        

    # Flip the display

    pygame.display.flip()

    clock.tick(2)

# Done! Time to quit.

pygame.quit()