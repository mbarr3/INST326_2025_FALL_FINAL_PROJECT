import random

def roll(rolls):
    """ 
    Summary: 
        Generates random numbers between 1-6 to simulate a dice roll 
        stores all the randomly generated numbers in a list to be returned 
    
    Args:
        rolls (int): The amount of random dice rolls you would like

    Returns:
        List: List with all the randomly rolled dice values in each index
    """
    back = list()
    count = 0
    while count < int(rolls):
           back.append(random.randint(1,6))
           count+=1
    return back