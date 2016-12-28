import pygame

pygame.init()
clock = pygame.time.Clock()
joystick_count = pygame.joystick.get_count()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

# Get the name from the OS for the controller/joystick
name = joystick.get_name()
print("Joystick name: {}".format(name) )
while True:
# Get all axis
    pygame.event.get()
    axes = joystick.get_numaxes()

    for i in range( axes ):
                axis = joystick.get_axis( i )
                print("Axis {} value: {:>6.3f}".format(i, axis) )
    clock.tick(30
               )
    print ("\n ----------------------------- \n")
