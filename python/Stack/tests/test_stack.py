import pytest
from stack.stack import stack

def test_push_stack():
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.top.value == 3

def test_pop_stack():
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1

def test_empty():
    s = stack()
    assert s.is_empty() == True
    s.push(1)
    assert s.is_empty() == False

def test_peek():
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.peek() == 3

def test_instance():
    s = stack()
    assert isinstance(s, stack)

def test_peek_or_pop_Exeption():
    s = stack()
    with pytest.raises(Exception):
        s.peek_or_pop()




