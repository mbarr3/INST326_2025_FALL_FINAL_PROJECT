import random_roll
from Spots import Player, Card

def howl():
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
    random_roll(1)