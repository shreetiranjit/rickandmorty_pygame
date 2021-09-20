from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

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
# rick.execute(('''CREATE TABLE registerA(
#               username text ,
#               email text ,
#               country text ,
#               password text ,
#               confirm_password text
#
#               )'''))
# print('Table created successfully.')


def signin():
    rick = sqlite3.connect("registration.db")
    r = rick.cursor()
    r.execute("INSERT INTO registerA VALUES(:username, :email, :country, :password, :confirm_password)", {
        'username': username_entry.get(),
        'email': email_entry.get(),
        'country': country_entry.get(),
        'password': pw_entry.get(),
        'confirm_password': confirm_pw_entry.get()
    })
    messagebox.showinfo("Success", "Your data has been inserted successfully .")
    rick_data = r.fetchall()
    print(rick_data)
    rick.commit()
    rick.close()
    username_entry.delete(0, END)
    email_entry.delete(0, END)
    country_entry.delete(0, END)
    pw_entry.delete(0, END)
    confirm_pw_entry.delete(0, END)



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
#username
global username_entry
user = StringVar()
user.set("Username")
def on_click(event):
    event.widget.delete(0, END)
username_entry = Entry(root, bg='black', fg='grey', width=40, bd=5 , font=('San Francisco', 10), textvariable= user )
username_entry.bind("<Button-1>", on_click)
username_entry.place(x=60, y=130, height=36 )

#email
mail = StringVar()
mail.set("E-mail")
email_entry = Entry(root, bg='black', fg='grey', width=40, bd=5, font=('San Francisco', 10), textvariable = mail )
email_entry.bind("<Button-1>", on_click)
email_entry.place(x=60, y=190, height=36)

#country
country = StringVar()
country.set("Country")
country_entry = Entry(root, bg='black', fg='grey', width=40, bd=5, font=('San Francisco', 10) , textvariable = country)
country_entry.bind("<Button-1>", on_click)
country_entry.place(x=60, y=250, height=36)

#password
global pw_entry
password = StringVar()
password.set("Password")
pw_entry = Entry(root, bg='black', fg='grey', width=40, bd=5, font=('San Francisco', 10) , textvariable = password)
pw_entry.bind("<Button-1>", on_click)
pw_entry.place(x=60, y=310, height=36)

#confirm_pw
confirm_pw = StringVar()
confirm_pw.set("Confirm Your Password")
confirm_pw_entry = Entry(root, bg='black', fg='grey', width=40, bd=5, font=('San Francisco', 10) , textvariable = confirm_pw)
confirm_pw_entry.bind("<Button-1>", on_click)
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
register_button = Button(root, image=reg_image, bd=0, bg='black' , command = signin)
register_button.place(x=135, y=410)

def login2():
    root.destroy()
    join = Toplevel()
    join.title('RICK AND MORTY MINI GAME')
    join.iconbitmap('C:/Users/Lenovo/OneDrive/Desktop/RM.ico')
    join.geometry('850x600')

    def login_data():
        morty = sqlite3.connect("registration.db")
        m = morty.cursor()
        name = username_entry1.get()
        password2 = pw_entry1.get()
        m.execute("SELECT * FROM registerA")
        record = m.fetchall()
        print(record)
        user_name = []
        password3 = []
        for records in record:
            user_name += [records[0]]
            password3 += [records[1]]
        print(user_name)
        print(password3)
        if name in user_name and password2 in password3:
            if user_name.index(name) == password3.index(password2):
                messagebox.showinfo('Success', 'Login Successful.')
            else:
                messagebox.showinfo("FAILED", "Invalid Username or Password")
        else:
            messagebox.showinfo("FAILED", "Invalid Username or Password")
        username_entry1.delete(0, END)
        pw_entry1.delete(0, END)
        morty.commit()
        morty.close()

    # Background image
    bg_image = Image.open("C:/Users/Lenovo/OneDrive/Desktop/starrick1.jpg")
    resizing_image = bg_image.resize((850, 600))
    resized_bg = ImageTk.PhotoImage(resizing_image)
    label1 = Label(join, image=resized_bg)
    label1.place(x=-2, y=0)

    # designing part of register frame
    f_image = Image.open("C:/Users/Lenovo/OneDrive/Desktop/starrick_side.jpg")
    f_image_resized = f_image.resize((350, 350))
    f_image_resized_bg = ImageTk.PhotoImage(f_image_resized)
    register_frame = Frame(join, height=350, width=350)
    frame_label = Label(join, image=f_image_resized_bg)
    register_frame.place(x=10, y=100)
    frame_label.place(x=10, y=100)

    title_image1 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/log_text.png")
    title_image_resized1 = title_image1.resize((260,50))
    final_title_image1 = ImageTk.PhotoImage(title_image_resized1)
    title_frame1 = Label(join, image=final_title_image1 , bd=0)
    title_frame1.place(x=50, y=115)

    h_icon_image1 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/R.jpg")
    h_icon_image_resized1 = h_icon_image1.resize((50,50))
    h_icon_title_image1 = ImageTk.PhotoImage(h_icon_image_resized1)
    h_icon_frame1 = Label(join, image=h_icon_title_image1 , bd=0)
    h_icon_frame1.place(x=270, y=173)

    h_icon_image2 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/mhead.jpg")
    h_icon_image_resized2 = h_icon_image2.resize((47,50))
    h_icon_title_image2 = ImageTk.PhotoImage(h_icon_image_resized2)
    h_icon_frame2 = Label(join, image=h_icon_title_image2 , bd=0)
    h_icon_frame2.place(x=60, y=173)

    b_icon_image1 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/rfull.jpg")
    b_icon_image_resized1 = b_icon_image1.resize((80,100))
    b_icon_title_image1 = ImageTk.PhotoImage(b_icon_image_resized1)
    b_icon_frame1 = Label(join, image=b_icon_title_image1 , bd=0)
    b_icon_frame1.place(x=250, y=229)

    b_icon_image2 = Image.open("C:/Users/Lenovo/OneDrive/Desktop/mfull.png")
    b_icon_image_resized2 = b_icon_image2.resize((80,110))
    b_icon_title_image2 = ImageTk.PhotoImage(b_icon_image_resized2)
    b_icon_frame2 = Label(join, image=b_icon_title_image2 , bd=0)
    b_icon_frame2.place(x=30, y=220)

    # creating text boxes
    # username
    user1 = StringVar()
    user1.set(" Enter Your Username")
    def on_click1(event):
        event.widget.delete(0, END)
    username_entry1 = Entry(join, bg='black', fg='grey', width=40, bd=5, textvariable=user1)
    username_entry1.bind("<Button-1>", on_click1)
    username_entry1.place(x=60, y=220, height=36)

    # password
    password1 = StringVar()
    password1.set(" Enter Your Password")
    pw_entry1 = Entry(join, bg='black', fg='grey', width=40, bd=5, textvariable=password1)
    pw_entry1.bind("<Button-1>", on_click1)
    pw_entry1.place(x=60, y=320, height=36)

    # creating button
    log_icon = Image.open("C:/Users/Lenovo/OneDrive/Desktop/LOG.png")
    log_resized = log_icon.resize((150,50))
    log_image = ImageTk.PhotoImage(log_resized)
    log_button = Button(join, image=log_image, bd=0, bg='black', command=login_data)
    log_button.place(x=110, y=380)

    join.mainloop()
login_button = Button(root, text='Already have an account ? Click Here!!!', fg='#08E5DB', bg='black'
                      , font=('San Francisco', 11, 'bold'), bd=0 , command=login2 )
login_button.place(x=57, y=449)
root.mainloop()
