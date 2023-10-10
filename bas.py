from tkinter import *
from tkinter import messagebox

top=Tk()
top.geometry("800x700")
c=Canvas(top,bg="gray16",height=200,width=200)
filename=PhotoImage(file="C://Users//feed_//Desktop//background.png")
background_label=Label(top,image=filename)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

c.pack()
top.mainloop()