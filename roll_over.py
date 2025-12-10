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
    hold = roll(len(player.yard))
    bust_test = dice_placement(player, hold)
    if bust_test == True:
        return bust_test
    hold = roll(1)
    bust_test = dice_placement(player, hold)
    if bust_test == True:
        return bust_test
    