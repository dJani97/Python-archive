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
yellow = (230, 200, 0)
light_yellow = (255, 255, 0)

font = pygame.font.SysFont("comicsansms", 50)
smallfont = pygame.font.SysFont("comicsansms", 25)
bigfont = pygame.font.SysFont("comicsansms", 85)

res_x = 800
res_y = 600
Display = pygame.display.set_mode((res_x, res_y))
FPS = 60
pygame.display.set_caption("Tank Game")
#icon = pygame.image.load("file_name")
#pygame.display.set_icon(icon)

clock = pygame.time.Clock() 
# useless definition of values to avoid errors
projectiles = set([])
add_to_particles = set([])
remove_these = set([])
barrier_pos = [1, 1, 1, 1]


class Projectile:
    def __init__(self, pos, vel, color, radius = 4, img = None):
        self.pos = list(pos)
        self.vel = list(vel)
        self.color = color
        self.img = img
        self.radius = radius

    def get_data(self):
        return self, self.pos, self.vel

    def explosion(self):
        multipler = 2000
        if self.vel[1] < 0:
            pass
        else:
            self.vel[1] *= -0.1
            
        for bit in range(60):
            color = random.choice((yellow, light_red, red))
            bit = Projectile(self.pos, [random.randrange(-multipler, multipler+1)/1000,
                                        self.vel[1]+random.randrange(-multipler, multipler+1)/1000],
                             color, 2)
            
            add_to_particles.add(bit)
    def update(self):
        #Velocity update
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.vel[1] += 0.08

        
        #Draw
        pos = [int(self.pos[0]), int(self.pos[1])]
        pygame.draw.circle(Display, self.color, pos, self.radius)

        #Returns True if collides
        if (pos[1]+self.radius*2 > res_y) or collision_circle(barrier_pos, pos, self.radius):
            if self.radius == 4:
                self.explosion()
            return True
        # Add a counter: first time reflect, second time kill



