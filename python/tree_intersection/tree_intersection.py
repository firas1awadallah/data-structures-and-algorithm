class Tnode:
   

    def __init__(self, value, right=None, left=None):
       
        self.value = value
        self.right = right
        self.left = left

    
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None


class Tree:
   

    def __init__(self):
       
        self.root = None

    def __str__(self):
     
        if self.root is None:
            return "this Tree is empty"
        return f"the Tree root = {self.root.value},"

    
    
class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        return sum([ord(str(char)) for char in key]) * 283 % self.__size

    def set(self, key, value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            self.__buckets[index] = LinkedList()
        self.__buckets[index].insert(key, value)

    def get(self, key):
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket:
            return bucket.search(key)
        return None

    def has(self, key):
        return self.get(key) is not None

    def get_keys(self):
        keys = []
        for bucket in self.__buckets:
            if bucket:
                curr = bucket.head
                while curr:
                    keys.append(curr.key)
                    curr = curr.next
        return keys
  

class Binary_Search_Tree(Tree):
   

    def __init__(self, root=None):
     
        self.root = root

    def __str__(self):
    
        if self.root is None:
            return "This binary tree is empty"

        return f"The tree root = {self.root.value}"

    def add(self, value):
     
        tn_value = Tnode(value)

        def _walk(root):
            
            if root.value <= tn_value.value:
                if root.right:
                    _walk(root.right)
                else:
                    root.right = Tnode(value)

            if root.value > tn_value.value:
                if root.left:
                    _walk(root.left)
                else:
                    root.left = Tnode(value)

        _walk(self.root)



def tree_intersection(t1, t2):
    hasht = HashTable()
    common_values = []

    def _walk_t1(node):
        if node:
            hasht.set(str(node.value), 0)
            _walk_t1(node.left)
            _walk_t1(node.right)

    _walk_t1(t1.root)

    def _walk_t2(node):
        if node:
            if hasht.has(str(node.value)):
                common_values.append(str(node.value))
            _walk_t2(node.left)
            _walk_t2(node.right)

    _walk_t2(t2.root)

    return common_values







if __name__ == "__main__":
    tn1 = Tnode(10)
    t1 = Binary_Search_Tree(tn1)
    t1.add(17)
    t1.add(9)
    t1.add(11)
    t1.add(30)
    tn2 = Tnode(10)
    t2 = Binary_Search_Tree(tn2)
    t2.add(7)
    t2.add(9)
    t2.add(11)
    t2.add(40)

    print(tree_intersection(t1, t2))




   