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

res_x = 1000
res_y = 600
Display = pygame.display.set_mode((res_x, res_y))
FPS = 60
pygame.display.set_caption("Tank Game")
#icon = pygame.image.load("file_name")
#pygame.display.set_icon(icon)

clock = pygame.time.Clock() 
# useless definition of values to avoid errors

shells = set([])
remove_shells = set([])

class Plane:
    def __init__(self, pos, vel, ang, img = None):
        self.pos = list(pos)
        self.vel = list(vel)
        self.ang = int(ang)
        self.img = scale_image(img, 0.5)
        self.size = self.img.get_size()

        self.numImages = 6
        self.cImage = 0

        self.dir = [None, None]
        self.fire = None
        self.shell_cd = 0

        self.gun_pos_minus = 15
        self.fire_vector_len = math.sqrt(self.size[0]**2 + (self.size[1]-self.gun_pos_minus)**2)
        print (self.fire_vector_len)
        self.fire_angle = math.asin((self.size[1]-self.gun_pos_minus)/self.fire_vector_len)
        print (self.fire_angle)

    def update(self):
        if self.fire:
            self.shoot()
        if self.dir[0] == "right" and self.vel[0] <= 6:
            self.vel[0] += 2
        elif self.dir[0] == "left" and self.vel[0] > -6:
            self.vel[0] -= 2
        elif self.dir[0] == None: self.vel[0] *= 0.9

        if self.dir[1] == "down" and self.vel[1] < 11:
            self.vel[1] += 1
        elif self.dir[1] == "up" and self.vel[1] > -10:
            self.vel[1] -= 1
        elif self.dir[1] == None: self.vel[1] *= 0.9

        #Cooldown
        if self.shell_cd > 0:
            self.shell_cd -= 1
        #Update
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        #Draw stuff
        pos = [int(self.pos[0]), int(self.pos[1])]
        if self.cImage >= self.numImages-1:
            self.cImage = 0
        else:
            self.cImage += 1


        image = pygame.transform.rotate(self.img, self.vel[1]*-1)

        Display.blit(image, (pos[0], pos[1]))

    def shoot(self):
        if not self.shell_cd:
            angle_rad = (self.vel[1])*math.pi/180
            forward = angle_to_vector(self.fire_angle + angle_rad)
            spread = random.randrange(-100, 101)/50

            pos = [int(self.pos[0]), int(self.pos[1])]
            new_shell = Sprite((pos[0]+self.fire_vector_len, pos[1]+self.fire_vector_len*forward[1]+5),
                               (self.vel[0]+30, self.vel[1]+spread))
            shells.add(new_shell)
            self.shell_cd = 5

        

    def key_event(self, key, down = False):
        if ((key == "left") or (key == "right")) and down:
            self.dir[0] = key
        elif ((key == "left") or (key == "right")) and not down:
            self.dir[0] = None

        if ((key == "up") or (key == "down")) and down:
            self.dir[1] = key
        elif ((key == "up") or (key == "down")) and not down:
            self.dir[1] = None

        if key == "shoot" and down:
            self.fire = True
        elif key == "shoot" and not down:
            self.fire = False

        if key == "bomb" and down:
            self.bomb()

class Sprite:
    def __init__(self, pos, vel, ang = None, img = None):
        self.pos = list(pos)
        self.vel = list(vel)
        self.ang = None

    def update(self):
        #Draw
        pos = [int(self.pos[0]), int(self.pos[1])]
        pygame.draw.circle(Display, black, pos, 4)

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if not (0<self.pos[0]<res_x and 0<self.pos[1]<res_y):
            remove_shells.add(self)


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
    text = smallfont.render("Score: "+str(score), True, black)
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
        message_screen("Légi Csata", green, -120, "large")
        message_screen("Shoot and destroy enemy planes,", black, -30, "small")
        message_screen("before they kill you!", black, 10, "small")
        intro = button("Play", (res_x/2-220, res_y-150, 100, 50), green, light_green, action = "switch")
        button("Controls", (res_x/2-60, res_y-150, 120, 50), yellow, light_yellow, action = "controls")
        button("Quit", (res_x/2+120, res_y-150, 100, 50), red, light_red, action = "quit")
        clock.tick(30)
        pygame.display.update()


def gameLoop():
    global shells, remove_shells
    gameExit = False
    gameOver = False

    shells = set([])
    remove_shells = set([])

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
        for event in pygame.event.get():  # Event handling
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                    myplane.key_event("left", True)
                if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                    myplane.key_event("right", True)
                if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                    myplane.key_event("down", True)
                if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                    myplane.key_event("up", True)
                if event.key == pygame.K_SPACE:
                    myplane.key_event("shoot", True)
                if event.key == pygame.K_q:
                    myplane.key_event("bomb", True)
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                    myplane.key_event("left", False)
                if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                    myplane.key_event("right", False)
                if (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                    myplane.key_event("down", False)
                if (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                    myplane.key_event("up", False)
                if event.key == pygame.K_SPACE:
                    myplane.key_event("shoot", False)
                if event.key == pygame.K_q:
                    myplane.key_event("bomb", False)
        


        Display.fill(light_blue)
        # Drawing goes here
        myplane.update()

        for shell in shells:
            shell.update()
        shells.difference_update(remove_shells)
        
        # Drawing goes here
        pygame.display.update()

        

        #print ("FPS:", 1/(time.clock() - prev_time))
        clock.tick(FPS)
    pygame.quit()
    quit()

def exit_game():
    pygame.quit()
    quit()

myplane = Plane((50, 100), (0, 0), 0, "plane3.png")


game_intro()
gameLoop()
