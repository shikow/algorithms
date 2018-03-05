from random import randrange

def binary_search(search_itens, item):
    min_position = 0
    high_position = len(search_itens) - 1

    while min_position <= high_position:
        mid = (min_position + high_position) // 2
        finded_item = search_itens[mid]
        if finded_item == item:
            return mid
        elif finded_item > item:
            high_position = mid - 1
        else:
            min_position = mid + 1

    return None


def order_by_selection(arr):
    new_arr = []
    for i in range(len(arr)):
        lower = _find_lower_index(arr)
        new_arr.append(arr.pop(lower))

    return new_arr


def recursive_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)


def recursive_sum(arr):

    if not arr:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])


def recursive_count(arr):

    if not arr:
        return 0
    else:
        return 1 + recursive_count(arr[1:])


def recursive_max_value(arr):

    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    max_value = recursive_max_value(arr[1:])
    return arr[0] if arr[0] > max_value else max_value


def quicksort(arr):

    if len(arr) <= 1:
        return arr
    else:
        next_position = randrange(len(arr))
        pivot = arr[next_position]
        lowers = [item for i, item in enumerate(arr) if item <= pivot and i != next]
        highers = [item for i, item in enumerate(arr) if item > pivot and i != next]
        return quicksort(lowers) + [pivot] + quicksort(highers)


def _find_lower_index(arr):
    lower = arr[0]
    lower_index = 0
    for i in range(1, len(arr)):
        if arr[i] < lower:
            lower = arr[i]
            lower_index = i

    return lower_index



