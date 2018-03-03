
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


def _find_lower_index(arr):
    lower = arr[0]
    lower_index = 0
    for i in range(1, len(arr)):
        if arr[i] < lower:
            lower = arr[i]
            lower_index = i

    return lower_index



