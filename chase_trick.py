"""Function for the chase trick card

Roll 1 die

You may repeat this trick as many times as you want but each time roll 1 more 
die than you just did (2, 3, 4...)
"""
import random_roll, dice_placment
def chase_trick(player):
    while True:
        count = 1
        hold = random_roll(count)
        dice_placment(player,hold)
        inp = input("would you like to roll again")
        if inp == "n":
            break
    
    
        
    

