import random
import random_roll

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
    if player.total_cards < 6:
        new_card = player.active_cards.append(Card())
        
    random_roll(1)