import random_roll
import dice_placement

def howl(player):
    """
Arguments:
    Player class object

Side-effects:
    If player has less than 6 cards call the deal function which will add 
    another card to the player's dog cards. Then the player will roll one die.
    
Returns:
    None
    """
    if Player.active_cards < 6:
        Player.active_cards.append(Card())
    dice = random_roll(1)
    dice_placement(player, dice)