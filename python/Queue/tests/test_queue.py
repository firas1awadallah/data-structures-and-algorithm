import pytest
from Queue.queue import Queue

def test_enqueue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.__str__() == "1 -> 2 -> 3 -> None"

def test_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    

def test_peek():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.peek() == 1
    

def test_is_empty():
    q = Queue()
    assert q.is_empty() == True
    q.enqueue(1)
    assert q.is_empty() == False
    q.enqueue(2)
    assert q.is_empty() == False
    q.enqueue(3)
    assert q.is_empty() == False
    q.dequeue()

def test_instance():
    q = Queue()
    assert isinstance(q, Queue)

def test_peek_or_decueue_Exeptions():
    q = Queue()
    with pytest.raises(Exception):
        q.peek()
    with pytest.raises(Exception):
        q.dequeue()