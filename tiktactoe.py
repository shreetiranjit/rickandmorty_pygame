import pygame
import sys
from pygame.locals import *
import time
def rick():

    pygame.mixer.init()

    # initializing global constants
    global RM
    global draw
    global winner
    RM = 'x'
    winner = None
    draw = False
    width = 400
    height = 400
    white = (255, 255, 255)
    line_color = (10,10,10)

    #initializing pygame window
    pygame.init()
    fps = 30
    CLOCK = pygame.time.Clock()

    screen = pygame.display.set_mode((width, height+100),0,32)
    pygame.display.set_caption("Tic Tac Toe (Rick - And - Morty )")



    # 3x3 board
    global RMRM
    RMRM = [[None]*3,[None]*3,[None]*3]

    # loading the images
    opening = pygame.image.load('C:/Users/Lenovo/Downloads/rickrackroe.jpg')
    morty_head_img = pygame.image.load('C:/Users/Lenovo/Downloads/morty_head.jpg')
    rick_head_img = pygame.image.load('C:/Users/Lenovo/Downloads/rick_head.jpg')
    # resizing images
    mhead_img = pygame.transform.scale(morty_head_img, (80,80))
    rhead_img = pygame.transform.scale(rick_head_img, (80,80))
    opening = pygame.transform.scale(opening, (width, height+100))

    # Background music
    pygame.mixer.music.load('C:/Users/Lenovo/Downloads/theme.mp3')
    pygame.mixer.music.play(-1)


    def game_opening():
        """thus function creates front ag"""
        screen.blit(opening,(0, 0))
        pygame.display.update()
        time.sleep(1)
        screen.blit(opening, (0, 0))
        # Drawing vertical lines
        pygame.draw.line(screen, line_color, (width/3, 0), (width/3, height), 7)
        pygame.draw.line(screen, line_color, (width/3*2, 0), (width/3*2, height), 7)
        # Drawing horizontal lines
        pygame.draw.line(screen, line_color, (0,height/3), (width, height/3), 7)
        pygame.draw.line(screen, line_color, (0,height/3*2), (width, height/3*2), 7)
        draw_status()

    def draw_status():
        global draw
        if winner is None:
            message = RM.upper() + "'s Turn"
        else:
            message = winner.upper() + " won!"
        if draw:
            message = 'Game Draw!'
        font = pygame.font.Font(None, 30)
        text = font.render(message, 1, (255, 255, 255))
        # copy the rendered message onto the board
        screen.fill ((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(width/2, 500-50))
        screen.blit(text, text_rect)
        pygame.display.update()

    def check_win():
        global TTT, winner,draw
        # check for winning rows
        for row in range (0,3):
            if ((RMRM[row][0] == RMRM[row][1] == RMRM[row][2]) and(RMRM[row][0] is not None)):
                # this row won
                winner = RMRM[row][0]
                one = pygame.mixer.Sound('C:/Users/Lenovo/Downloads/youwin.mp3')
                one.play()
                pygame.draw.line(screen, (250, 0, 0), (0, (row + 1)*height/3 - height/6),\
                                  (width, (row + 1)*height/3 - height/6), 4)
                break

        # check for winning columns
        for col in range (0, 3):
            if (RMRM[0][col] == RMRM[1][col] == RMRM[2][col]) and (RMRM[0][col] is not None):
                # this column won
                winner = RMRM[0][col]
                one = pygame.mixer.Sound('C:/Users/Lenovo/Downloads/youwin.mp3')
                one.play()
                # winning line
                pygame.draw.line(screen, (250,0,0),((col + 1)* width/3 - width/6, 0), \
                              ((col + 1)* width/3 - width/6, height), 4)
                break
        # check for diagonal winners
        if (RMRM[0][0] == RMRM[1][1] == RMRM[2][2]) and (RMRM[0][0] is not None):
            # game won diagonally left to right
            winner = RMRM[0][0]
            pygame.mixer.music.stop()
            one = pygame.mixer.Sound('C:/Users/Lenovo/Downloads/youwin.mp3')
            one.play()
            pygame.draw.line (screen, (250,70,70), (50, 50), (350, 350), 4)
        if (RMRM[0][2] == RMRM[1][1] == RMRM[2][0]) and (RMRM[0][2] is not None):
            # game won diagonally right to left
            winner = RMRM[0][2]
            pygame.mixer.music.stop()
            one = pygame.mixer.Sound('C:/Users/Lenovo/Downloads/youwin.mp3')
            one.play()
            pygame.draw.line (screen, (250,70,70), (350, 50), (50, 350), 4)
        if(all([all(row) for row in RMRM]) and winner is None ):
            draw = True
        draw_status()

    def drawXO(row,col):
        global RMRM,RM
        if row==1:
            posx = 30
        if row==2:
            posx = width/3 + 30
        if row==3:
            posx = width/3*2 + 30
        if col==1:
            posy = 30
        if col==2:
            posy = height/3 + 30
        if col==3:
            posy = height/3*2 + 30
        RMRM[row-1][col-1] = RM
        if(RM == 'x'):
            screen.blit(mhead_img,(posy,posx))
            RM = 'o'
        else:
            screen.blit(rhead_img,(posy,posx))
            RM = 'x'
        pygame.display.update()


    def on_click():
        # gets coordinates of mouse click
        x, y = pygame.mouse.get_pos()
        # gets column of mouse click (1-3)
        if x < width/3:
            col = 1
        elif x < width/3*2:
            col = 2
        elif x < width:
            col = 3
        else:
            col = None

        # gets row of mouse click (1-3)
        if y < height/3:
            row = 1
        elif y < height / 3 * 2:
            row = 2
        elif y < height:
            row = 3
        else:
            row = None

        if row and col and RMRM[row-1][col-1] is None:
            global RM
            # draws the x or o on screen
            drawXO(row, col)
            check_win()
        click = pygame.mixer.Sound('C:/Users/Lenovo/Downloads/click.wav')
        click.play()

    def reset_game():
        """this function restarts the game."""
        global RMRM, winner,RM, draw
        time.sleep(1)
        RM = 'x'
        draw = False
        game_opening()
        winner=None
        RMRM = [[None]*3,[None]*3,[None]*3]


    game_opening()
    def gameloop():
        """this funtion runs the game loop forever."""
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    # the user clicked; place an X or O
                    on_click()
                    if winner or draw:
                        reset_game()

    pygame.display.update()
    CLOCK.tick(fps)
    gameloop()
