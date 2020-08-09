# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import numpy
import os
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import math
from tkinter import messagebox
import random



#INTEGRALS
root = Tk()
root.geometry('2400x2400')
root.title ('Heat Capacity Calculator')
frame = Frame(root)
frame.pack()

#VISUALS
canvas = Canvas(root, width = 2400, height = 2400, background='black')

root.state('zoomed')
canvas.place(x=0, y=0)

#INFORMATION and MATHEMATICAL CALCULATIONS
canvas.create_text(950, 100, text = 'Heat Capacity Calculator', font = ('Times New Roman', 70), justify = 'center', fill='white smoke')
canvas.create_text(950, 200, text = 'Instructions: Input numerical data below to solve for an unknown component', font = ('Times New Roman', 15), justify = 'center', fill='white smoke')
canvas.create_text(190, 800, text = 'Reference', font = ('Times New Roman', 25), justify = 'center', fill='white smoke')
canvas.create_text(900, 350, text = 'Q = m c △T', font = ('Times New Roman', 50), justify = 'right', fill='white smoke')
canvas.create_text(200, 850, text = 'Q = heat capacity (J) ', font = ('Times New Roman', 15), justify = 'right', fill='white smoke')
canvas.create_text(169, 880, text = 'm = mass (g) ', font = ('Times New Roman', 15), justify = 'right', fill='white smoke')
canvas.create_text(308, 910, text = 'c = specific heat capacity of substance (J/g°C) ', font = ('Times New Roman', 15), justify = 'right', fill='white smoke')
canvas.create_text(235, 940, text = '△T = change in temperature (°C) ', font = ('Times New Roman', 15), justify = 'right', fill='white smoke')
canvas.create_text(1750, 940, text = 'Vishnu Vijayakumar', font = ('Times New Roman', 15), justify = 'right', fill='white smoke')
canvas.create_text(1750, 970, text = 'May 2020', font = ('Times New Roman', 13), justify = 'right', fill='white smoke')
var = IntVar()
a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()

a.set("")
b.set("")
c.set("")
d.set("")


def multiplication():
    if len(entry1.get()) == 0:
        output = float(entry2.get()) * float(entry3.get()) * float(entry4.get())
        entry1.insert(0, output) 
    elif len(entry2.get()) == 0:
        output = float(entry1.get()) / (float(entry3.get()) * float(entry4.get()))
        entry2.insert(0, output)
    elif len(entry3.get()) == 0:
        output = float(entry1.get()) / (float(entry2.get()) * float(entry4.get()))
        entry3.insert(0, output)
    elif len(entry4.get()) == 0:
        output = float(entry1.get()) / (float(entry2.get()) * float(entry3.get()))
        entry4.insert(0, output)
           
def errorhighlow():
    len(entry1.get()) 
    len(entry2.get()) 
    len(entry3.get()) 
    len(entry4.get()) 
    if len(entry1.get()) == 1 and len(entry2.get()) ==1:
        if len(entry3.get()) == 1:
            if len(entry4.get()) == 1:
                messagebox.showerror("Error", "Please delete a value")
    else:
        pass
    if len(entry1.get()) == 0 and len(entry2.get()) ==0:
           messagebox.showerror("Error", "Please input 3 values")
    if len(entry1.get()) == 0 and len(entry3.get()) ==0:
           messagebox.showerror("Error", "Please input 3 values")
    if len(entry1.get()) == 0 and len(entry4.get()) ==0:
           messagebox.showerror("Error", "Please input 3 values")         
    if len(entry2.get()) == 0 and len(entry3.get()) ==0:
           messagebox.showerror("Error", "Please input 3 values")
    if len(entry2.get()) == 0 and len(entry4.get()) ==0:
           messagebox.showerror("Error", "Please input 3 values")
    if len(entry3.get()) == 0 and len(entry4.get()) ==0:
           messagebox.showerror("Error", "Please input 3 values")                                
    else:
       multiplication() 
                    
button1=Button(canvas, text="Solve", fg="black",bg='white smoke', borderwidth=0, command=errorhighlow)
button1.place(x=840, y=465)
                               
                                         
        
def ClearAll():
    a.set("")
    b.set("")
    c.set("")
    d.set("")
    


entry1 = tk.Entry(canvas, textvariable=a)
canvas.create_window(764, 400, window=entry1, height=20, width=45)
entry1.configure(bg='white smoke', borderwidth=0)

entry2 = tk.Entry(canvas, textvariable=b)
canvas.create_window(882, 400, window=entry2, height=20, width=45)
entry2.configure(bg='white smoke', borderwidth=0)

entry3 = tk.Entry(canvas, textvariable=c)
canvas.create_window(940, 400, window=entry3, height=20, width=45)
entry3.configure(bg='white smoke', borderwidth=0)

entry4 = tk.Entry(canvas, textvariable=d)
canvas.create_window(1025, 400, window=entry4, height=20, width=45)
entry4.configure(bg='white smoke', borderwidth=0)


  
button1=Button(canvas, text="Solve", fg="black",bg='white smoke', borderwidth=0, command=errorhighlow)
button1.place(x=840, y=465)

button2=Button(canvas, text="Clear All", fg="black",bg='white smoke', borderwidth=0, command=ClearAll)
button2.place(x=900, y=465)


root.update()
canvas.pack()
root.mainloop()
root.destroy()




