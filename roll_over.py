from random_roll import roll
from diceplacement import dice_placement

def rollover(player, total_rolls):
    """Function for the roll over trick card

    Roll all your buried dice and then place or rebury them
    THEN
    You may roll 1 die

    Args: 
        player (Player obj): provides Player attributes yard and active_cards which
            provides Card class obj attributes
        total_rolls (list): list of all dice rolled throughout the game
    Side effects:
        Prints rolled dice to terminal
        If applicable, prints prompt to the terminal to spend a treat or not
        If input error prints error message to the terminal
        Updates player obj treat attribute if applicable
        If applicable, sets player yard attribute to empty list
        If player yard attribute empty:
            prints info message to terminal
        Adds rolled dice to total_rolls
        Prints info message to player that they will roll 1 die
        Prints rolled die 
        If applicable, prints prompt to the terminal to spend a treat or not
        If input error prints error message to the terminal
        Updates player obj treat attribute if applicable
        Adds rolled dice to total_rolls
    Returns:
        bust_test (bool): True or False as returned by the bust function 
        
    Author: Mackenzie Barrett
    """
    
    if len(player.yard) > 0:
        while True:
            hold = roll(len(player.yard))
            
            reroll = None
            
            # Print dice list to the player
            print(f"Your rolled dice are: {hold}")
            
            if player.treats > 0:
                while True:
                    reroll = input(f"You have {player.treats} treat(s). Would "\
                        f"you like to spend a treat to reroll? (y/n) ").lower()
                    if reroll not in ['yes', 'y', 'no', 'n']:
                        print(f"{reroll} is not y or n")
                        continue
                    else:
                        break
            
            # Restart function if they want to spend a treat  
            if reroll == "y" or reroll == "yes":
                player.treats-=1
                continue
            
            total_rolls.extend(hold)
            
            # Update player yard
            player.yard = list()
        
            bust_test = dice_placement(player, hold)
            if bust_test == True:
                return bust_test
            else:
                break
            
    else:
        print("\nYour yard was empty so you skip to rolling a die.")
    
    print("\n***~~~Now you roll one die~~~***")
    while True:
        hold = roll(1)
        print(f"\nYour rolled dice are: {hold}")
        if player.treats > 0:
            while True:
                reroll = input(f"You have {player.treats} treat(s). Would you like to spend "\
                    f"a treat to reroll? (y/n) ").lower()
                if reroll not in ['yes', 'y', 'no', 'n']:
                    print(f"{reroll} is not y or n")
                    continue
                else:
                    break
        
        # Restart loop if they want to spend a treat  
        if reroll == "y" or reroll == "yes":
            player.treats-=1
            continue
        
        total_rolls.extend(hold)
        bust_test = dice_placement(player, hold)
        return bust_test
    