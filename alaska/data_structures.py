
class Node(object):

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

class UnorderedList(object):

    def __init__(self):
        self.head = None

    def __bool__(self):
        return  self.head is None

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next

        return count
