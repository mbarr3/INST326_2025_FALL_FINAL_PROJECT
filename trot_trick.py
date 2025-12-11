from random_roll import roll as rr
from diceplacement import dice_placement as dp

def trot(player, total_rolls):
    """Function for the trot trick

    You may move 1 die on your dog cards to any other space, changing the number if 
    needed
    THEN 
    Roll 2 dice

    Args: 
        player (Player obj): provides Player attributes yard and active_cards which
            provides Card class obj attributes
    Side effects:
        Prints the player's active cards to the terminal
        Prompts the player to input which card they would like to remove a die 
            from, which die to remove, which card to place the die on, and what
            value to set the die to; these inputs are saved to variables
        The dice_placement function is called 

    Returns:
        None
        
    Author: Samuel Onakoya
    Technique:
    """
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
      
    # TODO We don't need this part if we call the dice_placement function since 
    # dice placement asks the player which card to place the value on we just need 
    # to ask what they want the value to be and pass it to dice placement
    print(f"Which card from the {[card.name for card in player.active_cards]} do you want to add a die to? ")
    new_card = input()
    
    dest = None
    for card in player.active_cards:
        if card.name.lower() == new_card.lower():
            dest = card
            break
            
    if dest is None:
        print("This card does not exist.")
        # TODO Need to add player input validation instead of kicking them out of the function with return
        #return
    
    new_value = int(input("Choose a new value for this die(1-6): "))
    
     
    bust_test = dp.dice_placement(player, [new_value]) 
    if bust_test == True:
        return bust_test

    dice = rr.roll(2)
    total_rolls.extend(dice)
    bust_test = dp.dice_placement(player, dice)
    if bust_test == True:
        return bust_test
