import random

def player_class():
    '''
    Temporary player class to be implemented.
    This functions is not final 
    '''
    player_class = [] # list of player cards
    return player_class


def card_class(new_card_dice):
    """
    Card class that is a composition from the player class. 
    
    """
    

def deal():
    """
    A method of the card class to be implemented in the future, It will chose a random variable 
    name from a list of name and generate a random number of die between 1-4
    and values for each dice. 
    """
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