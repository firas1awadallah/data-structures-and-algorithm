class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.

        Args:
            value: The value to be appended.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def zip_lists(list1, list2):
    """
    Zips two linked lists together, alternating nodes from each list.

    Args:
        list1: The first linked list.
        list2: The second linked list.

    Returns:
        A new linked list obtained by alternating nodes from list1 and list2.
    """
    if not list1:  # If list1 is empty, return list2
        return LinkedList(list2.head) if list2.head else None
    if not list2:  # If list2 is empty, return list1
        return LinkedList(list1.head) if list1.head else None

    new_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        new_list.append(current1.value)
        new_list.append(current2.value)
        current1 = current1.next
        current2 = current2.next

    while current1:
        new_list.append(current1.value)
        current1 = current1.next

    while current2:
        new_list.append(current2.value)
        current2 = current2.next

    return new_list



my_list1 = LinkedList()
my_list2 = LinkedList()
my_list1.append(1)
my_list1.append(3)
my_list1.append(5)
my_list2.append(2)
my_list2.append(4)
my_list2.append(6)



result = zip_lists(my_list1, my_list2)
current = result.head
while current:
    print(current.value, end=" -> ")
    current = current.next
print(None)
