from graphics import *
import tkinter as tk

DOT_SIZE_HALF = None
window = None
worldMap = None

def drawDot(x, y, color, outlineColor = "black"):
    ll = Point(x - DOT_SIZE_HALF, y -DOT_SIZE_HALF)
    tr = Point(x + DOT_SIZE_HALF, y + DOT_SIZE_HALF)
    
    Rect = Rectangle(ll, tr)
    Rect.setFill(color)
    Rect.draw(window)
    Rect.setOutline(outlineColor)


def drawBackground(x, y):
    drawDot(x, y, "white", "white")
    worldMap[x][y] = 0

def drawAnt(x, y, ant):
    drawDot(x, y, ant.color)
    worldMap[x][y] = ant

def drawFood(x, y):
    drawDot(x, y, "red")
    worldMap[x][y] = "food"

def drawAntsNest(x, y, colony):
    drawDot(x, y, colony.getNestColor())
    worldMap[x][y] = colony

def drawStone(x, y):
    drawDot(x, y, "grey")
    worldMap[x][y] == "stone"



def getCoordStatus(x, y):
    return worldMap[x][y]

def init(width, height, windowCoordX, windowCoordY, dotSize):
    global window
    global DOT_SIZE_HALF
    global worldMap
    DOT_SIZE_HALF = dotSize/2

    window = GraphWin(width=width, height=height)
    window.setCoords(0, 0, windowCoordX, windowCoordY)
    worldMap = [ [0]*(windowCoordY+1) for i in range(windowCoordX+1)]


def getScreenSize():
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height
