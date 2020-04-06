from graphics import *
from random import randint


i = 0


def pt(x,y,r,g,b):
    obj = Point(x,y)
    aColour = color_rgb(r,g,b)
    obj.setOutline(aColour)
    obj.draw(win)
    


win = GraphWin("Никому не нужный рисунок от никому не нужного утки", 600, 600)
while i < 6000:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    x = randint(1,600)
    y = randint(1,600)
    pt(x,y,r,g,b)
    i += 1


win.getMouse()
win.close()