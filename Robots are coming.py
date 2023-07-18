from gasp import *
from random import randint
begin_graphics() 
finished= False


def place_player():
    player_x= randint(1,60) # the X coordinate of the player
    player_y= randint(1,47) # the y coordinate of the player 
    c= Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True) 
    print("here i am")
    player_shape= str(c)
    
    key = update_when('key_pressed')

    if key == '6' and player_x < 63:
        player_x += 1
    elif key == '3':
        if player_x < 63:
            player_x += 1
        if player_y > 0:
            player_y -= 1

    # You fill in the rest here...

    move_to(player_shape, (10 * player_x + 5, 10 * player_y + 5))
()

def moving_player(): 
        while True: 
            x= +4
            y= +3  
            R= +5 
            ball_x=Circle((x,y), R)
            move_to= ball_x

            if x> 635: break
            else: move_to(ball_x)
           
            ()       

place_player()            
moving_player()
remove_from_screen() 
sleep(.02)
end_graphics()