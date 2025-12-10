from random_roll import roll
from diceplacement import dice_placement
from player_card import Player, Card

def howl(Player):
    """Function for the Howl trick
        If player has less than 6 cards call the deal function which will add 
        another card to the player's dog cards. Then the player will roll one die.
    
    Arguments:
        Player class object
    Side-effects:
        Establishes a dice variable to save the value of the rolled die
        Calls the dice placement function to place the rolled die
    Returns:
        bust_test (bool): True/False returned by bust function in dice placement
        
    Author:
    """
    if Player.active_cards < 6:
        Player.active_cards.append(Card())
    dice = roll(1)
    bust_test = dice_placement(Player, dice)
    if bust_test == True:
        return bust_test