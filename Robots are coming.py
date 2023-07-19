from gasp import *
from random import randint
begin_graphics() 
finished= False
player_x= randint(1, 63)
player_y= randint(1, 47) 
Robot_1= randint(1,63) # this is for the x 
robot_2= randint(1,47) # this is for the y 


def place_player(): #This is the function that moves the player 
        global player_x, player_y, c
c= Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True) 
print("here i am")
()

def moving_player(): 
    global player_x, player_y, c
    key= update_when('key_pressed')
    print( 'player is moving')
    while  key == 'z':
          print('re-spawn')
    remove_from_screen(c)
    place_player()
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
     a= Circle(( 10* robot_2, 10* Robot_1), 5, filled=True) # Robot entity circle
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

def found_each_other(): #when the bots are equal to each other
     global robot_2, Robot_1, player_x, player_y
     if Robot_1 == player_x: Finished= True
print( 'BOOM')
if robot_2 == player_y: finished= True 
print( 'BOOM ')
()

place_robot()
move_robot()
place_player()            
moving_player()
found_each_other() 
sleep(.02)
end_graphics()