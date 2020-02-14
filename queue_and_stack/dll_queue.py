import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # adding
    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    # removing
    def dequeue(self):
        self.storage.remove_from_tail()
        self.size -= 1

    def len(self):
        return self.size
