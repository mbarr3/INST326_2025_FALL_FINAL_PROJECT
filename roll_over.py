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
        None 
        
    Author: 
    Technique:
    """
    hold = roll(len(player.yard))
    dice_placement(player, hold)
    hold = roll(1)
    dice_placement(player, hold)
    