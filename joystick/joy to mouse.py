import pygame, ctypes
from ctypes import windll, Structure, c_ulong, byref


# Mouse event list
LEFTDOWN   = 0x00000002
LEFTUP     = 0x00000004
MIDDLEDOWN = 0x00000020
MIDDLEUP   = 0x00000040
MOVE       = 0x00000001
ABSOLUTE   = 0x00008000
RIGHTDOWN  = 0x00000008
RIGHTUP    = 0x00000010
MOUSEEVENTF_WHEEL = 0x0800 # wheel button is rotated

# Source:
# http://nullege.com/codes/show/src@u@i@UISoup-1.3.2@uisoup@win_soup@mouse.py/213/ctypes.windll.user32.GetCursorPos

Mouse = ctypes.windll.user32



POWER = 2
RESOLUTION = [1920, 1200]
mouse_vel = [0, 0]
mouse_left = False

pygame.init()
clock = pygame.time.Clock()
joystick_count = pygame.joystick.get_count()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()


class POINT(Structure): # IDK Class for get_pos
    _fields_ = [("x", c_ulong),
             ("y", c_ulong)]
pt = POINT()
def getpos():
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


def convert(vel, pos, res): #velocity processor
    if (vel < 0) and (POWER%2 == 0): multipler = -1
    else: multipler = 1
    velocity = ((vel*5)**POWER)*multipler
    pos += velocity
    if pos > res:
        pos = res
    elif pos < 0:
        pos = 0
    return pos

prev_mpos = getpos() #Gets the actual mouse position to begin
cur_mpos = prev_mpos
mouse_pos = [prev_mpos["x"], prev_mpos["y"]]

while True:
    
    pygame.event.get()
            
    mouse_vel[0] = joystick.get_axis(4)
    mouse_vel[1] = joystick.get_axis(3)

    mouse_scroll = [joystick.get_axis(0), joystick.get_axis(1)]    
    
    

    v_max = 0.05
    mouse_bool = False      # Turn of moouse controll is buggy as shit !!!!
    
    # Keeping the mouse hardware in sync
    if (-v_max < mouse_vel[0] < v_max) and (-v_max < mouse_vel[1] < v_max) and mouse_bool:
        cur_mpos = getpos() # Gets ctual position
        mchange = [cur_mpos["x"] - prev_mpos["x"], cur_mpos["y"] - prev_mpos["y"]]
        prev_mpos = cur_mpos #Sets curren pos as "next round's" prev pos
        print ("szamolok")
    else:
        mchange = [0,0]
        #print ("mozog")
    
    
    #Mouse manipulation
    mouse_pos[0] = convert(mouse_vel[0], mouse_pos[0], RESOLUTION[0]) + mchange[0]
    mouse_pos[1] = convert(mouse_vel[1], mouse_pos[1], RESOLUTION[1]) + mchange[1]
    Mouse.SetCursorPos(int(mouse_pos[0]), int(mouse_pos[1])) # Set pos
    if (joystick.get_axis(2) < -0.2) and (not mouse_left):
        mouse_left = True
        Mouse.mouse_event(2, 0, 0, 0, 0) # left down
    elif (joystick.get_axis(2) >= -0.2):
        mouse_left = False
        Mouse.mouse_event(4, 0, 0, 0, 0) # left up

    if -0.2 < mouse_scroll[1] < 0.2:
        pass
    else:
        print (mouse_scroll[1])
        







    clock.tick(60)















