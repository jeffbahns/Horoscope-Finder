# Coin Flip Simulation

from random import random
from time import sleep

def coin_flip():
    if random() >= .5:
        return True
    else:
        return False

def main():
    heads = 0
    tails = 0
    n = int(input("How many times would you like to flip the coin?  "))

    for i in range(n):
        if coin_flip():
            heads+=1
            print ("Roll {}, heads!".format(str(i+1)))
        else:
            tails+=1
            print ("Roll {}, tails!".format(str(i+1)))
        sleep(1)
    if heads > tails:
        winner = "Heads Wins!"
    elif tails > heads:
        winner = "Tails Wins!"
    else:
        winner = "There was a tie!"
        
    print ("_______________________________________\nTOTAL SCORE:")
    print ("Heads: {}".format(str(heads)))
    print ("Tails: {}".format(str(tails)))
    print (winner)

main()

