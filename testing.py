import tkinter

# init tk
root = tkinter.Tk()

# create canvas
myCanvas = tkinter.Canvas(root, bg="white", height=300, width=300)

myCanvas.create_rectangle(0,0,100,100,fill="blue")

# add to window and show
myCanvas.pack()
root.mainloop()