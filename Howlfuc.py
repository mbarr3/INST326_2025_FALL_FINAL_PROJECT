from random_roll import roll
from diceplacement import dice_placement
from player_card import Player, Card


def howl(Player):
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
    dice = roll(1)
    dice_placement(Player, dice)