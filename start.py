

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x600")
root.title("Face Recognition System")

# Load the background image
background_image = Image.open("/home/apiiit-rkv/Desktop/sai/MAJOR/sreevani.png")  # Change "background_image.jpg" to your image file path
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to navigate to the registration page
def savedata():
    root.destroy()
    import majorproject

# Function to navigate to the face scan page
def fetch():
    root.destroy()
    import fetch_data

# Title label
title_label = Label(root, text="Welcome to Missing Person Identification System", 
                    font=("Helvetica", 20, "bold italic"), 
                    bg="blue", fg="yellow")
title_label.pack(pady=50)
"""# Registration button
reg_button = Button(root, text="REGISTRATION", font="Arial 15 bold", width=20, height=2, bg="yellow", command=savedata)
reg_button.pack(pady=20)

# Face scan button
scan_button = Button(root, text="FACE SCAN", font="Arial 15 bold", width=20, height=2, bg="yellow", command=fetch)
scan_button.pack(pady=20)"""

# Registration button with styled parameters
reg_button = Button(root, text="REGISTRATION", font=("Arial", 15, "bold"), width=20, height=2, bg="green", fg="white", relief="raised", borderwidth=3, command=savedata)
reg_button.pack(pady=20)

# Face scan button with styled parameters
scan_button = Button(root, text="FACE SCAN", font=("Arial", 15, "bold"), width=20, height=2, bg="green", fg="white", relief="raised", borderwidth=3, command=fetch)
scan_button.pack(pady=20)


root.mainloop()


