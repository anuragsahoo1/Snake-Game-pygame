import pygame
import  random
import os
pygame.init()


#colors
white = (17, 231, 128)
red = (255,0,0)
black= (0,0,0)
blue = (110, 255, 255)
yellow = (240, 255, 0, 1)
purple = (106, 90, 205)

#variables
screen_width =700
screen_hieght = 400
gameWindow = pygame.display.set_mode((screen_width,screen_hieght))
bgimg = pygame.image.load("photo.jpg")
bgimg =pygame.transform.scale(bgimg,(screen_width,screen_hieght)).convert_alpha()
pygame.display.set_caption("Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

#text
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
#snake body
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,black,[x,y,snake_size,snake_size])

#Wlcome screen function
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(blue)
        gameWindow.blit(bgimg, (0, 0))
        text_screen("Snake  ",purple,275,130)
        text_screen("Press Enter To Play  ",purple,169,190)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(60)
#main event loop func
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 66
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    score = 0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_hieght / 2)
    snk_list = []
    snk_length = 1
    fps = 60
    init_velocity = 3
    if (not os.path.exists("high.txt")):
        with open("high.txt","w") as f:
            f.write("0")
    with open("high.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("high.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.fill(white)
            text_screen("Game over!! enter to continue",red,76,190)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game =True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
                for event in pygame.event.get():
                    #print(event)
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0

                        if event.key == pygame.K_LEFT:
                            velocity_x = -init_velocity
                            velocity_y = 0
                        if event.key == pygame.K_UP:
                            velocity_y = -init_velocity
                            velocity_x = 0
                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0

                snake_x += velocity_x
                snake_y += velocity_y

                if abs(snake_x - food_x)<6 and abs(snake_y- food_y) <6:
                    score = score + 2
                    food_x = random.randint(20, screen_width / 2)
                    food_y = random.randint(40, screen_hieght / 2)
                    snk_length +=5
                    if score>int(highscore):
                        highscore = score


                gameWindow.fill(white)

                text_screen("Score-" + str(score) + "    HighScore" +str(highscore), red, 5, 5)
                pygame.draw.rect(gameWindow, yellow, [food_x, food_y, snake_size, snake_size])

                head=[]
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)

                if len(snk_list) > snk_length:
                    del snk_list[0]

                if head in snk_list[:-1]:
                    game_over = True
                if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_hieght:
                    game_over =True


        plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
