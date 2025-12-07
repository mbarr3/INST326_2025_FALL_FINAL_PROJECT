"""Function meant to track active and unactive trick cards and reset available 
tricks when applicable
"""

import random

# TODO For tracking active/inactive tricks
active_tricks = ['Chase', 'Fetch', 'Gobble', 'Howl', 'Roll Over', 'Trot']
inactive_tricks = []

# Trick descriptions
trick_descriptions = {
    'Chase': "Roll 1 die. You may repeat this trick as many times as you want but each time roll 1 more die than you just did (2, 3, 4...)", 
    'Fetch': "Roll 8 dice. Choose a number you rolled, and place or bury all dice of that number.Discard the rest.", 
    'Gobble': "Take 7 treats. Then return 1 treat for each spot in your highest unfilled space.", 
    'Howl': "If you have fewer than 6 dog cards, draw the top card of the dog deck and add it to your pack.Then roll 1 die.", 
    'Roll Over': "Roll all your buried dice and then place or rebury them. Then you may roll 2 dice.", 
    'Trot': "You may move 1 die on your dog cards to any other space, changing the number if needed. Then roll 2 dice."
}

def display_tricks():
    """Show available tricks"""
    print("\n" + "="*50)
    for i in range(len(active_tricks)):
        trick = active_tricks[i]
        print(f"{i+1}. {trick}: {trick_descriptions[trick]}")
    print("="*50)        
    return False

def select_trick():
    """Let player choose a trick"""
    display_tricks()
    
    while True:
        choice = input("\nChoose trick (number or name): ").strip()
        
        # Number selection
        if choice.isdigit() and 1 <= int(choice) <= len(active_tricks):
            return active_tricks[int(choice) - 1]
        
        # Name selection
        if choice in active_tricks:
            return choice
        
        print("Invalid choice. Try again.")


def use_trick(trick_name):
    """Move trick from active to inactive"""
    if trick_name in active_tricks:
        active_tricks.remove(trick_name)
        inactive_tricks.append(trick_name)


def refresh_tricks():
    """Move all tricks back to active"""
    active_tricks.extend(inactive_tricks)
    inactive_tricks.clear()
    print("\nAll tricks refreshed!")