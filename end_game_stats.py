import pandas as pd
import matplotlib.pyplot as plt


def stats(total_rolls):
    df = pd.DataFrame(total_rolls, columns=["Roll Value"])
    counts = df["Roll Value"].value_counts().sort_index()
    plt.figure(figsize=(8,5))
    counts.plot(kind="bar")
    plt.xlabel("Value Rolled")
    plt.ylabel("Times Rolled")
    plt.title("End Game Roll Stats")
    plt.show()