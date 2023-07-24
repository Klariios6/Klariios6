from gasp import * 
from random import randint
player_x = 1
player_y = 1
robot_1 = randint(0, 63)
robot_2 = randint(0, 47)

def place_robot():
    global b
    b = Circle((10 * robot_1 +5 , 10 * robot_2 + 5), 5 , color =color.GREEN)

def move_robot():
    global robot_1, robot_2, b
    print('Robot is going after you')
    if robot_2 > player_y:
        robot_2 -= 1
    if robot_2 < player_y:
        robot_2 += 1
    if robot_1 > player_x:
        robot_1 -= 1
    if robot_1 < player_x:
        robot_1 += 1
    move_to(b, (10 * robot_1, 10 * robot_2))
    
def place_player():
    global c, player_x, player_y
    player_x = randint(0, 63) 
    player_y = randint(0, 47)
    c = Circle((10 * player_x + 5 , 10 * player_y + 5), 5, filled = True, color = color.RED)

def move_player():
    global player_x, player_y, c
    print('Player is moving')
    key = update_when('key_pressed')
    while key == 'q':
        print('teleport')
        remove_from_screen(c)
        safe_player()
        key = update_when('key_pressed')
    if key == 'w' and player_y <47:
        player_y += 1
    if key == 's' and player_y >1:
        player_y -=1
    if key == 'a' and player_x >1:
        player_x -= 1
    if key == 'd' and player_x <63:
        player_x += 1
    
    move_to(c, (10 * player_x, 10 * player_y))
def check_collisions():
    global finished
    if player_x == robot_1 and player_y == robot_2:
        Text("WHOOPS!", (320, 240), size=20)
        sleep(2)
        finished = True
def safe_player():
    place_player()
while player_x == robot_1 and player_y == robot_2:
    place_player()

begin_graphics()
finished = False

safe_player()
place_robot()
while not finished:
    move_player()
    move_robot()
    check_collisions()
end_graphics()