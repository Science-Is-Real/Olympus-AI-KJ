import time
from tkinter import*
root = Tk()
curLabels = []
curRow = 1
lRow = 0
def Talk(speech, x = 0):
    global curLabels
    global curRow
    curLabels.append(Label(root,text=speech))
    if curRow < 10:
        curLabels[-1].grid(row=curRow,column=0,sticky="w")
    else:
        curLabels = curLabels[1:]
        for x in range(10):
            curLabels[x].grid_forget()
            curLabels[x].grid(row=x,column=0,sticky="w")
        curLabels[-1].grid(row=10,column=0,sticky="w")
    curRow += 1
    if x == 0:
        Talk(" ",1)
    root.update()
def button(Text, Command):
    global curRow
    Button(root, text = str(Text), command = Command).grid(row = curRow, column = 0, sticky = 'w', pady = 4)
    
def Listen(title):
    global lRow
Button(root, text = 'Quit', command = root.destroy).grid(row = 0, column = 0, sticky = 'w', pady = 4)    
    
