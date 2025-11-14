def update_card_status(required, rolled):
    """
    Side-effects:
        Compare the player's dice list to the card's required dice to see which match.
        If the player busts, clear the player's dice list.
        Update the card's status based on whether all required dice are matched.

    Returns:
        bool: True if the card is complete, False if still in progress.
    """

    need = required.copy()

    for d in rolled:
        if d in need:
            need.remove(d)
        else:
            rolled.clear()
            return False

    return len(need) == 0
