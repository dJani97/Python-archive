import pygame, random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
dark_green = (0, 80, 0)
purple = (214, 32, 211)
blue = (0, 0, 255)
yellow = (200, 200, 0)

img_green = pygame.image.load('SnakeHeadGreen.png')
font = pygame.font.SysFont("comicsansms", 50)
smallfont = pygame.font.SysFont("comicsansms", 25)
bigfont = pygame.font.SysFont("comicsansms", 85)

res_x = 600
res_y = 500
Display = pygame.display.set_mode((res_x, res_y))
FPS = 12
block_size = 20
apple_size = 31
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

direction = "right"

def pause():
    paused = True
    message_screen("Paused", black, -100, "large")
    message_screen("Press Space to continue or Escape to quit", black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    exit_game()
        clock.tick(10)


def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    Display.blit(text, [1, 1])

def snake(snakeList, block_size):
    if direction == "right":
        head = pygame.transform.rotate(img_green, 270)
    if direction == "left":
        head = pygame.transform.rotate(img_green, 90)
    if direction == "up":
        head = img_green
    if direction == "down":
        head = pygame.transform.rotate(img_green, 180)

    Display.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(Display, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size = "small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = font.render(text, True, color)
    elif size == "large":
        textSurface = bigfont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, pos, size = "small"):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (pos[0]+(pos[2]/2), pos[1]+(pos[3]/2))
    Display.blit(text_surf, text_rect)
    

def message_screen(msg, color, y_displace=0, size = "small"):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (res_x/2), (res_y/2)+y_displace
    Display.blit(text_surf, text_rect)


def randAppleGen():
    apple_x = round(random.randrange(apple_size, res_x-apple_size)/10)*10
    apple_y = round(random.randrange(apple_size, res_y-apple_size)/10)*10
    return apple_x, apple_y


def game_intro():
    intro = True
    Display.fill(white)
    message_screen("Tanks Game", green, -120, "large")
    message_screen("Shoot and destroy enemy tanks,", black, -30, "small")
    message_screen("before they kill you!", black, 10, "small")
    #message_screen("Press Space to start, Esc to quit.", black, 80, "small")
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                elif event.key == pygame.K_ESCAPE:
                    exit_game()

        
        pygame.draw.rect(Display, green, (res_x/2-220, res_y-150, 100, 50))
        pygame.draw.rect(Display, yellow, (res_x/2-60, res_y-150, 120, 50))
        pygame.draw.rect(Display, red, (res_x/2+120, res_y-150, 100, 50))
        text_to_button("Play", black, (res_x/2-220, res_y-150, 100, 50))
        text_to_button("Controlls", black, (res_x/2-60, res_y-150, 120, 50))
        text_to_button("Quit", black, (res_x/2+120, res_y-150, 100, 50))















        
        clock.tick(10)
        pygame.display.update()


def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    apple_x, apple_y = randAppleGen()
    lead_x = res_x/2-5*block_size
    lead_y = res_y/2
    lead_x_change = 0
    lead_y_change = 0
    snakeList = []
    snakeLenght = 1

    while not gameExit:
        if gameOver == True:
            message_screen("Game Over!", red, -50, "large")
            message_screen("Press Space to restart or Esc to quit.", black, 30)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            exit_game()
                        if event.key == pygame.K_SPACE:
                            gameLoop()

        for event in pygame.event.get():  # Events LEAD
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_LEFT) or (event.key == pygame.K_a)) and lead_x_change != block_size:          # Snake1
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                if ((event.key == pygame.K_RIGHT) or (event.key == pygame.K_d)) and lead_x_change != -block_size:
                    lead_x_change = +block_size
                    lead_y_change = 0
                    direction = "right"
                if ((event.key == pygame.K_DOWN) or (event.key == pygame.K_s)) and lead_y_change != -block_size:
                    lead_y_change = +block_size
                    lead_x_change = 0
                    direction = "down"
                if ((event.key == pygame.K_UP) or (event.key == pygame.K_w)) and lead_y_change != block_size:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                if event.key == pygame.K_SPACE:
                    pause()
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
                if event.key == pygame.K_p:
                    pause()

        if lead_x < 0 or lead_x >= res_x or lead_y < 0 or lead_y >= res_y:      # Határok
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        Display.fill(white)
        pygame.draw.rect(Display, red,[apple_x, apple_y, apple_size, apple_size])


        snakeHead = []                  # Snake1 rajzolás
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLenght:
            del snakeList[0]
        if snakeHead in snakeList[:-1]:
            gameOver = True
        
        snake(snakeList, block_size)

        score(snakeLenght-1)
        pygame.display.update()

        if lead_x > apple_x and lead_x < apple_x + apple_size or lead_x + block_size > apple_x and lead_x < apple_x + apple_size:
            if lead_y > apple_y and lead_y < apple_y + apple_size or lead_y + block_size > apple_y and lead_y < apple_y + apple_size:
                apple_x, apple_y = randAppleGen()
                snakeLenght += 1






        clock.tick(FPS)
    exit_game()


def exit_game():
    pygame.quit()
    quit()

game_intro()
gameLoop()
