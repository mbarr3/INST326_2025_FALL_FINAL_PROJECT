import dice_placement
import random_roll

"""Function for the roll over trick card

Roll all your buried dice and then place or rebury them
THEN
You may roll 1 die
"""

def rollover(player):
    hold = random_roll(len(player.yard))
    dice_placement(player, hold)
    hold = random_roll(1)
    dice_placement(player, hold)
    