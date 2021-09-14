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

# creating and connecting  database for registration
rick_db = sqlite3.connect('registration.db')
# creating a  cursor
rick = rick_db.cursor()
# creating a table in database
# rick.execute(('''CREATE TABLE register(
#               username text ,
#               full_name text ,
#               email text ,
#               country text ,
#               password text ,
#               confirm password text ,
#
# )'''))


# designing part of register frame
f_image = Image.open("C:/Users/Lenovo/OneDrive/Desktop/starrick_side.jpg")
f_image_resized = f_image.resize((360, 420))
f_image_resized_bg = ImageTk.PhotoImage(f_image_resized)
register_frame = Frame(root, height=420, width=360)
frame_label = Label(root, image=f_image_resized_bg)
register_frame.place(x=10, y=60)
frame_label.place(x=10, y=60)
title_image = Image.open("C:/Users/Lenovo/OneDrive/Desktop/w1.png")
title_image_resized = title_image.resize((220,40))
final_title_image = ImageTk.PhotoImage(title_image_resized)
title_frame = Label(root, image=final_title_image , bd=0)
title_frame.place(x=90, y=70)

# creating text boxes
username_entry = Entry(root, bg='black', fg='grey', width=40, bd=5 , font=('San Francisco', 10))
username_entry.place(x=60, y=130, height=36 )
email_entry = Entry(root, bg='black', fg='grey', width=40, bd=5, font=('San Francisco', 10))
email_entry.place(x=60, y=190, height=36)
country_entry = Entry(root, bg='black', fg='grey', width=40, bd=5, font=('San Francisco', 10))
country_entry.place(x=60, y=250, height=36)
pw_entry = Entry(root, bg='black', fg='grey', width=40, bd=5, font=('San Francisco', 10))
pw_entry.place(x=60, y=310, height=36)
confirm_pw_entry = Entry(root, bg='black', fg='grey', width=40, bd=5, font=('San Francisco', 10))
confirm_pw_entry.place(x=60, y=370, height=36)

# icons for text boxes
# user
user_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/user.png")
u_resized = user_icon.resize((20,20))
user_image = ImageTk.PhotoImage(u_resized)
user_label = Label(root, image=user_image, bg='black')
user_label.place(x=32, y=134)

# email
email_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/mail.png")
e_resized = email_icon.resize((20, 20))
email_image = ImageTk.PhotoImage(e_resized)
email_label = Label(root, image=email_image, bg='black')
email_label.place(x=32, y=194)

# country
country_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/country.png")
c_resized = country_icon.resize((25, 25))
country_image = ImageTk.PhotoImage(c_resized)
country_label = Label(root, image=country_image, bg='black')
country_label.place(x=32, y=254)

# password
pw_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/pw.png")
pw_resized = pw_icon.resize((25,25))
pw_image = ImageTk.PhotoImage(pw_resized)
pw_label = Label(root, image=pw_image, bg='black')
pw_label.place(x=32, y=314)

# confirm password
c_pw_label = Label(root, image=pw_image, bg='black')
c_pw_label.place(x=32, y=374)


# creating buttons
reg_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/py_register.png")
reg_resized = reg_icon.resize((100,40))
reg_image = ImageTk.PhotoImage(reg_resized)
register_button = Button(root, image=reg_image, bd=0, bg='black')
register_button.place(x=135, y=410)

login_button = Button(root, text='Already have an account ? Click Here!!!', fg='#08E5DB', bg='black', font=('San Francisco', 11, 'bold'), bd=0)
login_button.place(x=57, y=449)
root.mainloop()