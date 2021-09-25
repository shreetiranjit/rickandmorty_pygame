import pygame
import os
import random
pygame.init()

# global constants
screen_height = 600
screen_width = 1100
screen = pygame.display.set_mode((screen_width,screen_height))

running = [pygame.image.load(os.path.join("dinopic", "DinoRun1.png")),
           pygame.image.load(os.path.join("dinopic", "DinoRun2.png"))]

jumping = pygame.image.load(os.path.join("dinopic", "DinoJump.png"))

ducking = [pygame.image.load(os.path.join("dinopic", "DinoDuck1.png")),
           pygame.image.load(os.path.join("dinopic", "DinoDuck1.png"))]

small_cactus = [pygame.image.load(os.path.join("dinopic", "SmallCactus1.png")),
                pygame.image.load(os.path.join("dinopic", "SmallCactus2.png")),
                pygame.image.load(os.path.join("dinopic", "SmallCactus3.png"))]

large_cactus = [pygame.image.load(os.path.join("dinopic", "LargeCactus1.png")),
                pygame.image.load(os.path.join("dinopic", "LargeCactus2.png")),
                pygame.image.load(os.path.join("dinopic", "LargeCactus3.png"))]

bird = [pygame.image.load(os.path.join("dinopic", "Bird1.png")),
        pygame.image.load(os.path.join("dinopic", "Bird2.png"))]

bg = pygame.image.load(os.path.join("dinopic", "Track.png"))

cloud  = pygame.image.load(os.path.join("dinopic", "Cloud.png"))

class Dinosaur :
    x_pos = 80
    y_pos = 310
    y_pos_duck = 340
    jump_velocity = 8.5

    def __init__(self):
        self.duck_image = ducking
        self.run_image = running
        self.jump_image = jumping

        self.dino_duck = False
        self.dino_jump = False
        self.dino_run = True

        self.step_index =  0
        self.jump_vel = self.jump_velocity
        self.image = self.run_image[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, userinput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userinput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_jump = True
            self.dino_run = False
        elif userinput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif not (self.dino_jump or userinput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_jump = False
            self.dino_run = True

    def duck(self):
        self.image = self.duck_image[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index += 1

    def run(self):
        self.image = self.run_image[self.step_index//5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_image
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.jump_velocity:
            self.dino_jump = False
            self.jump_vel= self.jump_velocity

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = screen_width + random.randint(800,1000)
        self.y = random.randint(50,100)
        self.image = cloud
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < - self.width:
            self.x = screen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


def main():
    global game_speed
    global x_pos_bg
    global y_pos_bg
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    CLOUD = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380

    def background():
        global x_pos_bg
        global y_pos_bg
        image_width = bg.get_width()
        screen.blit(bg, (x_pos_bg, y_pos_bg))
        screen.blit(bg, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(bg, (image_width + x_pos_bg , y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.fill((255, 255, 255))
        userinput = pygame.key.get_pressed()

        player.draw(screen)
        player.update(userinput)

        CLOUD.draw(screen)
        CLOUD.update()

        background()

        clock.tick(30)
        pygame.display.update()


main()


