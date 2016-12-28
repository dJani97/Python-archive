import pygame, math

print (math.sqrt(280**2 + 86**2))
       
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


def scale_image(str_img, multipler):
    img = pygame.image.load(str_img)
    size = img.get_size()
    return pygame.transform.scale(img, (int(size[0]*multipler), int(size[1]*multipler)))


IMAGE = "plane.png"


class Sprite:
    def __init__(self, image):
        self.image = scale_image(image, 1)
        self.size = self.image.get_size()
        print (self.size)
        self.numImages = 6
        self.cImage = 0
        self.x = 200
        self.y = 200
        

    def update(self):

        if self.cImage >= self.numImages-1:
            self.cImage = 0
        else:
            self.cImage += 1

        Display.blit(self.image, (self.x, self.y), (self.cImage*(self.size[0]//self.numImages), 0, self.size[0]//self.numImages, self.size[1]))

        image = pygame.image.load("plane11.png")
        image_c = pygame.transform.chop(image, (10, 10, 100, 1))
        Display.blit(image_c, (100,100))
        
explosion = Sprite(IMAGE)


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

    Display.fill(white)
    
    explosion.update()
    
    pygame.display.update()

    clock.tick(20)
