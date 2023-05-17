class Node : 
    def __init__(self, value,_next=None):
        self.value = value
        self.next = _next

class LinkedList :
    def __init__(self,head=None):
        self.head = head

    def insert (self, value) : 
         new_node = Node(value)
         new_node.next = self.head
         self.head = new_node

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        if self.head is None:
            return "None"

        current = self.head
        result = ""
        while current is not None:
            result += "{ " + str(current.value) + " } -> "
            current = current.next
        result += "None"
        return result
    
    def append(self, new_value):
        new_node = Node(new_value)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return

        if self.head.value == value:
            # If the value is found at the head, insert the new node before it
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                # If the value is found in the next node, insert the new node before it
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        # If the value is not found in the list, the new node will be added at the end
        current.next = new_node
    
    def insert_after(self, value, new_value):
        new_node = Node(new_value)

        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return

        current = self.head
        while current:
            if current.value == value:
                # If the value is found, insert the new node after it
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current:
            print(f'{{{current.value}}} ->', end=' ')
            current = current.next
        print('X')

    def kthFromEnd(self, k):
        if self.head is None:
            return "Linked list is empty."

        first = self.head
        second = self.head

        count = 0
        while count < k:
            if second.next is None:
                return "Exception"
            second = second.next
            count += 1
# moves the second pointer k steps from ahead 
# count to  track of the number of steps
        while second.next:
            first = first.next
            second = second.next
# move the first and second pointers 
# second reaches the last node
# first pointer ends up at the node that is k steps 
        return first.value


my_list = LinkedList()
my_list.insert("c")
my_list.insert("b")
my_list.insert("a")
print(my_list.includes("b")) 
print(my_list.includes("d")) 
print(my_list.to_string())  


my_list.append(2)
my_list.append(5)
my_list.traverse()

my_list.insert_before(2, 1)
my_list.insert_before(5, 4)
my_list.traverse()

my_list.insert_after(2, 3)
my_list.insert_after(5, 6)
my_list.traverse()

print(my_list.kthFromEnd(0))  
print(my_list.kthFromEnd(1))  
print(my_list.kthFromEnd(2))
print(my_list.kthFromEnd(3))    
print(my_list.kthFromEnd(9))  # return Exception
print(my_list.kthFromEnd(-1)) # return last bode value 6

# python python/linked-list/linked_list/linked_list.py
# pytest