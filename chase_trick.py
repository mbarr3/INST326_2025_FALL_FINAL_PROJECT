from random_roll import roll
from diceplacement import dice_placement

def chase(player, total_rolls):
    """Function for the chase trick card

    Roll 1 die

    You may repeat this trick as many times as you want but each time roll 1 more 
    die than you just did (2, 3, 4...)

    Args: 
        player (Player obj): provides Player attributes yard and active_cards which
            provides Card class obj attributes
        total_rolls (list): list of all dice rolled throughout the game 
    Side effects:
        Prints rolled dice to the terminal
        If applicable, prints prompt to the terminal to spend a treat or not
        If input error prints error message to the terminal
        Updates player obj treat attribute if applicable 
        Adds rolled dice to total_rolls
        Prints prompt to roll again or not
    Returns:
        bust_test (bool): True or False as returned by the bust function
        
    Author: Noah Aurdos
    """
    
    count = 1
    
    while True:
        hold = roll(count)
        total_rolls.extend(hold)
        reroll = None
        
        print(f"\nDice amount: {count} | Your rolled dice are: {hold}")
        
        if player.treats > 0:
            while True:
                reroll = input(f"You have {player.treats} treat(s). Would you like to spend "\
                    f"a treat to reroll? (y/n) ").lower()
                if reroll not in ['yes', 'y', 'no', 'n']:
                    print(f"{reroll} is not y or n")
                    continue
                else:
                    break
        
        if reroll == "y" or reroll == "yes":
            player.treats -= 1
            continue
            
        bust_test = dice_placement(player, hold)

        if bust_test == True:
            return True
        
        # Validate user input
        while True:
            inp = input(f"Would you like to roll again with {count+1} dice this"\
                f" time? (y/n) ")
            if inp not in ['yes', 'y', 'no', 'n']:
                print(f"{inp} is not y or n")
                continue
            else:
                break
            
        if inp == "y" or inp == "yes":
            count += 1
            continue
        elif inp == "n" or inp == "no":
            break
    
    return False