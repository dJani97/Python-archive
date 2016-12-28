SERVER_IP = "ftp.kozos.comule.com"
USER = "a1151360"
PASSWORD = "agyacska000"
DIR = False
prev_x = 150
prev_y = 150


# FTP upload
import ftplib
import io
counter = 290
ftp = ftplib.FTP(SERVER_IP)
ftp.login(USER, PASSWORD)
if DIR:
    ftp.cwd(DIR)


# Initalize pygame&joys
import pygame
pygame.init()
clock = pygame.time.Clock()
joystick_count = pygame.joystick.get_count()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()


while True:
    #Get joystick axes
    pygame.event.get()
    pos_x = joystick.get_axis(4)
    pos_y = joystick.get_axis(3)
    clock.tick(30)
    print ("\n\n")
    
    if pos_x != prev_x:
        myfile = io.BytesIO()
        myfile.write(bytes(str(int((pos_x+1)*150)), 'UTF-8'))
        myfile.seek(0)
        print (ftp.storlines("STOR " + "x.test", myfile))
    if pos_y != prev_y:
        myfile = io.BytesIO()
        myfile.write(bytes(str(int((pos_y+1)*150)), 'UTF-8'))
        myfile.seek(0)
        print (ftp.storlines("STOR " + "y.test", myfile))
    
    prev_x = pos_x
    prev_y = pos_y
