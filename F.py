from tkinter import *

window=Tk()
#vars
Ftokens=IntVar(value=0)
#----
#funcs
def buy():
    global Ftokens
    ft=str(Ftokens.get())
    Ftokens.set(+10)
    Label(textvariable=ft).grid(column=9, row=0)
#-----
Button(text="Buy",command=buy).grid(column=0,row=1)
window.mainloop()