"""Monster Card Catalogue."""

import random
from tkinter import messagebox
import pandas as pd
from tkinter import *
import re
from datetime import date
from PIL import Image, ImageTk
import time


class Card():
    """Main class of program."""

    FILENAME = 'mcards.csv'
    df = pd.read_csv(FILENAME)
    clname = list(df.columns)
    root = Tk()
    draw = Canvas(
        root, width=851, height=355, bg='gray', 
        bd=0, highlightthickness=0, relief='ridge')
    record = IntVar()
    FONT = "Ubuntu"
    MAXCARDS = 10
    MAXPOINTS = 25
    MINPOINTS = 1
    NAMELIMIT = r"^[a-zA-Z0-9]*$"
    eflag = 0
    iflag = 0
    day = date.today()
    today = day.strftime("%d - %m - %y")
    images = ['XM0.png', 'XM1.png', 'XM2.png', 'XM3.png', 'XM4.png']
    edited = False

    def __init__():
        pass

    def filehandle():
        """Gets the data from the csv and calculates the total."""

        Card.df = pd.read_csv(Card.FILENAME)
        Card.df['Total'] = (
            Card.df[Card.clname[1]]+
            Card.df[Card.clname[2]]+
            Card.df[Card.clname[3]]+
            Card.df[Card.clname[4]])
        Card.clname = list(Card.df.columns)
        Card.df.to_csv(Card.FILENAME, index=False)


    def creategui():
        """Creates the tkinter gui."""

        def search():
            search = searchEty.get()
            filter = Card.df['Name'] == search
            result = Card.df[filter].index[0]
            searchEty.delete(0, END)
            Card.viewcard(result)

        def temp_text(e):
            searchEty.delete(0, END)

        BG = 'gray'
        Card.root.title('Monster Card Games')
        Card.root['bg'] = BG
        Card.root.geometry("900x410")

        # Headers
        Label(
            Card.root,
            text="Monster Card Data",
            bg=BG,
            font=Card.FONT).place(x=10, y=10)
        Label(
            Card.root,
            text="Click the name to view the card",
            bg=BG,
            font=(Card.FONT, 10)).place(x=190, y=16)
        Label(
            Card.root,
            text="File Name: "+Card.FILENAME+"   Date: "+Card.today,
            bg=BG,
            font=(Card.FONT, 10)).place(x=440, y=16)
        searchEty = Entry(
            Card.root,
            font=(Card.FONT, 10))
        searchEty.insert(0, "Search By Name...")
        searchEty.place(x=700,y=16)
        Button(
            Card.root,
            text='Search',
            font=(Card.FONT,10),
            command=search).place(x=850,y=16)

        searchEty.bind("<FocusIn>", temp_text)

        #Header Row
        Card.draw.create_rectangle(0,0,140,30,fill="white")
        Card.draw.create_rectangle(140,0,245,30,fill="white")
        Card.draw.create_rectangle(245,0,350,30,fill="white")
        Card.draw.create_rectangle(350,0,455,30,fill="white")
        Card.draw.create_rectangle(455,0,560,30,fill="white")
        Card.draw.create_rectangle(560,0,665,30,fill="white")  

        Button(
            Card.draw, 
            text=Card.clname[0], 
            bg='white', 
            bd=0, 
            font=Card.FONT, 
            command=lambda:Card.sortdata(sortkey=0)).place(x=11,y=0)
        X2=105
        X3=141 
        for i in range(len(Card.clname)-2):
            sortkey = i+2
            Button(
                Card.draw, 
                text=Card.clname[i+1], 
                bg='white', 
                bd=0, 
                font=Card.FONT, 
                command=lambda:Card.sortdata(sortkey)).place(x=X3,y=0)
            X3=X3+X2
        
        Y1=30
        R = 0

        for row in Card.df.index:
            Y2 = Y1+30
            Card.draw.create_rectangle(0,Y1,140,Y2,fill='white')
            Radiobutton(
                Card.draw, 
                text=Card.df[Card.clname[0]][row], 
                indicatoron = 0, 
                variable=Card.record, 
                bg='white', 
                bd=0, 
                font=Card.FONT, 
                command=lambda:Card.viewcard(Card.record.get()), 
                value=row, 
                padx=5).place(x=1,y=Y1)
            
            X1=151
            X2=105
            X3=141
            X4=245
            for i in range(len(Card.clname)-2):
                Card.draw.create_rectangle(X3,Y1,X4,Y2,fill='white')
                Label(
                    Card.draw, 
                    text=Card.df[Card.clname[i+1]][row], 
                    bg='white', 
                    font=Card.FONT,
                    padx=10,).place(x=X3,y=Y1)
                X1=X1+X2
                X3=X3+X2
                X4=X4+X2
            Y1 = Y1+30
            R = R+1
        Y2 = Y1+31

        Button(
            Card.draw, 
            text="Export to Txt", 
            font=(Card.FONT,10), 
            bg='yellow',
            command=Card.export).place(x=675, y=325)
        Button(
            Card.draw, 
            text="Exit", 
            font=(Card.FONT,10), 
            bg='red',
            command=Card.root.destroy).place(x=765, y=325)

        if len(Card.df.index) != Card.MAXCARDS:
            global nRecord
            nRecord = Radiobutton(
                Card.draw, 
                text="New Record", 
                indicatoron = 0, 
                variable=Card.record, 
                bg='white', 
                bd=0, 
                font=Card.FONT, 
                value=R, 
                padx=10, 
                command=lambda:Card.addRecord(edit=False))
            nRecord.place(x=1,y=Y1)
        Card.draw.place(x=10,y=50)


    def export():
        Card.df.to_csv(
            r'monsterCards.txt', 
            header=None, 
            index=None, 
            sep='\t', 
            mode='w')
        messagebox.showinfo('Success','Successfully exported as text file.')


    def viewcard(result):
        frame = Frame(
            Card.root, 
            bg = 'light gray',
            height = 275,
            width = 175)
        title = Label(
            frame, 
            text = str(Card.df['Name'][result]),
            bg='white', 
            font = Card.FONT,
            width = 16)
        strength = Label(
            frame,
            text = 'Strength '+str(
                Card.df['Strength'][result]),
            bg = 'white',
            font = Card.FONT,
            width = 16)
        speed = Label(
            frame,
            text = 'Speed '+str(
                Card.df['Speed'][result]),
            bg = 'white',
            font = Card.FONT,
            width = 16)
        stealth = Label(
            frame,
            text = 'Stealth '+str(
                Card.df['Stealth'][result]),
            bg = 'white',
            font = Card.FONT,
            width = 16)
        cunning = Label(
            frame,
            text = 'Cunning '+str(
                Card.df['Cunning'][result]),
            bg = 'white',
            font = Card.FONT,
            width = 16)
        title.place(x=0, y=1)
        strength.place(x=0, y=145)
        speed.place(x=0, y=175)
        stealth.place(x=0, y=205)
        cunning.place(x=0, y=235)
        Button(
            Card.draw, 
            text="Delete Card", 
            font=(Card.FONT,10), 
            bg="red", 
            command=lambda:Card.deleteRecord(result)).place(x=765, y=290)
        
        editBtn = Button(
            Card.draw,
            text="Edit Card", 
            font=(Card.FONT,10), 
            bg="orange",
            command=lambda:Card.addRecord(edit=True))
        editBtn.place(x=675, y=290)
        
        if Card.df['Added'][result] == 1:
            editBtn["state"] = NORMAL
        if Card.df['Added'][result] == 0:
            editBtn["state"] = DISABLED
        
        file = random.choice(Card.images)
        img = ImageTk.PhotoImage(Image.open(file))
        Card.draw.create_image(700,60, image=img)
        Card.draw.place(x=10,y=50)
        frame.place(x=694,y=51)

    def sortdata(sortkey): # User Sort Data
        if sortkey == 1:
            Card.df.sort_values(
                by=Card.clname[0], 
                key=lambda col: col.str.lower(),
                inplace=True,
                ascending=True
                )
        elif sortkey == 2:
            Card.df.sort_values(
                by=Card.clname[1],
                inplace=True,
                ascending=True
                )  
        elif sortkey == 3:
            Card.df.sort_values(
                by=Card.clname[2],
                inplace=True,
                ascending=True
                )
        elif sortkey == 4:
            Card.df.sort_values(
                by=Card.clname[3],
                inplace=True,
                ascending=True
                )
        elif sortkey == 5:
            Card.df.sort_values(
                by=Card.clname[4],
                inplace=True,
                ascending=True
                )
        elif sortkey == 6:
            Card.df.sort_values(
                by=Card.clname[5],
                inplace=True,
                ascending=True
                )
        Card.creategui()
        


    def addRecord(edit): # User Add Record

        def leaveDef():
            tl.destroy()
            nRecord.place_forget()
            Card.returntoMain()


        def saveRecord(): # User Save Record
            nameEty = str(name.get())
            strengthEty = int(strength.get())
            speedEty = int(speed.get())
            stealthEty = int(stealth.get())
            cunningEty = int(cunning.get())
            check = errorCheck(
                nameEty, 
                strengthEty, 
                speedEty, 
                stealthEty, 
                cunningEty)
            if (check[0]==0) and (check[1]==0):
                msgBox = messagebox.askquestion(
                    'Save the card?',
                    'Are you satified with the stats entered:\n'
                    +str(nameEty)+', '
                    +str(strengthEty)+', '
                    +str(speedEty)+', '
                    +str(stealthEty)+', '
                    +str(cunningEty))
                totalEty = strengthEty+speedEty+stealthEty+cunningEty
                df2 = pd.DataFrame([[
                    nameEty, 
                    strengthEty, 
                    speedEty, 
                    stealthEty, 
                    cunningEty,
                    totalEty,1
                    ]], 
                    columns=Card.clname)
                if msgBox == 'yes':
                    if edit == True:
                        Card.df = Card.df.drop(Card.record.get())
                    Card.df = pd.concat([Card.df, df2],ignore_index=True)
                    Card.df.to_csv(Card.FILENAME, index=False)
                    leaveDef()
                else:
                    Card.addRecord(edit=True)
            elif check[0] != 0 or check[1] != 0:
                if check[0] == 1:
                    text ="Name is empty"
                elif check[0] == 2:
                    text ="Strength is empty"
                elif check[0] == 3:
                    text ="Speed is empty"
                elif check[0] == 4:
                    text ="Stealth is empty"
                elif check[0] == 5:
                    text ="Cunning is empty"
                elif check[1] == 1:
                    text ="Name cannot contain other special characters"
                elif check[1] == 2:
                    text ="Strength is invalid.\nMust be above 0 and below 26"
                elif check[1] == 3:
                    text ="Speed is invalid.\nMust be above 0 and below 26"
                elif check[1] == 4:
                    text ="Stealth is invalid.\nMust be above 0 and below 26"
                elif check[1] == 5:
                    text ="Cunning is invalid.\nMust be above 0 and below 26"
                messagebox.showerror('Error',text)
                Card.eflag, Card.iflag = 0,0
                nRecord.place_forget()
                tl.destroy()
                Card.creategui()
                    

        def emptyValidation(strengthEty, speedEty, stealthEty, cunningEty):
            tic = time.perf_counter()
            if name.index("end") == 0:
                Card.eflag = 1
            elif len(str(strengthEty)) == 0:
                Card.eflag = 2
            elif len(str(speedEty)) == 0:
                Card.eflag = 3
            elif len(str(stealthEty)) == 0:
                Card.eflag = 4
            elif len(str(cunningEty)) == 0:
                Card.eflag = 5
            toc = time.perf_counter()
            print(f"{toc - tic:0.6f} seconds")
            return Card.eflag


        def invalidValidation(name,strength,speed,stealth,cunning):
            nameFlag = re.fullmatch(Card.NAMELIMIT, name)
            if nameFlag is None:
                Card.iflag = 1
            elif strength>Card.MAXPOINTS or strength<Card.MINPOINTS:
                Card.iflag = 2
            elif speed > Card.MAXPOINTS or speed < Card.MINPOINTS:
                Card.iflag = 3
            elif stealth>Card.MAXPOINTS or stealth<Card.MINPOINTS:
                Card.iflag = 4
            elif cunning>Card.MAXPOINTS or cunning<Card.MINPOINTS:
                Card.iflag = 5
            return Card.iflag


        def errorCheck(name,strength,speed,stealth,cunning):
            eMessage = emptyValidation(strength,speed,stealth,cunning)
            iMessage = invalidValidation(name,strength,speed,stealth,cunning)
            return eMessage, iMessage
        

        if Card.df[Card.df.columns[0]].count()<=Card.MAXCARDS:
            tl = Toplevel(bg='gray', height=300, width=200)
            Label(
                tl,
                text="Add New Record",
                font=Card.FONT,
                bg='gray').place(x=10, y=10)

            name = Entry(tl, bg='white', bd=0, width=14)
            strength = Entry(tl, bg='white', bd=0, width=14)
            speed = Entry(tl, bg='white', bd=0, width=14)
            stealth = Entry(tl, bg='white', bd=0, width=14)
            cunning = Entry(tl, bg='white', bd=0, width=14)
            nameL = Label(tl, text=Card.clname[0], bg='gray', bd=0)
            strengthL = Label(tl, text=Card.clname[1], bg='gray', bd=0)
            speedL = Label(tl, text=Card.clname[2], bg='gray', bd=0)
            stealthL = Label(tl, text=Card.clname[3], bg='gray', bd=0)
            cunningL = Label(tl, text=Card.clname[4], bg='gray', bd=0)

            userEntry = [name, strength, speed, stealth, cunning]
            entryLabel = [nameL, strengthL, speedL, stealthL, cunningL]
            Y = 50

            for i in range(len(userEntry)):
                entryLabel[i].place(x=10, y=Y)
                userEntry[i].place(x=60, y=Y)
                Y = Y+20

            Button(
                tl,
                text="Save",
                bg='white',
                bd=0,
                font=Card.FONT,
                command=saveRecord).place(x=11,y=250)
            Button(
                tl,
                text="Cancel",
                bg='white',
                bd=0,
                font=Card.FONT,
                command=leaveDef).place(x=66,y=250)            

            if edit == True:
                name.insert(0,Card.df[Card.clname[0]][Card.record.get()])
                strength.insert(0,Card.df[Card.clname[1]][Card.record.get()])
                speed.insert(0,Card.df[Card.clname[2]][Card.record.get()])
                stealth.insert(0,Card.df[Card.clname[3]][Card.record.get()])
                cunning.insert(0,Card.df[Card.clname[4]][Card.record.get()])
        
    def returntoMain(): # Return To Main
        Card.draw.delete(all)
        Card.filehandle()
        Card.creategui()


    def deleteRecord(row): # User Delete Record
        Card.df.drop(
            Card.df[Card.df[Card.clname[0]] == Card.df[Card.clname[0]][row]],
            inplace=True)
        Card.df.to_csv(Card.FILENAME, index=False)
        Card.returntoMain()


    def main():
        Card.creategui()
        mainloop()
