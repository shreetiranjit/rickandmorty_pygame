from tkinter import *
import sqlite3
from PIL import ImageTk, Image
root = Tk()
root.title('RICK AND MORTY MINI GAME')
root.iconbitmap('C:/Users/Lenovo/OneDrive/Desktop/RM.ico')
root.geometry('850x600')

# Background image
bg_image = Image.open("C:/Users/Lenovo/OneDrive/Desktop/starrick1.jpg")
resizing_image = bg_image.resize((850, 600))
resized_bg = ImageTk.PhotoImage(resizing_image)
label1 = Label(root, image=resized_bg)
label1.place(x=-2, y=0)




# designing part of register frame
f_image = Image.open("C:/Users/Lenovo/OneDrive/Desktop/starrick_side.jpg")
f_image_resized = f_image.resize((350, 350))
f_image_resized_bg = ImageTk.PhotoImage(f_image_resized)
register_frame = Frame(root, height=350, width=350)
frame_label = Label(root, image=f_image_resized_bg)
register_frame.place(x=10, y=100)
frame_label.place(x=10, y=100)

title_image1 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/log_text.png")
title_image_resized1 = title_image1.resize((260,50))
final_title_image1 = ImageTk.PhotoImage(title_image_resized1)
title_frame1 = Label(root, image=final_title_image1 , bd=0)
title_frame1.place(x=50, y=115)

h_icon_image1 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/R.jpg")
h_icon_image_resized1 = h_icon_image1.resize((50,52))
h_icon_title_image1 = ImageTk.PhotoImage(h_icon_image_resized1)
h_icon_frame1 = Label(root, image=h_icon_title_image1 , bd=0)
h_icon_frame1.place(x=270, y=173)

h_icon_image2 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/mhead.jpg")
h_icon_image_resized2 = h_icon_image2.resize((47,52))
h_icon_title_image2 = ImageTk.PhotoImage(h_icon_image_resized2)
h_icon_frame2 = Label(root, image=h_icon_title_image2 , bd=0)
h_icon_frame2.place(x=60, y=173)

b_icon_image1 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/rfull.jpg")
b_icon_image_resized1 = b_icon_image1.resize((80,90))
b_icon_title_image1 = ImageTk.PhotoImage(b_icon_image_resized1)
b_icon_frame1 = Label(root, image=b_icon_title_image1 , bd=0)
b_icon_frame1.place(x=250, y=232)

b_icon_image2 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/mfull.png")
b_icon_image_resized2 = b_icon_image2.resize((80,110))
b_icon_title_image2 = ImageTk.PhotoImage(b_icon_image_resized2)
b_icon_frame2 = Label(root, image=b_icon_title_image2 , bd=0)
b_icon_frame2.place(x=30, y=220)





# creating text boxes
username_entry = Entry(root, bg='black', fg='grey', width=40, bd=5 )
username_entry.place(x=60, y=220, height=36 )
pw_entry = Entry(root, bg='black', fg='grey', width=40, bd=5)
pw_entry.place(x=60, y=320, height=36)


# icons for text boxes
# user
# user_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/user.png")
# u_resized = user_icon.resize((20,20))
# user_image = ImageTk.PhotoImage(u_resized)
# user_label = Label(root , image = user_image, bg='black')
# user_label.place(x=32 , y = 144)
#
# # password
# pw_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/pw.png")
# pw_resized = pw_icon.resize((25,25))
# pw_image = ImageTk.PhotoImage(pw_resized)
# pw_label = Label(root , image =pw_image, bg='black')
# pw_label.place(x=32 , y = 324)

# creating button
log_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/LOG.png")
log_resized = log_icon.resize((150,50))
log_image = ImageTk.PhotoImage(log_resized)
log_button = Button(root, image=log_image, bd=0, bg='black')
log_button.place(x=110, y=380)

root.mainloop()