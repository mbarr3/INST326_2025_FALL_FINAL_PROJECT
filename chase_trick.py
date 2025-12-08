"""Function for the chase trick card

Roll 1 die

You may repeat this trick as many times as you want but each time roll 1 more 
die than you just did (2, 3, 4...)
"""
from random_roll import roll
from diceplacement import dice_placement

def chase(player):
    while True:
        count = 1
        hold = roll(count)
        dice_placement(player,hold)
        inp = input("Would you like to roll again with one more die than before? (y/n)")
        if inp == "y":
            count+=1
            continue
        elif inp == "n":
            break
        else: # TODO Need to adjust where it continues to ask if they want to roll again until valid input
            print(f"{inp} is not y or n")
            continue
    
    
        
    

