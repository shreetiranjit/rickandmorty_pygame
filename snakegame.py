"""this module is for snake game"""

import pygame
import random
import os

def snake12():
    pygame.mixer.init()

    pygame.init()

    # Colors
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    green = (0, 255, 0)

    # Creating screen
    screen_width = 700
    screen_height = 600
    gameWindow = pygame.display.set_mode((screen_width, screen_height))

    # Background Images
    background = pygame.image.load("C:/Users/Lenovo/Downloads/2snake.jpg")
    bgimg = pygame.transform.scale(background, (screen_width, screen_height)).convert_alpha()
    start_image = pygame.image.load("C:/Users/Lenovo/Downloads/fam.jpg")
    start = pygame.transform.scale(start_image, (screen_width, screen_height)).convert_alpha()
    gameover_image = pygame.image.load("C:/Users/Lenovo/Downloads/game_over.jpg")
    gameover = pygame.transform.scale(gameover_image, (screen_width, screen_height)).convert_alpha()

    # Game Title
    pygame.display.set_caption("Snake Game (Rick - And - Morty)")
    pygame.display.update()

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Ubuntu", 45)

    # background music
    pygame.mixer.music.load('C:/Users/Lenovo/Downloads/theme.mp3')
    pygame.mixer.music.play(-1)


    def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, [x,y])


    def draw_snake(gameWindow, color, snk_list, snake_size):
        for x,y in snk_list:
            pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


    def front_page():
        """ creates welcome page"""
        exit_game = False
        while not exit_game:
            gameWindow.blit(start, (0, 0))
            text_screen("Welcome!!!", red, 170, 230)
            text_screen("Press Press 'S' To Play", red, 170, 300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:

                        gameloop()

            pygame.display.update()
            clock.tick(60)


    # Game Loop
    def gameloop():
        # Game specific variables
        exit_game = False
        game_over = False
        snake_x = 10
        snake_y = 10
        velocity_x = 0
        velocity_y = 0
        snake_list = []
        snake_length = 1
        # Check if highscore file exists
        if(not os.path.exists("highscore.txt")):
            with open("highscore.txt", "w") as f:
                f.write("0")

        with open("highscore.txt", "r") as f:
            highscore = f.read()

        food_x = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0
        score = 0
        init_velocity = 5
        snake_size = 20
        fps = 60
        while not exit_game:
            if game_over:
                with open("highscore.txt", "w") as f:
                    f.write(str(highscore))
                gameWindow.blit(gameover, (0, 0))
                text_screen("Game Over! Press Enter To Continue.", red, 50, 250)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            front_page()

            else:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            velocity_x = - init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_UP:
                            velocity_y = - init_velocity
                            velocity_x = 0

                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0

                        if event.key == pygame.K_q:
                            score += 10

                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y

                if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                    score += 5
                    food_x = round(random.randrange(0, screen_width - 10) / 10.0) * 10.0
                    food_y = round(random.randrange(0, screen_height - 10) / 10.0) * 10.0
                    snake_length += 1
                    if score>int(highscore):
                        highscore = score


                gameWindow.blit(bgimg, (0, 0))
                text_screen("Score: " + str(score) , red, 5, 5)
                text_screen("Highscore: " + str(highscore) , red, 420, 5)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


                head = []
                head.append(snake_x)
                head.append(snake_y)
                snake_list.append(head)

                if len(snake_list)>snake_length:
                    del snake_list[0]

                if head in snake_list[:-1]:
                    game_over = True
                    pygame.mixer.music.stop()
                    over = pygame.mixer.Sound('C:/Users/Lenovo/Downloads/wubalubadubdubs.mp3')
                    over.play()

                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                    game_over = True
                    pygame.mixer.music.stop()
                    over = pygame.mixer.Sound('C:/Users/Lenovo/Downloads/wubalubadubdubs.mp3')
                    over.play()
                draw_snake(gameWindow, green, snake_list, snake_size)
            pygame.display.update()
            clock.tick(fps)

        pygame.quit()
        quit()
    front_page()