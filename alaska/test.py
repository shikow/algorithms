from alaska.algorithms import binary_search, order_by_selection, recursive_factorial



def test_binary_search():
    test = list(range(1, 100))
    binary_search(test, 90)

def test_order_by_selection():
    arr = [5, 3, 6, 2, 10]
    print(order_by_selection(arr))

def test_recursive_factorial():
    print(recursive_factorial(5))


test_recursive_factorial()