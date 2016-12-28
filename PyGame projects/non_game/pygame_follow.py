import pygame

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

res_x = 1300
res_y = 700
gameDisplay = pygame.display.set_mode((res_x, res_y))
pygame.display.set_caption("Izé")

gameExit = False
clock = pygame.time.Clock()
main_x = 300
main_y = 300
main_x_change = 0
main_y_change = 0
sub_x = 200
sub_y = 200
sub_x_change = 0
sub_y_change = 0

while not gameExit:
    if main_x < 0:          #Reset_main
        main_x = res_x
    if main_x > res_x:
        main_x = 0
    if main_y < 0:
        main_y = res_y
    if main_y > res_y:
        main_y = 0
    if main_x_change < 0:           #Decelerate main
        main_x_change += 1
    if main_x_change > 0:
        main_x_change -= 1
    if main_y_change < 0:
        main_y_change += 1
    if main_y_change > 0:
        main_y_change -= 1
    for event in pygame.event.get():          #Events main
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_x_change += -20
            if event.key == pygame.K_RIGHT:
                main_x_change += +20
            if event.key == pygame.K_DOWN:
                 main_y_change += +20
            if event.key == pygame.K_UP:
                 main_y_change += -20
            if event.key == pygame.K_SPACE:
                main_x_change = 0
                main_y_change = 0

    if main_y > sub_y:          #Follow
        sub_y_change += 1
    if main_y < sub_y:
        sub_y_change -= 1
    if main_x > sub_x:
        sub_x_change += 1
    if main_x < sub_x:
        sub_x_change -= 1

    if sub_x_change > 0:
        sub_x_change -= 0.5
    if sub_x_change < 0:
        sub_x_change += 0.5
    if sub_y_change > 0:
        sub_y_change -= 0.5
    if sub_y_change < 0:
        sub_y_change += 0.5

    if sub_x == main_x and sub_y == main_y:
        gameExit = True

    main_x += main_x_change
    main_y += main_y_change
    sub_x += sub_x_change
    sub_y += sub_y_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [main_x, main_y, 20, 20])
    pygame.draw.rect(gameDisplay, red, [sub_x, sub_y, 20, 20])
    pygame.display.update()




    clock.tick(30)
pygame.quit()
quit()