from graphics import *


def pt2(x,y,colour):
    global win
    win = GraphWin("Никому не нужный рисунок от никому не нужного утки", 600, 600)
    obj = Point(x,y)
    obj.setOutline(colour)
    obj.draw(win)

def pt1(x,y,r,g,b):
    global win
    win = GraphWin("Никому не нужный рисунок от никому не нужного утки", 600, 600)
    obj = Point(x,y)
    aColour = color_rgb(r,g,b)
    obj.setOutline(aColour)
    obj.draw(win)


tp = int(input("Введите цифру соответствующую способу, которым вы хотите выбрать цвет:\n1.rgb\n2.Выбрать цвет из таблицы цветов\n"))
x = int(input("Введите координату х: "))
y = int(input("Введите координату y: "))
if tp == 1:
    r = int(input("Введите первый спектр(первое число) из rgb таблицы: "))
    g = int(input("Введите второй спектр(второе число) из rgb таблицы: "))
    b = int(input("Введите третий спектр(третее число) из rgb таблицы: "))
    pt1(x,y,r,g,b)
else:
    colour = input("Введите однин из приведенных цветов:red,green,blue,yellow,black,white: ")
    pt2(x,y,colour)


win.getMouse()
win.close()