class Tank:
    def __init__(self, pos, vel, angle, color, img = None):
        self.pos = list(pos)
        self.vel = list(vel)
        self.angle = angle
        self.color = color
        self.img = img
        self.score = 0

        self.dim = [40, 10]
        self.turret = 3
        self.wheel = 5
        self.dir = None
        self.aim = None
        self.charge = False
        self.power = 0

    def score_display(self):
        score(self.score, [1, 1], self.power, self.color)
    
    def shoot(self):
        forward = angle_to_vector(self.angle)
        pos = [int(self.pos[0]), int(self.pos[1])]
        projectile = Projectile((forward[0]*25+pos[0], forward[1]*25+pos[1]),
                           (forward[0]*self.power, forward[1]*self.power), green)
        projectiles.add(projectile)

    def detonate(self):
        remove = set([])
        for projectile in projectiles:
            if projectile.radius == 4:
                projectile.explosion()
                remove.add(projectile)
        projectiles.difference_update(remove)
    
    def key_event(self, key, down = False):
        if ((key == "left") or (key == "right")) and down:
            self.dir = key
        elif ((key == "left") or (key == "right")) and not down:
            self.dir = None

        if ((key == "up") or (key == "down")) and down:
            self.aim = key
        elif ((key == "up") or (key == "down")) and not down:
            self.aim = None

        if key == "shoot" and down:
            self.charge = True
        elif key == "shoot" and not down:
            self.charge = False

        elif key == "detonate":
            self.detonate()
         
    def update(self, right = False):
        forward = angle_to_vector(self.angle)
        
        #Velocity update
        if self.dir == "right" and self.vel[0] < 2:
            self.vel[0] += 0.5
        elif self.dir == "left" and self.vel[0] > -2:
            self.vel[0] -= 0.5
        else: self.vel[0] *= 0.8
        #Turet move
        if self.aim == "up":
            self.angle += 0.01
        elif self.aim == "down":
            self.angle -= 0.01
        #Charge and shoot
        if self.charge:
            self.power += 0.1
        else:
            if self.power > 2:
                self.shoot()
            self.power = 2
        
        #Update tank
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        #Check if out of map or barrier
        if right and barrier_pos[0]+barrier_pos[2]+(self.dim[0]//2) > self.pos[0]:
            self.pos[0] += 10

        elif not right and barrier_pos[0]+barrier_pos[2]+(self.dim[0]//2) < self.pos[0]:
            self.pos[0] -= 2.5
    
        #Draw stuff
        pos = [int(self.pos[0]), int(self.pos[1])]
        pygame.draw.line(Display, self.color, (pos[0], pos[1]-self.turret), (forward[0]*25+pos[0], forward[1]*25+pos[1]), self.turret)
        
        pygame.draw.circle(Display, black, pos, 10)
        pygame.draw.rect(Display, self.color, (pos[0]-self.dim[0]//2, pos[1],
                                               self.dim[0], self.dim[1]))
        
        for x in range(10):
            pygame.draw.circle(Display, black, (pos[0]-self.dim[0]//2+2 + x*4, pos[1]+self.dim[1]), self.wheel)
        #Draw HUD
        self.score_display()
            
mytank = Tank([res_x*0.95, res_y*0.96], [0, 0], 3.26, dark_green)

def barrier(pos):
    pygame.draw.rect(Display, black, pos)

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


def score(score, pos, power, color = black):
    linewidth = 20
    if power*30-30 <= 255: color_intensity = power*30-30
    
    else: color_intensity = 255
    mxd_color = [color_intensity, 255-color_intensity, 0]
    
    text = smallfont.render("Score: "+str(score), True, color)
    Display.blit(text, (pos[0], pos[1]+linewidth))

    pygame.draw.rect(Display, mxd_color, (pos[0]-40, pos[1], power*20, linewidth))

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
        message_screen("Tanks Game", green, -120, "large")
        message_screen("Shoot and destroy enemy tanks,", black, -30, "small")
        message_screen("before they kill you!", black, 10, "small")
        intro = button("Play", (res_x/2-220, res_y-150, 100, 50), green, light_green, action = "switch")
        button("Controls", (res_x/2-60, res_y-150, 120, 50), yellow, light_yellow, action = "controls")
        button("Quit", (res_x/2+120, res_y-150, 100, 50), red, light_red, action = "quit")
        mytank.update()
        clock.tick(30)
        pygame.display.update()


    
def gameLoop():
    gameExit = False
    gameOver = False
    global projectiles, barrier_pos, add_to_particles
    
    projectiles = set([])
    barrier_pos = [(res_x//2)+random.randint(int(-res_x*0.2), int(res_x*0.15)),
                   random.randint(res_y*0.4, res_y*0.7), 60, res_x]

    while not gameExit:

        prev_time = time.clock()
        
        remove_these = set([])
        add_to_particles = set([])
        
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
                    mytank.key_event("left", True)
                if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                    mytank.key_event("right", True)
                if event.key == (pygame.K_DOWN or pygame.K_s):
                    mytank.key_event("down", True)
                if event.key == (pygame.K_UP or pygame.K_w):
                    mytank.key_event("up", True)
                if event.key == pygame.K_SPACE:
                    mytank.key_event("shoot", True)
                if event.key == pygame.K_w:
                    mytank.key_event("detonate")
                if event.key == pygame.K_p:
                    pause()
                if event.key == pygame.K_ESCAPE:
                    gameExit = True
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                    mytank.key_event("left", False)
                if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                    mytank.key_event("right", False)
                if event.key == (pygame.K_DOWN or pygame.K_s):
                    mytank.key_event("down", False)
                if event.key == (pygame.K_UP or pygame.K_w):
                    mytank.key_event("up", False)
                if event.key == pygame.K_SPACE:
                    mytank.key_event("shoot", False)

        Display.fill(white)

        for projectile in projectiles:
            if projectile.update():
                remove_these.add(projectile)
        projectiles.difference_update(remove_these)
        for bit in add_to_particles:
            projectiles.add(bit)
        print ("Lenght of item list:", len(projectiles))
        mytank.update(True)
        barrier(barrier_pos)
                                            
        pygame.display.update()


        
        print ("FPS:", 1/(time.clock() - prev_time))
        
        clock.tick(FPS)
        
    exit_game()


def exit_game():
    pygame.quit()
    quit()


game_intro()
gameLoop()
