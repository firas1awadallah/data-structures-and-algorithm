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
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size
        self.__keys_order = []  

    def __hash(self, key):
        return sum([ord(str(char)) for char in key]) * 283 % self.__size

    def set(self, key, value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            self.__buckets[index] = LinkedList()
        self.__buckets[index].insert(key, value)
        if key not in self.__keys_order:
            self.__keys_order.append(key)  

    def get(self, key, default="NULL"):
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket:
            return bucket.search(key)
        return default

    def has(self, key):
        return self.get(key) is not None

    def get_keys(self):
        return self.__keys_order
    

# function that LEFT JOINs two hashmaps into a single data structure.

    def left_join(self, antonyms_table):
        """ 
        This method combines the keys and corresponding values from the current HashTable
        and the provided antonyms_table into a new data structure according to LEFT JOIN .
        Parameters:HashTable containing word strings as keys and antonyms of the keys as values.
        Returns: A list of lists containing the joined data. Each inner list contains three elements:
              1. The key from the current HashTable.
              2. The synonym value associated with the key in the current HashTable.
              3. The antonym value associated with the key in the provided antonyms_table.
              If the antonyms_table does not have a value for a key, the antonym_value will be "NULL".
              If the key does not exist in the current HashTable, the synonym_value will be None.
        """
        result = []
        keys = self.get_keys()  
        for key in keys:
            synonym_value = self.get(key)
            antonym_value = antonyms_table.get(key, "NULL")  
            result.append([key, synonym_value, antonym_value])
        return result


# example : 
synonyms_table = HashTable()
antonyms_table = HashTable()

synonyms_data = {
    "diligent": "employed",
    "fond": "enamored",
    "guide": "usher",
    "outfit": "garb",
    "wrath": "anger"
}

antonyms_data = {
    "diligent": "idle",
    "fond": "averse",
    "guide": "follow",
    "flow":  "jam",
    "wrath": "delight"
}

for key, value in synonyms_data.items():
    synonyms_table.set(key, value)

for key, value in antonyms_data.items():
    antonyms_table.set(key, value)

output = synonyms_table.left_join(antonyms_table)
print(output)



