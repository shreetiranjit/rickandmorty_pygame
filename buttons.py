"""this module is for choosing the games and to see the instructions."""

from tkinter import*
from PIL import ImageTk, Image
from tiktactoe import *
from pong import *
from snakegame import *
from dinogame import *
def button():
    root = Toplevel()
    root.geometry('700x600')
    root.title('RICK AND MORTY MINI-GAME')
    root.iconbitmap('C:/Users/Lenovo/OneDrive/Desktop/RM.ico')
    # background images
    bg_image = Image.open("C:/Users/Lenovo/Downloads/fam.jpg")
    bg1 = ImageTk.PhotoImage(bg_image)
    resizing_image = bg_image.resize((700, 700))
    resized_bg = ImageTk.PhotoImage(resizing_image)
    label1 = Label(root, image=resized_bg)
    label1.place(x=-2, y=0)

    text1_image = Image.open("C:/Users/Lenovo/Downloads/button1.png")
    resizing_text_image = text1_image.resize((220,45))
    resized_text_image = ImageTk.PhotoImage(resizing_text_image)
    text1_label = Label(root, image = resized_text_image , bd = 0 )
    text1_label.place(x = 42 , y = 62 )

    text2_image = Image.open("C:/Users/Lenovo/Downloads/button2.png")
    resizing_text2_image = text2_image.resize((150,35))
    resized_text2_image = ImageTk.PhotoImage(resizing_text2_image)
    text2_label = Label(root, image = resized_text2_image , bd = 0 )
    text2_label.place(x = 82 , y = 112 )

    def game1():
        rick()

    def game2():
        ping()

    def game3():
        snake12()

    def game4():
        dino12()

    # buttons
    dino_image = PhotoImage(file = r"C:/Users/Lenovo/Downloads/dino.png")
    dino = Button(root, image = dino_image, command = game4)
    dino.place(x= 10, y = 550)

    snake_image = PhotoImage(file=r"C:/Users/Lenovo/Downloads/snake.png")
    snake = Button(root, image = snake_image, command = game3)
    snake.place(x= 70, y = 550)

    pong_image = PhotoImage(file = r"C:/Users/Lenovo/Downloads/pong.png")
    pong= Button(root, image = pong_image, command = game2)
    pong.place(x= 130, y = 550)

    tack_image = PhotoImage(file = r"C:/Users/Lenovo/Downloads/tic.png")
    tack = Button(root,image = tack_image, command = game1)
    tack.place(x= 190, y =550)


    def inst():
        root1 = Toplevel()
        root1.geometry('700x650')
        root1.title('INSTRUCTIONS FOR RICK AND MORTY MINI-GAME')
        root1.iconbitmap('C:/Users/Lenovo/OneDrive/Desktop/RM.ico')

        bg_image1 = Image.open("C:/Users/Lenovo/Downloads/ii.png")
        resizing_image1 = bg_image1.resize((700, 650))
        resized_bg1 = ImageTk.PhotoImage(resizing_image1)
        label12 = Label(root1, image=resized_bg1)
        label12.place(x=-2, y=0)

        mainloop()


    instructions = Button(root,text = " Click Here For Instructions" , font = ("Calibre", 14) , fg = "green", command = inst)
    instructions.place(x= 455, y =400)


    mainloop()





