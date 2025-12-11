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
    while True:
        hold = roll(len(player.yard))
        total_rolls.extend(hold)
        
        reroll = None
        
        # Print dice list to the player
        print(f"Your rolled dice are: {hold}")
        
        if player.treats > 0:
            while True:
                reroll = input(f"You have {player.treats} treat(s). Would you like to spend "\
                    f"a treat to reroll? (y/n) ").lower()
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
        print("\nNow you get to roll one die\n")
        hold = roll(1)
        bust_test = dice_placement(player, hold)
        return bust_test
    