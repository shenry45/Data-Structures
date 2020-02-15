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
        self.size += 1
        self.storage.add_to_tail(value)

    # removing
    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            current_head = self.storage.head.value
            self.storage.remove_from_head()
            return current_head

    def len(self):
        return self.size
