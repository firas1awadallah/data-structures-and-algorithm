from linked_list_zip.linked_list_zip import zip_lists, LinkedList


def create_linked_list(values):
    if not values:
        return None

    head = LinkedList()
    for value in values:
        head.append(value)

    return head


def linked_list_to_list(head):
    result = []
    current = head.head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Both lists are empty
def test_zip_lists_empty_lists():
    list1 = LinkedList()
    list2 = LinkedList()
    result = zip_lists(list1, list2)
    assert linked_list_to_list(result) == []

# One list is empty, the other is not
def test_zip_lists_one_list_empty():
    list1 = LinkedList()
    list2 = LinkedList()
    list2.append(1)
    result = zip_lists(list1, list2)
    assert linked_list_to_list(result) == [1]

# Both lists have one element
def test_zip_lists_both_lists_one_element():
    list1 = LinkedList()
    list1.append(1)
    list2 = LinkedList()
    list2.append(2)
    result = zip_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 2]

# Both lists have multiple elements of the same length
def test_zip_lists_same_length_lists():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    result = zip_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3, 4]

# List 1 is longer than list 2
def test_zip_lists_list1_longer():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list2 = LinkedList()
    list2.append(2)
    result = zip_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 3]

# List 2 is longer than list 1
def test_zip_lists_list2_longer():
    list1 = LinkedList()
    list1.append(1)
    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    result = zip_lists(list1, list2)
    assert linked_list_to_list(result) == [1, 2, 4]
