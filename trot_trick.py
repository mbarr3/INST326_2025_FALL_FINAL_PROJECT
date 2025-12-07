import random_roll as rr
import dice_placement as dp
from Spots import Player, Card

"""Function for the trot trick

You may move 1 die on your dog cards to any other space, changing the number if 
needed
THEN 
Roll 2 dice
"""

def trot(player, Selected_die):
    old_card = None
    old_place = None
    
    for card in player.active_cards:
        for place, value in card.req_dice_items():
            if value == Selected_die:
               old_card = value
               old_place = place
               break
           
    if old_card is None:
        print("Selected card doesn't exist")
        return
    
    old_card.req_dice[old_place] = None
    
    dp.dice_placement(Player, [Selected_die])
    
    rr.roll(2)