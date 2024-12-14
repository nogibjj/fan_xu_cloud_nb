"""main file with main functions"""

from lib import load_data
import matplotlib.pyplot as plt

data = "NBA_24_stats.csv"


def summary(dataset):
    """provides summary statistics"""
    df = load_data(dataset)
    summary_stats = df.describe()
    print(summary_stats)


def points_plot(dataset):
    """provides visualization"""
    df = load_data(dataset)
    accurate = df[df["3P%"] >= 0.5]
    player_rank = accurate["Player"].astype(str)
    plt.barh(player_rank, width=accurate["PTS"], color="green")
    plt.xlabel("PPG")
    plt.ylabel("Players")
    plt.title("PPG for Players with 50% or higher 3P%")
    plt.subplots_adjust(left=0.25)
    plt.savefig("NBA_pts_bar.png")
    plt.show()


if __name__ == "__main__":
    summary(data)
    points_plot(data)
