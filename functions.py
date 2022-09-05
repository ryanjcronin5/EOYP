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

    def FHF():
        col_list= list(functions.df)
        functions.df['Total'] = functions.df[functions.columnName[1]] + functions.df[functions.columnName[2]] + functions.df[functions.columnName[3]] + functions.df[functions.columnName[4]]
        functions.columnName = list(functions.df.columns)

    def GUI(): # Graphical User Inferface
        functions.FHF()
        BG = 'gray'
        root = Tk()
        root.title('Monster Card Games')
        root['bg']= BG
        root.geometry("700x400")
        draw = Canvas(root, width=651, bg=BG, bd=0, highlightthickness=0, relief='ridge')
        MYFONT = "Ubuntu"

        # Headers
        Label(root, text="Monster Card Data", bg=BG, font=MYFONT).place(x=10,y=10)
        Label(root, text="Click the name to edit and view the card", bg=BG, font=(MYFONT,10)).place(x=190,y=16)
        Label(root, text="File Name: "+functions.FILENAME, bg=BG, font=(MYFONT,10)).place(x=550,y=16)

        #Header Row
        draw.create_rectangle(0,0,140,30,fill="white")
        draw.create_rectangle(140,0,245,30,fill="white")
        draw.create_rectangle(245,0,350,30,fill="white")
        draw.create_rectangle(350,0,455,30,fill="white")
        draw.create_rectangle(455,0,560,30,fill="white")
        draw.create_rectangle(560,0,630,30,fill="white")      

        Label(root, text=functions.columnName[0], bg='white', font=MYFONT).place(x=11,y=51)
        Label(root, text=functions.columnName[1], bg='white', font=MYFONT).place(x=151,y=51)
        Label(root, text=functions.columnName[2], bg='white', font=MYFONT).place(x=256,y=51)
        Label(root, text=functions.columnName[3], bg='white', font=MYFONT).place(x=361,y=51)
        Label(root, text=functions.columnName[4], bg='white', font=MYFONT).place(x=466,y=51)
        Label(root, text=functions.columnName[5], bg='white', font=MYFONT).place(x=571,y=51)
        
        Y1=30
        Y=51
        for row in functions.df.index:
            Y2 = Y1+30
            Y = Y+30
            draw.create_rectangle(0,Y1,140,Y2,fill='white')
            Label(root, text=functions.df[functions.columnName[0]][row], bg='white', font=MYFONT).place(x=11,y=Y)
            draw.create_rectangle(140,Y1,245,Y2,fill='white')
            Label(root, text=functions.df[functions.columnName[1]][row], bg='white', font=MYFONT).place(x=151,y=Y)
            draw.create_rectangle(245,Y1,350,Y2,fill='white')
            Label(root, text=functions.df[functions.columnName[2]][row], bg='white', font=MYFONT).place(x=256,y=Y)
            draw.create_rectangle(350,Y1,455,Y2,fill='white')
            Label(root, text=functions.df[functions.columnName[3]][row], bg='white', font=MYFONT).place(x=361,y=Y)
            draw.create_rectangle(455,Y1,560,Y2,fill='white')
            Label(root, text=functions.df[functions.columnName[4]][row], bg='white', font=MYFONT).place(x=466,y=Y)
            draw.create_rectangle(560,Y1,630,Y2,fill='white')
            Label(root, text=functions.df[functions.columnName[5]][row], bg='white', font=MYFONT).place(x=571,y=Y)
            Y1 = Y1+30
        draw.place(x=10,y=50)

        
    def UAR(): # User Add Record
        pass
        


    def USR(): # User Save Record
        pass


    def UDR(): # User Delete Record
        pass


    def UDEV(): # User Data Empty Validation
        pass


    def UDIV(): # User Data Invalid Validation
        pass


    def main():
        functions.GUI()
        mainloop()

