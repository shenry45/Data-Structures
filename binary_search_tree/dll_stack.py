import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # adding to top of stack
    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    # remove from top of stack
    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            current_tail = self.storage.tail.value
            self.storage.remove_from_tail()
            return current_tail

    def len(self):
        return self.size
