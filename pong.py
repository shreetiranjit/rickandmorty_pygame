import pygame
import time

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
# setting the main screen
width = 600
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ping-Pong')
# RBG
white = (255, 255, 255)
black = (0, 0, 0)

# background images
look_1 = pygame.image.load("C:/Users/Lenovo/Downloads/p.jpg").convert_alpha()
background = pygame.transform.smoothscale(look_1, (width, height))

# game constants
game_font = pygame.font.SysFont('Ubuntu', 40)
delay = 30
paddle_speed = 55
paddle_width = 10
paddle_height = 100
player1_x_pos = 10
player1_y_pos = height / 2 - paddle_height / 2
player2_x_pos = 580
player2_y_pos = height / 2 - paddle_height / 2
player1_Score = 0
player2_Score = 0
# False so we can control the up and down process
player1_up = False
player1_down = False
player2_up = False
player2_down = False
# position for ball
ball_x_pos = width / 2
ball_y_pos = height / 2
ball_width = 8
# because we want ball to go in one dire
ball_x_velocity = -10
ball_y_velocity = 0
def draw_figures():
    pygame.draw.rect(screen, white, (int(player1_x_pos), int(player1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (int(player2_x_pos), int(player2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x_pos, ball_y_pos), ball_width)
    score = game_font.render(f"{str(player1_Score)}- {str(player2_Score)}", False, white)
    screen.blit(score, (width / 2, 30))


def ball_movement():
    global ball_x_pos
    global ball_y_pos
    global ball_x_velocity
    global ball_y_velocity
    global player1_Score
    global player2_Score
    if (ball_x_pos + ball_x_velocity < player1_x_pos + paddle_width) and (player1_y_pos < ball_y_pos + ball_y_velocity
                                                                          + ball_width < player1_y_pos + paddle_height):
        ball_x_velocity = -ball_x_velocity
        ball_y_velocity = (player1_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_velocity = - ball_y_velocity
    elif ball_x_pos + ball_x_velocity < 0:
        player2_Score += 1
        ball_x_pos = width / 2
        ball_y_pos = height / 2
        ball_x_velocity = 10
        ball_y_velocity = 0
    if (ball_x_pos + ball_x_velocity > player2_x_pos - paddle_width) and (player2_y_pos < ball_y_pos + ball_y_velocity +
                                                                          ball_width < player2_y_pos + paddle_height):
        ball_x_velocity = -ball_x_velocity
        ball_y_velocity = (player2_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_velocity = - ball_y_velocity
    elif ball_x_pos + ball_x_velocity > height:
        player1_Score += 1
        ball_x_pos = width / 2
        ball_y_pos = height / 2
        ball_x_velocity = -10
        ball_y_velocity = 0
    if ball_y_pos + ball_y_velocity > height or ball_y_pos + ball_y_velocity < 0:
        ball_y_velocity = - ball_y_velocity
    ball_x_pos += ball_x_velocity
    ball_y_pos += ball_y_velocity

def gameover():
    font = game_font.render("you have miseed 5 times, Game over", True , (255, 255, 255))
    screen.blit(font, (15,15))
    font1 = game_font.render("Please press 'R' to restart.", True, (255, 255, 255))
    screen.blit(font1, (15, 60))


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_loop()

# game-loop

def game_loop():
    global player2_y_pos
    global player1_y_pos
    global player2_x_pos
    global player1_x_pos
    player1_x_pos = 10
    player1_y_pos = height / 2 - paddle_height / 2
    player2_x_pos = 580
    player2_y_pos = height / 2 - paddle_height / 2
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_y_pos = max(player1_y_pos - paddle_speed, 0)
                if event.key == pygame.K_s:
                    player1_y_pos = min(player1_y_pos + paddle_speed, height)
                if event.key == pygame.K_UP:
                    player2_y_pos = max(player2_y_pos - paddle_speed, 0)
                if event.key == pygame.K_DOWN:
                    player2_y_pos = min(player2_y_pos + paddle_speed, height)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1_up = False
                    player1_down = False
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2_up = False
                    player2_down = False
        screen.blit(background, (0, 0))
        ball_movement()
        if player1_Score == 5 or player2_Score == 5:
            screen.blit(background, (0, 0))
            gameover()
            pygame.display.update()
            game_loop()
            break
        # player_movement()
        draw_figures()
        pygame.display.flip()
        pygame.time.wait(delay)
        pygame.display.update()

gameover()
game_loop()

