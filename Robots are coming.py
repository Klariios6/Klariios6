from gasp import *
from random import randint
begin_graphics() 
finished= False


def place_player():
    player_x= randint(0,60) # the X coordinate of the player
    player_y= randint(0,47) # the y coordinate of the player 
    c= Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True) 
    print("here i am")
    player_physical= int(c)


    def moving_player(): 
        while True: 
            x= +4
            y= +3  
            c= +5 
            ball_x=Circle((x,y), c)
            move_to= ball_x
            sleep(.02)
            if x> 635: break
            else: move_to(ball_x)
            ()       

    place_player()

    while not finished: 
        moving_player()


    remove_from_screen(c) 
            
            
    end_graphics()