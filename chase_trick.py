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
    Side effects:
        Establishes a count variable to track how many die the player has to roll
        Calls roll and dice placement functions
        Saves player input to a variable to determine if they roll again or not
    Returns:
        bust_test (bool): True/False from bust function
    Author: Noah Aurdos
    Technique: Conditional expressions
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

        if bust_test:
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