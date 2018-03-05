from alaska.algorithms import binary_search, order_by_selection, recursive_factorial, quicksort



def test_binary_search():
    test = list(range(1, 100))
    binary_search(test, 90)

def test_order_by_selection():
    arr = [5, 3, 6, 2, 10]
    print(order_by_selection(arr))

def test_recursive_factorial():
    print(recursive_factorial(5))


def test_quick_sort():
    print(quicksort([3, 6, 7, 1, 2, 12, 9, 4, 5, 3, 6]))


test_quick_sort()