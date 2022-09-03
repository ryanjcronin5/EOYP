import numpy as np
import pandas as pd
from tkinter import *
import tkinter.font as font
import re
from datetime import date

class functions():
    FILENAME = 'mcards.csv'
    df = pd.read_csv(FILENAME)
    columnName = list(df.columns)

    def __init__(self):
        pass


    def GUI(): # Graphical User Inferface
        BG = 'gray'
        root = Tk()
        root.title('Monster Card Games')
        root['bg']= BG
        root.geometry("700x400")
        draw = Canvas(root, bg=BG, bd=0, highlightthickness=0, relief='ridge')

        MYFONT = "Ubuntu"

        # Headers

        Label(root, text="Monster Card Data", bg=BG, font=MYFONT).place(x=10,y=10)
        Label(root, text="Click the name to edit and view the card", bg=BG, font=(MYFONT,10)).place(x=190,y=16)
        Label(root, text="File Name: "+functions.FILENAME, bg=BG, font=(MYFONT,10)).place(x=550,y=16)

        #Header Row


        draw.create_rectangle(0,0,90,30,fill="white")
        draw.create_rectangle(90,0,180,30,fill="white")
        draw.create_rectangle(180,0,270,30,fill="white")
        draw.create_rectangle(270,0,360,30,fill="white")
        draw.place(x=10,y=50)

        Label(root, text=functions.columnName[0], bg='white', font=MYFONT).place(x=11,y=51)
        Label(root, text=functions.columnName[1], bg='white', font=MYFONT).place(x=101,y=51)
        Label(root, text=functions.columnName[2], bg='white', font=MYFONT).place(x=191,y=51)
        Label(root, text=functions.columnName[3], bg='white', font=MYFONT).place(x=281,y=51)

        


    def UAR(): #User Add Record
        pass
        


    def USR():
        pass


    def UDR():
        pass


    def UDEV():
        pass


    def UDIV():
        pass


    def main():
        functions.GUI()
        mainloop()

