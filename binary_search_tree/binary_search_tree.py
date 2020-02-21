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
        # insert into RIGHT subtree
        elif value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # inserts into LEFT subtree
        else:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)


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
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value == None:
            return
        else:
            cb(self.value)

            if self.left: 
                self.left.for_each(cb)
            if self.right:
                self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # L Root R
        # 1. Base Case
            # at the bottom of the tree
        if node is None:
            return
        
        # 2. Recursive Case
            # go left as far as possible
        self.in_order_print(node.left)
        print(node.value)
            # go right as far as possible
        self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # setup a queue [node to backtrack to]
        queue = Queue()
        # init with 'node'
        queue.enqueue(node)

        # while queue is NOT empty
        while queue.size > 0:
            print(queue.size)

            if queue.storage.head is not None:
                # print node
                print('curr head, ', queue.storage.head.value.value)

                if queue.storage.head.value is not None:
                    # enqueue node.left, node.right
                    if queue.storage.head.value.left is not None:
                        print('left', queue.storage.head.value.left.value)
                        queue.enqueue(queue.storage.head.value.left)

                    if queue.storage.head.value.right is not None:
                        print('right', queue.storage.head.value.right.value)
                        queue.enqueue(queue.storage.head.value.right)
                

            # dequeue node
            print('dequeue', queue.storage.head.value.value)
            queue.dequeue()


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # set up a stack [node we backtrack to]
        # init with 'node'
        
        # while stack NOT empty
            # pop node from stack
            # print value
            # push node.left, node.right

        # print given node

        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
