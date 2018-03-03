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



