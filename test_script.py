""" file for testing code"""

from script import summary, points_plot


def test_summary():
    """test descriptive statistics function"""
    data = "NBA_24_stats.csv"
    summary(data)


def test_plot():
    """test plot function"""
    data = "NBA_24_stats.csv"
    points_plot(data)


if __name__ == "__main__":
    test_summary()
    test_plot()
