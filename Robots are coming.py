from gasp import *
from random import randint as rat
begin_graphics() 
finished= False


def place_player():
    player_x= rat(0,60)* 10
    player_y= rat(0,47)* 10 
    Circle((10 * player_x + 5, 10 * player_y + 5), 5, filled=True)
    print(" here i am")

    def moving_player(): print( "im moving rn")
    update_when('key_pressed')

    place_player()

    while not finished: 
        moving_player()
        end_graphics()