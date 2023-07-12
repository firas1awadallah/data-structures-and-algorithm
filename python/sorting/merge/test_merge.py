import pytest

from merge import merge_sort

def test_merge_sort():
    arr = [5, 2, 9, 1, 7, 6]
    merge_sort(arr)
    assert arr == [1, 2, 5, 6, 7, 9]

def test_merge_sort_empty():
    arr = []
    merge_sort(arr)
    assert arr == []

def test_merge_sort_single_element():
    arr = [42]
    merge_sort(arr)
    assert arr == [42]

def test_merge_sort_duplicates():
    arr = [3, 1, 2, 1, 4, 4, 3, 2]
    merge_sort(arr)
    assert arr == [1, 1, 2, 2, 3, 3, 4, 4]
