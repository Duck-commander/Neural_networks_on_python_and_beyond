from graphics import *
from random import randint


def rpt(x,y):
    obj = Point(x,y)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    aColour = color_rgb(r,g,b)
    obj.setOutline(aColour)
    obj.draw(win)

def lineX(x,x2):
    for x in range(x,x2):
        rpt(x)

def lineY(y,y2):
    for y in range(y,y2):
        rpt(y)


win = GraphWin("Никому не нужный рисунок от никому не нужного утки", 256, 256)
for x in range(128):
    for y in range(128):
        rpt(x,y)
        x1 = 128 + x
        y1 = 128 - y
        rpt(x1,y1)
        y2 = 128 + y
        rpt(x,y2)
        x3 = 128 + x
        y3 = 128 + y
        rpt(x3,y3)


win.getMouse()
win.close()