import pytest
from insertion import InsertionSort


def test_insertion_sort():
    
    input1 = [4, 2, 7, 1]
    expected1 = [1, 2, 4, 7]
    assert InsertionSort(input1) == expected1


    input2 = [9, 5, 8, 3, 6]
    expected2 = [3, 5, 6, 8, 9]
    assert InsertionSort(input2) == expected2

    input3 = [1]
    expected3 = [1]
    assert InsertionSort(input3) == expected3


    input4 = []
    expected4 = []
    assert InsertionSort(input4) == expected4


    input5 = [10, 5, 3, 8, 2]
    expected5 = [2, 3, 5, 8, 10]
    assert InsertionSort(input5) == expected5


    input6 = [1, 1, 1, 1]
    expected6 = [1, 1, 1, 1]
    assert InsertionSort(input6) == expected6


    input7 = [5, 4, 3, 2, 1]
    expected7 = [1, 2, 3, 4, 5]
    assert InsertionSort(input7) == expected7


    input8 = [1, 2, 3, 4, 5]
    expected8 = [1, 2, 3, 4, 5]
    assert InsertionSort(input8) == expected8

  
    input9 = [7, 7, 7, 7, 7]
    expected9 = [7, 7, 7, 7, 7]
    assert InsertionSort(input9) == expected9

    input10 = [8,4,23,42,16,15]
    expected10 = [4, 8, 15, 16, 23, 42]
    assert InsertionSort(input10) == expected10

