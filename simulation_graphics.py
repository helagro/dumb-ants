from graphics import *
import tkinter as tk

DOT_SIZE_HALF = None
window = None

def drawDot(x, y, color):
    ll = Point(x - DOT_SIZE_HALF, y -DOT_SIZE_HALF)
    tr = Point(x + DOT_SIZE_HALF, y + DOT_SIZE_HALF)
    
    Rect = Rectangle(ll, tr)
    Rect.setFill(color)
    Rect.draw(window)

def drawStone(x, y):
    drawDot(x, y, "grey")

def init(width, height, windowCoordX, windowCoordY, dotSize):
    global window
    global DOT_SIZE_HALF
    DOT_SIZE_HALF = dotSize/2

    window = GraphWin(width=width, height=height)
    window.setCoords(0, 0, windowCoordX, windowCoordY)

def getScreenSize():
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height
