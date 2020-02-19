import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # base case
        if value is None:
            return
        # base case for vertices
        elif self.value is None:
            self.value = BinarySearchTree(value)
        # if vertex is less than parent vertex value
        elif self.value > value:
            # if vertex left is None (default)
            if self.left is None:
                # assign tree to left
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # if vertex is greater than parent vertex value
        elif self.value <= value:
            # if vertex right is None (default)
            if self.right is None:
                # assign tree to right
                self.right = BinarySearchTree(value)
            else:
                # assess right tree and recurse
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value is None:
            return
        elif self.value == target:
            return True
        else:
            if self.left is not None and self.right is not None:
                return self.left.contains(target) or self.right.contains(target)
            elif self.left is not None: 
                return self.left.contains(target)
            elif self.right is not None:
                return self.right.contains(target)
            else:
                return

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
