from tkinter import *
from PIL import ImageTk , Image
root = Tk()
root.title('RICK AND MORTY INVADES SPACE ')
root.iconbitmap('C:/Users/Lenovo/OneDrive/Desktop/RM.ico')
root.geometry('850x600')

# Background image
bg_image = Image.open("C:/Users/Lenovo/OneDrive/Desktop/morty.jpg")
resizing_image = bg_image.resize((850, 600))
resized_bg = ImageTk.PhotoImage(resizing_image)
label1 = Label(root, image=resized_bg)
label1.place(x=-2, y=0)


mainloop()