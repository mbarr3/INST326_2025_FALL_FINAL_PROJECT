"""Function to represent the "Fetch" action in the Spots game. Fetch calls the 
future dice_roll function with an arg of 8 so it returns a list of 8 rolled dice.
Prompts the player to select a number from the rolled dice and validates that
input.

Side-effects:
    Saves the list returned by the dice_roll function to a variable
    Creates a chosen_num variable to store the player's input chosen number
    
Returns:
    A list of the rolled die that are the number input by the player
"""

def fetch():
    # Call another function that rolls the number of die provided as an int arg
    dice_roll(8)
    # Returns a list of the rolled dice 
    rolled = [1,2,5,1,4,1,6,3]
    print(rolled)
    # Prompt and validate user input (didn't reference a separate validation 
    # function due to player input being different for each instance it is required)
    while True:
        chosen_num = input("Choose one of the numbers present in the rolled dice" 
                           "(you will have to place or bury all dice of that "
                           "number): ")
        if isinstance(chosen_num, int):
            if chosen_num in range(1,7):
                if chosen_num in rolled:
                    break
        else:
            print(f"{chosen_num} is not present in the rolled dice")
            continue
        
    return [die for die in rolled if die == chosen_num]
            
