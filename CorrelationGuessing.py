import random, math
from tkinter import *
from tkinter.ttk import *

def createDotList(coefficient):
    dotList = []
    r = random.random()
    randomList = list((random.random()*r) for i in range(60))
    while(len(dotList)<40):
        dotList = []
        for i in range(60):
            x = random.random()
            y = coefficient*x + randomList[i]
            if (y>0 and y<1):
                dotList.append((x, y))
    return dotList

def drawDotList(canvas, dotList):
    for i in dotList:
        (x, y) = (50 + i[0]*200 , 250 - i[1]*200)
        canvas.create_oval(x, y, x+3, y+3, width=2)

def calculateR(dotList):
    (tx, txsquare, ty, tysquare, txy, n) = (0, 0, 0, 0, 0, len(dotList))
    for (x, y) in dotList:
        tx += x
        ty += y
        txsquare += x**2
        tysquare += y**2
        txy += x*y
    return abs((txy-tx*ty/n)/math.sqrt((txsquare-tx**2/n)*(tysquare-ty**2/n)))

def compareAnswer(guessR, realR, life, corn, canvas):
    difference = abs(guessR - realR)/realR
    if (difference>0.1):
        life -= 1
        drawLife(canvas, life)
    elif(difference>0.05):
        corn += 1
    else:
        life = life + 1 if life < 3 else life
        corn += 5 
        drawLife(canvas, life)

def drawLife(canvas, life):
    pass


def drawGamePanel():
    root = Tk()
    root.title("Guess Correlation")
    canvas = Canvas(root, width=600, height=400)
    canvas.pack()    
    canvas.create_rectangle(50, 50, 250, 250, width=5)
    canvas.create_line(52, 150, 248, 150, width=2, fill="gray")
    canvas.create_line(150, 52, 150, 248, width=2, fill="gray")
    canvas.create_text(30, 50, text="1.0", font="Monaco 15 bold")
    canvas.create_text(30, 150, text="0.5", font="Monaco 15 bold")
    canvas.create_text(30, 265, text="0", font="Monaco 15 bold")
    canvas.create_text(150, 265, text="0.5", font="Monaco 15 bold")
    canvas.create_text(250, 265, text="1.0", font="Monaco 15 bold")
    coefficient = random.random()
    dotList = createDotList(coefficient)
    drawDotList(canvas, dotList)
    print ("Coff=", coefficient, "Correlation=", calculateR(dotList), "n=", len(dotList))
    drawLife(canvas, 2)
    root.mainloop()

drawGamePanel()
