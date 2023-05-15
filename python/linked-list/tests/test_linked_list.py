from linked_list.linked_list import LinkedList


def test_instantiate_empty_linked_list():
    linked_list = LinkedList()
    assert linked_list.head is None

def test_insert_into_linked_list():
    linked_list = LinkedList()
    linked_list.insert("a")
    assert linked_list.head.value == "a"

def test_head_property_points_to_first_node():
    linked_list = LinkedList()
    linked_list.insert("a")
    linked_list.insert("b")
    linked_list.insert("c")
    assert linked_list.head.value == "c"

def test_insert_multiple_nodes_into_linked_list():
    linked_list = LinkedList()
    linked_list.insert("a")
    linked_list.insert("b")
    linked_list.insert("c")
    assert linked_list.to_string() == "{ c } -> { b } -> { a } -> None"

def test_value_exists_in_linked_list():
    linked_list = LinkedList()
    linked_list.insert("a")
    linked_list.insert("b")
    linked_list.insert("c")
    assert linked_list.includes("b") is True

def test_value_does_not_exist_in_linked_list():
    linked_list = LinkedList()
    linked_list.insert("a")
    linked_list.insert("b")
    linked_list.insert("c")
    assert linked_list.includes("d") is False

def test_return_collection_of_values_in_linked_list():
    linked_list = LinkedList()
    linked_list.insert("a")
    linked_list.insert("b")
    linked_list.insert("c")
    assert linked_list.to_string() == "{ c } -> { b } -> { a } -> None"
##################
def test_append_to_end():
    my_list = LinkedList()
    my_list.append(2)

    assert my_list.head.value == 2
    assert my_list.head.next is None

    my_list.append(5)

    assert my_list.head.next.value == 5
    assert my_list.head.next.next is None

def test_append_multiple_nodes():
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(5)
    my_list.append(8)

    assert my_list.head.value == 2
    assert my_list.head.next.value == 5
    assert my_list.head.next.next.value == 8
    assert my_list.head.next.next.next is None

def test_insert_before_middle_node():
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(3)
    my_list.append(4)
    my_list.insert_before(3, 2)

    assert my_list.head.value == 1
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.next.next.value == 4
    assert my_list.head.next.next.next.next is None

def test_insert_before_first_node():
    my_list = LinkedList()
    my_list.append(2)
    my_list.append(3)
    my_list.insert_before(2, 1)

    assert my_list.head.value == 1
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.next.next is None

def test_insert_after_middle_node():
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(4)
    my_list.insert_after(2, 3)

    assert my_list.head.value == 1
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.next.next.value == 4
    assert my_list.head.next.next.next.next is None

def test_insert_after_last_node():
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.insert_after(2, 3)

    assert my_list.head.value == 1
    assert my_list.head.next.value == 2
    assert my_list.head.next.next.value == 3
    assert my_list.head.next.next.next is None














