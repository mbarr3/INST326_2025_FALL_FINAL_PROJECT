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
    Side effects:
        Calls roll and dice placement functions
    Returns:
        bust_test (bool): True/False from bust function 
        
    Author: 
    Technique:
    """
    
    if len(player.yard) > 0:
        while True:
            hold = roll(len(player.yard))
            player.yard = list()
            total_rolls.extend(hold)
            
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
        
            bust_test = dice_placement(player, hold)
            if bust_test == True:
                return bust_test
    else:
        print("\nYour yard was empty so you skip to rolling a die.")
    
    print("\n***~~~Now you roll one die~~~***")
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
    bust_test = dice_placement(player, hold)
    return bust_test
    