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
    assert linked_list.to_string() == "{ c } -> { b } -> { a } -> NULL"

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
    assert linked_list.to_string() == "{ c } -> { b } -> { a } -> NULL"












