import pandas as pd
import matplotlib.pyplot as plt


def stats(total_rolls):
    """_summary_

    Args:
        total_rolls (List): Takes a list of intigers and converts it into a DF
        and generates a bar graph to show the roll values rolled the whole game
        
    Author: Sean Tully
    """
    df = pd.DataFrame(total_rolls, columns=["Roll Value"])
    counts = df["Roll Value"].value_counts().sort_index()
    plt.figure(figsize=(8,5))
    counts.plot(kind="bar")
    plt.xlabel("Value Rolled")
    plt.ylabel("Times Rolled")
    plt.title("End Game Roll Stats")
    plt.show()