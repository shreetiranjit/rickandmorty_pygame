import pygame
import sys
import numpy as np
import time

# initializing pygame
pygame.init()
pygame.mixer.init()

width = 600
heigth = 600
line_width = 10
board_rows = 3
board_column = 3
circle_radius = 60
circle_width = 15
cross_width = 25
# space = 55

# rgb
screen_colour = (255, 255, 255)
bg_color = (0, 0, 0)
line_color = (255,255,255)
color = (255,0,0)

# creating screen
screen = pygame.display.set_mode((width , heigth))
pygame.display.set_caption('TIC - TAC - TOE (RICK AND MORTY)')
look_1 = pygame.image.load("C:/Users/Lenovo/Downloads/rickrackroe.jpg").convert_alpha()
background = pygame.transform.smoothscale(look_1, (width, heigth))

# board
board = np.zeros((board_rows, board_column))

# music
red_circle = pygame.mixer.Sound("C:/Users/Lenovo/Downloads/hitler.mp3")
win = pygame.mixer.Sound("C:/Users/Lenovo/Downloads/heckyeah.mp3")


def draw_lines():
    # first_horizontal_line
    pygame.draw.line(background, line_color, (0,200), (600, 200),line_width )
    # second_horizontal_line
    pygame.draw.line(background, line_color, (0, 400), (600, 400), line_width)

    # first_vertical_line
    pygame.draw.line(background, line_color, (200, 0), (200, 600), line_width)
    # second_vertical_line
    pygame.draw.line(background, line_color, (400, 0), (400, 600), line_width)


def draw_figures():
    for row in range(board_rows):
        for col in range(board_column):
            if board[row][col] == 1:
                pygame.draw.circle(background, line_color, (int(col * 200 + 100), int(row * 200 + 100)),
                                   circle_radius, circle_width)
            elif board[row][col] == 2:
                pygame.draw.circle(background, color, (int(col * 200 + 100), int(row * 200 + 100)),
                                   circle_radius, circle_width)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row,col):
    if board[row][col] == 0:
        return True
    else:
        return False


def is_board_full():
    for row in range(board_rows):
        for column in range(board_column):
            if board[row][column] == 0 :
                return False
    else :
        return True


def check_win(player):
    # vertical win check
    for col in range(board_column):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_line_winning(col, player)
            return True

    # horizontal win check
    for row in range(board_column):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_line_winning(row, player)
            return True

    # ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal_line_winning(player)
        return True

    # descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_des_diagonal_line_winning(player)
        return True

    return False


def draw_vertical_line_winning(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = line_color
    elif player == 2:
        color = line_color

    pygame.mixer.Sound.play(win)
    pygame.draw.line(background, screen_colour, (posX, 15) , (posX, heigth - 15),15)
    pygame.mixer.music.stop()




def draw_horizontal_line_winning(row, player):
    posY = row *200 + 100
    if player == 1:
        color = line_color
    elif player == 2:
        color = line_color

    pygame.mixer.Sound.play(win)
    pygame.draw.line(background, screen_colour, (15,posY), (width-15 , posY), 15)
    pygame.mixer.music.stop()



def draw_asc_diagonal_line_winning(player):
    if player == 1:
        color = line_color
    elif player == 2:
        color = line_color
    pygame.mixer.Sound.play(win)
    pygame.draw.line(background, screen_colour, (15, heigth - 15), (width - 15, 15), 15)
    pygame.mixer.music.stop()



def draw_des_diagonal_line_winning(player):
    if player == 1:
        color = line_color
    elif player == 2:
        color = line_color
    pygame.mixer.Sound.play(win)
    pygame.draw.line(background, screen_colour, (15, 15), (width - 15, heigth - 15), 15)
    pygame.mixer.music.stop()




def text_object(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def restart():
    time.sleep(3)
    XO = 'x'
    game_over = False
    main()
    # screen.blit(background, (0,0))
    # draw_lines()
    # # player = 1
    # for row in range(board_rows):
    #     for col in range(board_column):
    #         board[row][col] = 0


draw_lines()



def main():
    player = 1
    game_over = False
    # game loop
    while True:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                clicked_row = int(mouseY // 200)
                clicked_col = int(mouseX // 200)

                if available_square(clicked_row, clicked_col):
                    if player == 1:
                        mark_square(clicked_row, clicked_col, 1)
                        if check_win(player):
                            game_over = True


                        player = 2

                    elif player == 2:
                        pygame.mixer.Sound.play(red_circle)
                        mark_square(clicked_row, clicked_col, 2)
                        if check_win(player):
                             game_over = True


                        player = 1
                        pygame.mixer.music.stop()
                    draw_figures()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()

        pygame.display.update()


main()
