from alaska.algorithms import binary_search
from alaska.algorithms import order_by_selection


def test_binary_search():
    test = list(range(1, 100))
    binary_search(test, 90)

def test_order_by_selection():
    arr = [5, 3, 6, 2, 10]
    print(order_by_selection(arr))



test_order_by_selection()