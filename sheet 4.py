from random import randint as r
x= r(1,1000)
question= (input('what is your guess'))
answer= int(question)
tries=0
 
while True:
    tries += 5

    if answer> x: print(' go lower')
    elif answer< x: print('go higher')
    else: print('yummy')

    play_again=input("play again yes or no? ")
    if play_again.lower() != "yes": 
        break
    ()
