from graphics import *
import tkinter as tk

DOT_SIZE_HALF = None
window = None
worldMap = None

def drawDot(x, y, color):
    ll = Point(x - DOT_SIZE_HALF, y -DOT_SIZE_HALF)
    tr = Point(x + DOT_SIZE_HALF, y + DOT_SIZE_HALF)
    
    Rect = Rectangle(ll, tr)
    Rect.setFill(color)
    Rect.draw(window)

def drawAntsNest(x, y, colony):
    drawDot(x, y, colony.color)
    worldMap[x][y] = colony

def drawStone(x, y):
    drawDot(x, y, "grey")
    worldMap[x][y] == "stone"

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
