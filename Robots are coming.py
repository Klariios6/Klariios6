from gasp import *
from random import randint  
player_x= randint(1, 63)
player_y= randint(1, 47) 
Robot_1= randint(1,63) # this is for the x 
robot_2= randint(1,47) # this is for the y 


def place_player(): #This is the function that moves the player 
        global player_x, player_y
c= Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True, color =color.GREEN) 
print("here i am")
()

def moving_player(): 
    global player_x, player_y, c
    key= update_when('key_pressed')
    print( 'player is moving')
    while  key == 'q':
          print('bye')
    remove_from_screen(c)
    safe_player()
    if key == "w" and player_y <47: 
        player_y += 1
    if key == "s" and player_y > 1: 
        player_y -= 1
    if key == "a" and player_x > 1: 
        player_x -= 1
    if key == "d" and player_x< 63: 
        player_x += 1

move_to(c,( player_x *10, player_y * 10), 5, filled=True)
()

def place_robot():
     global a, robot_2, Robot_1 
     a= Circle(( 10* robot_2, 10* Robot_1), 5, filled=True, color= color.RED) # Robot entity circle
     ()
def move_robot(): 
 global robot_2, Robot_1, a #uses defined a as robot
if robot_2 > player_y:
 robot_2 -= 1
if robot_2 < player_y: 
 robot_2 += 1
if Robot_1 > player_x:
 Robot_1 -= 1 
if Robot_1 < player_x:
 Robot_1 += 1
move_to(a(10* robot_2, Robot_1 *10), 5, filled=True)
()

def check_collisions():
    global finished
    if player_x == Robot_1 and player_y == robot_2:
        Text("CACHOW!", (320, 240), size=20)
        sleep(2)
        finished = True

def safe_player():
    place_player()
while player_x == Robot_1 and player_y == robot_2:
    place_player()

begin_graphics()
finished = False

safe_player()
place_robot()
while not finished:
 moving_player()
 move_robot()
 check_collisions()
end_graphics()