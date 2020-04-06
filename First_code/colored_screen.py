from graphics import *
from random import randint


x = 0
y = 0

def pt(x,y,r,g,b):
    obj = Point(x,y)
    aColour = color_rgb(r,g,b)
    obj.setOutline(aColour)
    obj.draw(win)



win = GraphWin("Никому не нужный рисунок от никому не нужного утки", 256, 256)
for x in range(256):
    for y in range(256):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        pt(x,y,r,g,b)



win.getMouse()
win.close()