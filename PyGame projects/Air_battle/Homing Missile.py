import pygame, random, math, threading, time

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
light_red = (255, 0, 0)
green = (0, 155, 0)
light_green = (0, 205, 0)
dark_green = (0, 80, 0)
purple = (214, 32, 211)
blue = (0, 0, 255)
light_blue = (135, 206, 250)
yellow = (230, 200, 0)
light_yellow = (255, 255, 0)

font = pygame.font.SysFont("comicsansms", 50)
smallfont = pygame.font.SysFont("comicsansms", 25)
bigfont = pygame.font.SysFont("comicsansms", 85)

res_x = 900
res_y = 700
Display = pygame.display.set_mode((res_x, res_y))
FPS = 60
pygame.display.set_caption("Tank Game")
#icon = pygame.image.load("file_name")
#pygame.display.set_icon(icon)

clock = pygame.time.Clock() 
# useless definition of values to avoid errors
missiles = set([])
remove_missiles = set([])

class Missile:
    def __init__(self, pos, vel, ang, tg, img):
        self.pos = list(pos)
        self.vel = list(vel)
        self.ang = int(ang)
        self.tg = tg
        self.turn = 0.05
        if img:
            self.img = scale_image(img, 1)
            self.size = self.img.get_size()

    def update(self):
        # Tracking
        tg, pos = self.tg.pos, self.pos
        forward = angle_to_vector(self.ang)
        vector = [tg[0]-pos[0], tg[1] -  pos[1]]
        distance = math.sqrt(vector[0]**2 + vector[1]**2)
        to_turn = math.atan2(vector[0], vector[1])
        if self.ang < (to_turn*-1+0.5*math.pi):
            self.ang += self.turn
        else: self.ang -= self.turn

        self.vel[0] *= 0.9
        self.vel[1] *= 0.9

                
        self.vel[0] += forward[0]*7
        self.vel[1] += forward[1]*7


        #Update
        self.pos[0] += self.vel[0]/10
        self.pos[1] += self.vel[1]/10
        #Draw stuff
        pos = [int(self.pos[0]), int(self.pos[1])]
        pygame.draw.circle(Display, red, pos, 4)


        #pygame.draw.line(Display, black, pos, tg, 1) # Vector
        pygame.draw.line(Display, blue, pos, (pos[0]+forward[0]*40, pos[1]+forward[1]*50), 1) # Forward vector

class Target:
    def __init__(self, pos):
        self.pos = list(pos)

    def update(self):
        if pygame.mouse.get_pressed()[0]:
            self.pos = pygame.mouse.get_pos()
        

        pygame.draw.circle(Display, black, self.pos, 6)

def new_missile(pos, vel, angle, tg, image = None):
    global missiles
    new_missile = Missile(pos, vel, angle, tg, image)
    missiles.add(new_missile)


def scale_image(str_img, multipler):
    img = pygame.image.load(str_img)
    size = img.get_size()
    return pygame.transform.scale(img, (int(size[0]*multipler), int(size[1]*multipler)))
    

def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]
def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)
def collision_circle(obj, item, radius):
    #obj is a tuple of (x, y, width, height)
    #obj2 is point(x, y) + radius
    if obj[0]-radius < item[0] < obj[0]+obj[2]+radius and obj[1]-radius < item[1] < obj[1]+obj[3]+radius:
        return True
 

def pause():
    paused = True
    message_screen("Paused", black, -100, "large")
    message_screen("Press P or Space to continue or Escape to quit", black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) or (event.key == pygame.K_p):
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    exit_game()
        clock.tick(10)


def score(score):
    text = smallfont.render("FPS: "+str(score)[0:6], True, black)
    Display.blit(text, [1, 1])


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


def game_controls():
    controlls = True
    Display.fill(white)
    message_screen("Controls", green, -120, "large")
    message_screen("Fire : Space", black, -30, "small")
    message_screen("Move Turret: Up and Down arows", black, 10, "small")
    message_screen("Move tank: Left and Right arows", black, 50, "small")
    message_screen("Pause: P", black, 90, "small")
    while controlls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    controlls = False
                elif event.key == pygame.K_ESCAPE:
                    exit_game()

        controlls = button("Main Menu", (res_x/2-70, res_y-150, 140, 50), yellow, light_yellow, action = "switch")
        button("Quit", (res_x/2+120, res_y-150, 100, 50), red, light_red, action = "quit")

        clock.tick(30)
        pygame.display.update()

def button(text, pos, color1, color2, action, text_color = black):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if pos[0]+pos[2] > cur[0] > pos[0] and pos[1]+pos[3] > cur[1] > pos[1]:
        pygame.draw.rect(Display, color2, pos)
        if click[0] == 1:
            if action == "switch":
                return False
            elif action == "controls":
                clock.tick(6)
                game_controls()
                clock.tick(6)
            elif action == "quit":
                exit_game()
    else:
        pygame.draw.rect(Display, color1, pos)
    text_to_button(text, text_color, pos)

    return True


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                elif event.key == pygame.K_ESCAPE:
                    exit_game()

        Display.fill(white)
        message_screen("Test", green, -120, "large")
        message_screen("A célpont bal egérgombbal mozgatható", black, -30, "small")
        message_screen("Rakéták a szóközzel indíthatók", black, 10, "small")
        intro = button("Play", (res_x/2-220, res_y-150, 100, 50), green, light_green, action = "switch")
        button("Controls", (res_x/2-60, res_y-150, 120, 50), yellow, light_yellow, action = "controls")
        button("Quit", (res_x/2+120, res_y-150, 100, 50), red, light_red, action = "quit")
        clock.tick(30)
        pygame.display.update()


def gameLoop():
    global missiles, remove_missiles
    gameExit = False
    gameOver = False

    missiles = set([])
    remove_missiles = set([])
    count_fps = 0

    while not gameExit:
        prev_time = time.clock()
        
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
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for x in range(500):
                        new_missile([random.randrange(0, res_x), random.randrange(0, res_y)], (0,0), random.randrange(0, int(math.pi*200))/100, target)
                    print ("Objects:",len(missiles))
                elif event.key == pygame.K_w:
                    new_missile([random.randrange(0, res_x), random.randrange(0, res_y)], (0,0), random.randrange(0, int(math.pi*200))/100, target)
                    print ("Objects:",len(missiles))


        Display.fill(light_blue)
        # Drawing goes below
        
        for missile in missiles:
            missile.update()
        target.update()

        score(1/(time.clock() - prev_time)) # FPS
        # Drawing goes above
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


target = Target((res_x//2, res_y//2))

def exit_game():
    pygame.quit()
    quit()

game_intro()
gameLoop()
