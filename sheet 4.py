from random import randint as r
x= r(1,1000)
question= (input('what is your guess'))
answer= int(question)
tries=0

#print("great" if answer== x else print("wrong"))

while True:
    tries += 1

    if answer> x: print(' go lower')
    elif answer< x: print('go higher')
    else: print('yummy')

    play_again=input("play again yes or no? ")
    if play_again.lower() != "no": 
        break
    ()


#else: print(' Whoops, your value is lower')
#elif answer>x: print (' number is lower than the value ')()

#x <1000:
    #print( 'x is lower than the number you typed')

    
    

#answer !=  100


#while True: 
   # x= r(1,1000)
   # print(x)
   # if x < 100 
   # print( 'go lower')
   

