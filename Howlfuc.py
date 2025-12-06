import random


def deal(player):
    """
    A method of the card class to be implemented in the future, It will create a
    new Card class object and assign that to the player's list of cards
    """
    player.active_cards.append(Card())



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
        new_card = deal()
        
    random_roll()