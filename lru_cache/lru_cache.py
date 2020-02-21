from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.list = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            node = self.storage[key]

            #MRU at the tail
            self.list.move_to_end(node)

            return node.value
        else:
            return None


        # # key does not exit
        # if key not in self.storage:
        #     # return None
        #     return None
        # # if key exists
        # else:
        #     print(key, self.storage)
        #     # move pair to end

        #     def findNode(node):
        #         print(node.value, self.storage[key])
        #         if node.value is None:
        #             return
        #         elif node.value == self.storage[key]:
        #             return self.list.move_to_end(node)
        #         else:
        #             return findNode(node.next)

        #     findNode(self.list.head)

        #     # self.list.move_to_end(self.list[self.storage[key]])
        #     # get & return pair value
        #     return self.storage[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            node = self.storage[key]
            node.value = value
            self.list.move_to_end(node)
        else:
            if len(self.list) == self.limit:
                for name in self.storage:
                    if self.storage[name] is self.list.head:
                        del self.storage[name]
                        break
                self.list.remove_from_head()
            self.list.add_to_tail(value)
            self.storage[key] = self.list.tail
        
        

        # # if key exists
        # if self.storage[key] is not None:
        #     self.storage.update({key: value})
        # # cache not full
        # elif self.size < self.limit:    
        #     # add pair to dict
        #     self.storage.update({key: value})
        #     # move pair to tail (most recent)
            
        #     # self.list.add_to_tail({key: value})
        #     self.list.add_to_tail(value)

        #     #increment size
        #     self.size += 1
        # # cache full
        # else:
        #     # delete head (oldest)
        #     self.list.remove_from_head()
        #     # add pair to tail
        #     # self.list.add_to_tail({key: value})
        #     self.list.add_to_tail(value)
