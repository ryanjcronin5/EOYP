import numpy as np
import pandas as pd
from threading import Thread as td
from tkinter import *

class functions():
    def __init__(self):
        pass


    def RDF(): # Read Data File
        df = pd.read_csv('mcards.csv')


    def GUI(): # Graphical User Inferface
        root = Tk()
        root.title('Monster Card Games')
        mainloop()


    def BWR(): #Button Wait Request
        print("Started")


    def TCF(): # Thread Call Function
        t1 = td(target=functions.RDF) # Thread 1 for Read Data File
        t2 = td(target=functions.GUI) # Thread 2 for Graphical User Interface
        t1.start()
        t2.start()
        t1.join()
        t2.join()
