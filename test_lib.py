"""file for testing lib.py"""

from lib import load_data


def test_load_data():
    """test load_data function"""
    dataset = "NBA_24_stats.csv"
    result_load = load_data(dataset)
    assert result_load is not None


if __name__ == "__main__":
    test_load_data()
