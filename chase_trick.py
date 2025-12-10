from random_roll import roll
from diceplacement import dice_placement

def chase(player):
    """Function for the chase trick card

    Roll 1 die

    You may repeat this trick as many times as you want but each time roll 1 more 
    die than you just did (2, 3, 4...)

    Args: 
        player (Player obj): provides Player attributes yard and active_cards which
            provides Card class obj attributes
    Side effects:
        Establishes a count variable to track how many die the player has to roll
        Calls roll and dice placement functions
        Saves player input to a variable to determine if they roll again or not
    Returns:
        None
    Author: 
    Technique:
    """
    count = 1
    while True:
        hold = roll(count)
        bust_test = dice_placement(player,hold)
        if bust_test == True:
            return bust_test
        inp = input("Would you like to roll again with one more die than before? (y/n)")
        if inp == "y":
            count+=1
            continue
        elif inp == "n":
            break
        else:
            print(f"{inp} is not y or n")
            continue
    
    
        
    

