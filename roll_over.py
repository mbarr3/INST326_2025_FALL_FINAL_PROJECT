from random_roll import roll
from diceplacement import dice_placement

def rollover(player):
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
        if player.treats > 1:
            reroll = input(f"You have {player.treats}. Would you like to spend "\
                f"a treat to reroll? (y/n)")
            if reroll == "y" or reroll == "yes":
                continue
            elif reroll == "n" or reroll == "no":
                break
            else:
                print(f"{reroll} is not y or n")
                continue
        bust_test = dice_placement(player, hold)
        if bust_test == True:
            return bust_test
        print("\nNow you get to roll one die\n")
        hold = roll(1)
        bust_test = dice_placement(player, hold)
        if bust_test == True:
            return bust_test
    