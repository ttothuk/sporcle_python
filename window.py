import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import *


# Adding function
def addCountry():
    print("hi there, everyone!")


drawing = svg2rlg("world.svg")
renderPM.drawToFile(drawing, "temp.png", fmt="PNG")

# Creating a list
country_list = ["Hungary", "Bulgaria", "Italy"]

root = tk.Tk()

# Canvas
canvas = tk.Canvas(root, width=700, height=700, bg="grey")
canvas.pack()

# Frame
frame = tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.15, relx=0.1, rely=0.1)

# Map Frame
frame2 = tk.Frame(root, bg="black")
frame2.place(relwidth=0.8, relheight=0.65, relx=0.1, rely=0.3)

# Add Button
addButton = tk.Button(frame, text="Add", bg="red", command=addCountry)
addButton.pack()

# Add Text
addText = tk.Text(frame)
addText.pack()

addText.insert(tk.INSERT, "Line Line Line")

root.wm_title("Tkinter window")
root.mainloop()
