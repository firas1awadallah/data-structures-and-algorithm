# from functools import reduce
# from operator import add

# class Node:
#     '''
#   A class represent a node in a linked list or other data structure each node has two main componenet the value of the node and the reference to the next node.
#   args: value
#   return : nothing
#   '''
#     def __init__(self, value):
#         self.next = None
#         self.value = value

# class HashTable:
#     '''
#      what : data structure that store key-value pairs of data using buckets to increace data accessing efficiency 
  
#     '''
#     def __init__(self, size=1024):
#         self.__size = size
#         self.__buckets = [None] * size
#         self.__keys = []  

#     def __hash(self, key):
#         return reduce(add, [ord(str(char)) for char in key]) * 283 % self.__size

#     class LinkedList:
#         '''
#         what : A class representing a singly linked list data structure
#         '''
#         def __init__(self):
#             self.head = None

#         def insert(self, value):
#             '''
#             insert a new node with the given value at the begining of     the linked list.
#             args: value
#             output : none
  
#             '''
#             new_node = Node(value)
#             new_node.next = self.head
#             self.head = new_node

#     def set(self, key, value):
#         '''
#     Set a key-value pair in the bucket, handling collisions as              needed.
#     Arguments:
#     key : The key to be hashed and used as the identifier for the           value.
#     value : the value that is aassociated with the key
#     Returns: None
#         '''
#         index = self.__hash(key)
#         if self.__buckets[index] is None:
#             ll = self.LinkedList()  
#             self.__buckets[index] = ll

#         self.__buckets[index].insert([key, value])
#         self.__keys.append(key)

#     def get(self, key):
#         '''
#     Retrieve the value with the given key from the hashtable
#     arg : key
#     return : value or None 
#          '''
#         index = self.__hash(key)
#         bucket = self.__buckets[index]
#         if bucket is not None:
#             curr = bucket.head
#             while curr:
#                 if curr.value[0] == key:
#                     return curr.value[1]
#                 curr = curr.next
#         return None

#     def has(self, key):
#         '''
#     A method to check if the given key exist in the hashtable.
#     arg: key
#     output: boolean
#     '''
#         return self.get(key) is not None

#     def keys(self):
#         '''
#             Return the keys attribute
#         '''  
#         return self.__keys  


from typing import Generic, TypeVar, Optional
K = TypeVar('K')
V = TypeVar('V')
class Hashtable(Generic[K, V]):
    def __init__(self, size: int = 100) :
        self._size: int = size
        self._buckets: list[Optional[list[tuple[K, V]]]] = [None] * size
    @property
    def size(self) :
        """
        Get the size of the hashtable
        """
        return self._size
    def set(self, key, value) :
        """
        Insert a new key-value pair into the hashtable
        """
        hash = self._hash(key)
        if (bucket := self._buckets[hash]) is None:
            bucket = []
        bucket.append((key, value))
        self._buckets[hash] = bucket
    def get(self, key) :
        """
        Get the value associated with a key
        """
        hash = self._hash(key)
        if (bucket := self._buckets[hash]) is None:
            return None
        for k, v in bucket:
            if k == key:
                return v
        return None
    def has(self, key) :
        """
        Check if a key exists in the hashtable
        """
        hash = self._hash(key)
        if (bucket := self._buckets[hash]) is None:
            return False
        for k, _ in bucket:
            if k == key:
                return True
        return False
    def keys(self) :
        """
        Get all the keys in the hashtable
        """
        keys = []
        for bucket in self._buckets:
            if bucket is not None:
                for k, _ in bucket:
                    keys.append(k)
        return keys
    def _hash(self, key) :
        """
        Hash a key
        """
        # from ascii to unicode
        hash: int = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
