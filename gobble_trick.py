"""Function for the gobble trick card

Take 7 treats
THEN
Return 1 treat for each spot in your highest unfilled space

(suggestion: maybe do a set intersection of the cards' required dice and 
fulfilled dice and then list sorting to return the highest overall required dice
from a list of all the uncompleted cards the player has)
"""
def gobble_trick(player):
    treat = 7
    blank_max = 0
    for card in player.active_cards:
        for dice in card.req_dice:
            if not card.req_dice[dice]:
                blank_max = dice 
    player.treats = treat - blank_max
            