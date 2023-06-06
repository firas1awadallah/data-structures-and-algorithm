import pytest
from stack_queue_brackets import validate_brackets


def test_validate_brackets():
    output = validate_brackets("{}(){}")
    
    assert output ==  True



def test_validate_brackets2():
    output = validate_brackets("{}{Code}[Fellows](())")
    
    assert output ==  True


def test_validate_brackets3():
    output = validate_brackets("{(})")
   
    assert output ==  False

def test_validate_brackets4():
    output = validate_brackets("[{[(]")
   
    assert output ==  False
