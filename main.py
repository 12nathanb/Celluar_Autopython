import pygame
import random
from cell import Cell

def gameOfLife(amount, x, y):

    if amount > 0:

        if cellArray[x][y].getState() == "ALIVE" and amount < 2:
            nextSetStateArray[x][y] = "DEAD"

        elif cellArray[x][y].getState() == "ALIVE" and amount == 2:
            nextSetStateArray[x][y] = "ALIVE"

        elif cellArray[x][y].getState() == "ALIVE" and amount == 3:
            nextSetStateArray[x][y] = "ALIVE"

        elif cellArray[x][y].getState() == "ALIVE" and amount > 3:
            nextSetStateArray[x][y] = "DEAD"

        elif cellArray[x][y].getState() == "DEAD" and amount == 3:
            nextSetStateArray[x][y] = "ALIVE"

def oddOrEven(amount, x, y):
    
    if amount % 2 == 0:
        nextSetStateArray[x][y] = "ALIVE"

    else:
        nextSetStateArray[x][y] = "DEAD"

def makeACircle():
    cellArray[49][47].setState("ALIVE")
    cellArray[50][47].setState("ALIVE")

    cellArray[48][48].setState("ALIVE")
    cellArray[49][48].setState("ALIVE")
    cellArray[50][48].setState("ALIVE")
    cellArray[51][48].setState("ALIVE")

    cellArray[47][49].setState("ALIVE")
    cellArray[48][49].setState("ALIVE")
    cellArray[49][49].setState("ALIVE")
    cellArray[50][49].setState("ALIVE")
    cellArray[51][49].setState("ALIVE")
    cellArray[52][49].setState("ALIVE")

    cellArray[48][50].setState("ALIVE")
    cellArray[49][50].setState("ALIVE")
    cellArray[50][50].setState("ALIVE")
    cellArray[51][50].setState("ALIVE")

    cellArray[49][51].setState("ALIVE")
    cellArray[50][52].setState("ALIVE")

    for i in range(gridSize):
        for j in range(gridSize):
            nextSetStateArray[i][j] = cellArray[i][j].getState()

def nearestNeigbourOf3(c, x, y):
    counter = ""
    if x > 0 and x < gridSize - 1 and  y > 0 and y < gridSize - 1:

        if cellArray[(x - 1)][(y)].getState() == "ALIVE": 
            counter + "1"
        else:
            counter + "0"

        if cellArray[(x)][(y)].getState() == "ALIVE": 
            counter + "1"
        else:
            counter + "0"

        if cellArray[(x + 1)][(y)].getState() == "ALIVE": 
            counter + "1"
        else:
            counter + "0"
    
    return counter

def nearestNeigbour(c, x, y):
    counter = 0
    if x > 0 and x < gridSize - 1 and  y > 0 and y < gridSize - 1:
        

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

    return counter

def rule30(r, x, y):
    if r == "111":
        nextSetStateArray[x][y + 1] = "DEAD"
    elif r == "110":
        nextSetStateArray[x][y + 1] = "DEAD"
        nextSetStateArray[x + 1][y] = "DEAD"
    elif r == "101":
        nextSetStateArray[x][y + 1] = "DEAD"
        nextSetStateArray[x][y] = "DEAD"
    elif r == "100":
        nextSetStateArray[x + 1][y] = "DEAD"
        nextSetStateArray[x][y] = "DEAD"
    elif r == "011":
        nextSetStateArray[x - 1][y] = "DEAD"
    elif r == "010":
        nextSetStateArray[x + 1][y] = "DEAD"
        nextSetStateArray[x - 1][y] = "DEAD"
    elif r == "001":
        nextSetStateArray[x][y] = "DEAD"
        nextSetStateArray[x - 1][y] = "DEAD"
    elif r == "000":
        nextSetStateArray[x + 1][y] = "DEAD"
        nextSetStateArray[x - 1][y] = "DEAD"
        nextSetStateArray[x][y] = "DEAD"
        nextSetStateArray[x][y + y] = "DEAD"


        
def setupCellArray():
    for i in range(gridSize):
        for j in range(gridSize):
            t = random.randint(0, 1)

            cellArray[i][j] = Cell(j , i , cellSize, stateArray[t], screen)
            
            nextSetStateArray[i][j] = cellArray[i][j].getState()
            cellArray[i][j].setColor()

pygame.init()
clock = pygame.time.Clock()
screenSize = 1000
gridSize = 100
cellSize = screenSize / gridSize
screen = pygame.display.set_mode((screenSize, screenSize))
RUN = False
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

cellArray = [[Cell for i in range(gridSize)] for j in range(gridSize)]

stateArray = ["ALIVE", "DEAD"]

nextSetStateArray = [ [" "]* gridSize for i in range(gridSize)]

setupCellArray()
#makeACircle()
        
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


    screen.fill(WHITE)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            RUN = True
            
  
    if RUN == True:
        for i in range(gridSize):
            for j in range(gridSize):
            
                cellArray[i][j].draw()
                cellArray[i][j].setColor()
                #oddOrEven(nearestNeigbourOf3(cellArray[i][j], i, j), i, j)
                rule30(nearestNeigbourOf3(cellArray[i][j], i, j), i, j)

        
        for i in range(gridSize):
                for j in range(gridSize):
                    cellArray[i][j].setState(nextSetStateArray[i][j])
                    
    
    
    pygame.display.flip()

    clock.tick(15)

# Done! Time to quit.

pygame.quit()