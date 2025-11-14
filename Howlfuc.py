import random

class player():
    '''
    Temporary player class to be implemented.
    
    '''
    pass

def howl(player):
    '''
Arguments:
    Player class object

Side-effects:
    If player has less than 6 cards call the deal function which will add 
    another card to the player’s dog cards Update the number of dog cards 
    attribute of the Player class object
    
Returns:
    None
    '''
    if len(player.cards) < 6:
        new_card = deal()
        r_num = random.randrange(0,5)
        player.cards.insert(r_num, new_card)