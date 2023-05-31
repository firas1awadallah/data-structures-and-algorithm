import pytest
from stack_queue_animal_shelter import AnimalShelter

def test_enqueue():
    shelter = AnimalShelter()
    shelter.enqueue("dog", "Mossberg")
    shelter.enqueue("cat", "Mirabel")


    assert len(shelter.queue) == 2

def test_dequeue():
    shelter = AnimalShelter()
    shelter.enqueue("dog", "Mossberg")
    shelter.enqueue("cat", "Mirabel")
    shelter.enqueue("dog", "Max")
    shelter.enqueue("cat", "Fluffy")

    cat = shelter.dequeue("cat")
    dog = shelter.dequeue("dog")

    assert cat.name == "Mirabel"
    assert dog.name == "Mossberg"
    assert len(shelter.queue) == 2

def test_print_queue(capsys):
    shelter = AnimalShelter()
    shelter.enqueue("dog", "Mossberg")
    shelter.enqueue("cat", "Mirabel")
    shelter.enqueue("dog", "Max")
    shelter.enqueue("cat", "Fluffy")

    shelter.print_queue()

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert output == "dog, Mossberg\ncat, Mirabel\ndog, Max\ncat, Fluffy"

def test_invalid_pref():
    shelter = AnimalShelter()
    shelter.enqueue("dog", "Buddy")
    shelter.enqueue("cat", "Whiskers")

    invalid_pref = shelter.dequeue("bird")

    assert invalid_pref is None

if __name__ == "__main__":
    pytest.main()
