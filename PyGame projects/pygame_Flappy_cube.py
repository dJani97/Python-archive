import pygame, random

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
dark_green = (0, 80, 0)
purple = (214, 32, 211)

block_size = 20
res_x = 800
res_y = 600
FPS = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
gameDisplay = pygame.display.set_mode((res_x, res_y))
pygame.display.set_caption("Flappy_cube")


def message_display(msg, color, y_displace=0):
    text_surf = font.render(msg, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (res_x/2), (res_y/2)+y_displace
    gameDisplay.blit(text_surf, text_rect)
    pygame.display.update()


def score_display(msg, color, y_place= 10, x_place=10):
    msg = str(msg)
    text_surf = font.render(msg, True, color)
    gameDisplay.blit(text_surf, [y_place, x_place])


def gameLoop():
    tube_count = 0
    score_count = 0
    gameExit = False
    gameOver = False
    main_x = res_x/4
    main_y = res_y/2
    main_x_change = 0
    main_y_change = 0



    while not gameExit:
        gameDisplay.fill(white)
        while gameOver is True:
            gameDisplay.fill(black)
            message_display("Score: "+str(score_count), red, -30)
            message_display("Esc - exit;    Space - restart.", red, 10)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        if main_y_change < 20:                      # 20 alap
            main_y_change += 0.5
        for event in pygame.event.get():            # Events main
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        main_x_change += -2
                    if event.key == pygame.K_RIGHT:
                        main_x_change += +2
                    if event.key == pygame.K_DOWN:
                        main_y_change += +2
                    if event.key == pygame.K_UP:
                        main_y_change = -10
                    if event.key == pygame.K_SPACE:
                        main_x_change = 0
                        main_y_change = 0
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        main_x_change += +2
                    if event.key == pygame.K_RIGHT:
                        main_x_change += -2

        main_x += main_x_change
        main_y += main_y_change
        if main_y > res_y-20:                       # Pattogas
            main_y = res_y-20
            main_y_change = (main_y_change*-1)/2
        if main_y < 0:
            main_y = 0
            main_y_change = (main_y_change*-1)/2

        # print (score_count)           # <---- !!!!!_unused_print_command_!!!!!
        if tube_count == 0 and score_count <= 5:                    # TUBE creation + difficulties
            tube_widht = 30
            tube_x = res_x
            tube_lenght_up = random.randrange(100, res_y-250)
            tube_lenght_down = (res_y-tube_lenght_up-140)*-1
            tube_count += 1
        elif tube_count == 0 and (5 < score_count <= 10):           # medium
            tube_widht = 30
            tube_x = res_x
            tube_lenght_up = random.randrange(60, res_y-200)
            tube_lenght_down = (res_y-tube_lenght_up-130)*-1
            tube_count += 1
        elif tube_count == 0 and (10 < score_count):                # hard
            tube_widht = 30
            tube_x = res_x
            tube_lenght_up = random.randrange(10, res_y-150)
            tube_lenght_down = (res_y-tube_lenght_up-115)*-1
            tube_count += 1

        if tube_count > 0:                                          # Move speed, alap = 4
            tube_x -= 4
            if tube_x < - tube_widht:
                tube_count -= 1
                score_count += 1

        pygame.draw.rect(gameDisplay, dark_green, [tube_x, 0, tube_widht, tube_lenght_up])
        pygame.draw.rect(gameDisplay, dark_green, [tube_x, res_y, tube_widht, tube_lenght_down])
        pygame.draw.rect(gameDisplay, black, [main_x, main_y, block_size, block_size])
        score_display(score_count, red)
        pygame.display.update()

        if main_x > tube_x and main_x < tube_x + tube_widht or main_x + block_size > tube_x and main_x < tube_x + tube_widht:
            if tube_lenght_up <= main_y <= (res_y-block_size-tube_lenght_down*-1):
                pass
            else:
                # message_display("FATAL!!!", red)
                gameOver = True

        score_display(score_count, red, -50)
        clock.tick(FPS)
    pygame.quit()
    quit()

gameLoop()