import pygame, math

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
dark_green = (0, 80, 0)
purple = (214, 32, 211)
blue = (0, 0, 255)

res_x = 600
res_y = 400

font = pygame.font.SysFont(None, 50)
smallfont = pygame.font.SysFont(None, 30)
bigfont = pygame.font.SysFont(None, 90)

clock = pygame.time.Clock()

Display = pygame.display.set_mode((res_x, res_y))




angle = 20

def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

forward = angle_to_vector(angle)


pygame.draw.line(Display, red, (forward[0]*50+200, forward[1]*50+200), (200, 200), 2)





"""
Display.fill(blue)

Pix = pygame.PixelArray(Display)
Pix[20][20] = white
Pix[20][21] = white
Pix[21][20] = white

pygame.draw.line(Display, red, (100, 100), (150, 350), 5)
pygame.draw.circle(Display, dark_green, (res_x//2, res_y//2), 60)
pygame.draw.rect(Display, green, (res_x, res_y, -120, -60))
pygame.draw.polygon(Display, white, ((200, 150), (250, 100), (100, 100)))
"""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

    clock.tick(60)
