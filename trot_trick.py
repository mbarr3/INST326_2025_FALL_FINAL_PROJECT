from random_roll import roll as rr
from diceplacement import dice_placement as dp

"""Function for the trot trick

You may move 1 die on your dog cards to any other space, changing the number if 
needed
THEN 
Roll 2 dice
"""

def trot(player):
    print(f"Your current cards: {[card.name for card in player.active_cards]}")
    old_card = input("Which card would you like to remove a die from? ")
    old_value = int(input("which die would like to remove? "))
    
    found = False
    
    for card in player.active_cards:
        if card.name.lower() == old_card.lower():
            for place, value in card.req_dice.items():
                if value == old_value:
                    card.req_dice[place] = None
                    found = True
                    break
            if found == True:
                break
                
    print(f"Which card from the {[card.name for card in player.active_cards]} do you want to add a die to? ")
    new_card = input()
    
    dest = None
    for card in player.active_cards:
        if card.name.lower() == new_card.lower():
            dest = card
            break
            
    if dest is None:
        print("This card does not exist.")
        return
    
    new_value = int(input("Choose a new value for this die(1-6): "))
    
    dp.dice_placement(player, [new_value]) 
    rr.roll(2)
    