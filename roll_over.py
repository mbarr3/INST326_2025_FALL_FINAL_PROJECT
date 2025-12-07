import dice_placement

"""Function for the roll over trick card

Roll all your buried dice and then place or rebury them
THEN
You may roll 1 die
"""
import random_roll
def roll_over(player):
    hold = random_roll(len(player.yard))
    dice_placement(player, hold)
    hold = random_roll(1)
    dice_placement(player, hold)
    