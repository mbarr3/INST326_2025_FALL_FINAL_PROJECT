"""Function meant to track and clear all uncompleted and unlocked dog cards and 
yard when a player busts
"""
def bust (player):
    total = 0
    for dye in player.yard:
        total+=dye
    if total > 7:
        player.yard = list()
        player.active_cards = list()