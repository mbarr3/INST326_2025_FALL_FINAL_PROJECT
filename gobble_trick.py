"""Function for the gobble trick card

Take 7 treats
THEN
Return 1 treat for each spot in your highest unfilled space

"""
from random_roll import roll
from diceplacement import dice_placement

def gobble(player):
    treat = 7
    blank_max = 0
    for card in player.active_cards:
        for dice in card.req_dice:
            if not card.req_dice[dice]:
                if blank_max < dice:
                    blank_max = dice
    player.treats = treat - blank_max
            