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
    
    while True:
        # TODO Does not print a understandable output (replaced with print loop below unless fix is found)
        # print(f"Your current cards: {[card for card in player.active_cards]}")
        
        # Print active cards to the player and their yard
        print("Your current active dog cards are:\n")
        for card in player.active_cards:
            print(f"{card}\n")
        print(f"Your yard: {sum(player.yard)}\n")
        old_card = input("\nWhich card would you like to remove a die from? ")
        old_value = (input("which die value would like to remove? "))
        
        # Validate user input
        try:
            old_value = int(old_value)
        except:
            print("\nInvalid Selection: You did not enter a number value.")
            continue
        
        found = False
        
        for card in player.active_cards:
            if card.name.lower() == old_card.lower() and old_value in card.req_dice.keys():
                if card.req_dice[old_value] == True:
                    card.req_dice[old_value] = False
                    found = True
        if found == False:
            print("Invalid selection: Either the card you selected was not "\
                "found or does not have the fulfilled die value you selected")
            continue
        else:
            break
        

    
    while True:
        new_value = int(input("Choose a new value for this die(1-6): "))
        
        try:
            new_value = int(new_value)    
        except:
            print("\nInvalid Selection: You did not enter a number value.")
            continue
            
        if new_value in range(1,7):
            break
        else:
            print(f"\nInvalid Selection: {new_value} is not a number between 1 and 6")
            continue
     
    bust_test = dp(player, [new_value]) 
    if bust_test == True:
        return bust_test

    print("\nYou now roll 2 dice")
    dice = rr(2)
    total_rolls.extend(dice)
    print(f"\nYour dice list is: {dice}")
    bust_test = dp(player, dice)
    return bust_test
