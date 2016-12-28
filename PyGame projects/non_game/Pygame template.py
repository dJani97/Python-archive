import pygame, random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
dark_green = (0, 80, 0)
purple = (214, 32, 211)
blue = (0, 0, 255)


font = pygame.font.SysFont(None, 50)
smallfont = pygame.font.SysFont(None, 30)
bigfont = pygame.font.SysFont(None, 90)

res_x = 600
res_y = 500
Display = pygame.display.set_mode((res_x, res_y))
FPS = 30
block_size = 20
apple_size = 31
pygame.display.set_caption("Tank Game")
clock = pygame.time.Clock()


def pause():
    paused = True
    message_display("Paused", black, -100, bigfont)
    message_display("Press Space to continue or Escape to quit", black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
        
        clock.tick(10)


def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [1, 1])


def message_display(msg, color, y_displace=0, font_type = font):
    text_surf = font_type.render(msg, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (res_x/2), (res_y/2)+y_displace
    gameDisplay.blit(text_surf, text_rect)


def gameLoop():
    gameExit = False
    gameOver = False

    while not gameExit:
        if gameOver == True:
            message_display("Game Over!", red, -50, bigfont)
            message_display("Press Space to restart or Esc to quit.", black, 30)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            gameExit = True
                            gameOver = False
                        if event.key == pygame.K_SPACE:
                            gameLoop()

        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_LEFT) or (event.key == pygame.K_a)) and lead_x_change != block_size:          # Snake1
                    pass
                if ((event.key == pygame.K_RIGHT) or (event.key == pygame.K_d)) and lead_x_change != -block_size:
                    pass
                if ((event.key == pygame.K_DOWN) or (event.key == pygame.K_s)) and lead_y_change != -block_size:
                    pass
                if ((event.key == pygame.K_UP) or (event.key == pygame.K_w)) and lead_y_change != block_size:
                    pass
                if event.key == (pygame.K_SPACE or pygame.K_p):
                    pause()
                if event.key == pygame.K_ESCAPE:
                    gameExit = True



        gameDisplay.fill(white)

        # Drawing goes here
        # Drawing goes here
        # Drawing goes here
        
        pygame.display.update()

        



        clock.tick(FPS)
    pygame.quit()
    quit()

gameLoop()
