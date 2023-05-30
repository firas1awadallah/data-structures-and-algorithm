import pytest
from stack_queue_pseudo import PseudoQueue

@pytest.fixture
def queue():
    return PseudoQueue()

def test_enqueue_single_item(queue, capfd):
    queue.enqueue(1)
    queue.print_stack1()
    out, _ = capfd.readouterr()
    assert out.strip() == "Stack1: 1"

def test_enqueue_multiple_items(queue, capfd):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_stack1()
    out, _ = capfd.readouterr()
    assert out.strip() == "Stack1: 3->2->1"

def test_dequeue_single_item(queue, capfd):
    queue.enqueue(1)
    queue.dequeue()
    queue.print_stack1()
    out, _ = capfd.readouterr()
    assert out.strip() == "Stack1:"

def test_dequeue_multiple_items(queue, capfd):
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.print_stack1()
    out, _ = capfd.readouterr()
    assert out.strip() == "Stack1: 3"


def test_enqueue_empty(queue, capfd):
    queue.enqueue(1)
    queue.print_stack1()
    out, _ = capfd.readouterr()
    assert out.strip() == "Stack1: 1"

def test_dequeue_empty(queue):
    with pytest.raises(IndexError):
        queue.dequeue()
