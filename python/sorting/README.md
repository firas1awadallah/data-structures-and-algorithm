
## to Run  code : python python/sorting/insertion.py
## to Test code : pytest python/sorting/test_insertion.py

## Pseudocode
----------------------------------------------------------------
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted

----------------------------------------------------------------

##  Trace

### Sample Array:
[8, 4, 23, 42, 16, 15]

1. Initial state:
   - sorted = [8]
   - input = [8, 4, 23, 42, 16, 15]

2. Iteration 1:
   - Insert( [8], 4)
   - i = 0, len(sorted) = 1, value = 4
   - 4 > 8? No
   - Insert 4 at index 0: [4, 8]
   - sorted = [4, 8]

3. Iteration 2:
   - Insert( [4, 8], 23)
   - i = 0, len(sorted) = 2, value = 23
   - 23 > 4? Yes
   - Continue loop: i = 1
   - Insert 23 at index 1: [4, 23, 8]
   - sorted = [4, 8, 23]

4. Iteration 3:
   - Insert( [4, 8, 23], 42)
   - i = 0, len(sorted) = 3, value = 42
   - 42 > 4? Yes
   - Continue loop: i = 1
   - 42 > 23? Yes
   - Continue loop: i = 2
   - Insert 42 at index 2: [4, 8, 23, 42]
   - sorted = [4, 23, 42, 8]

5. Iteration 4:
   - Insert( [4, 8, 23, 42], 16)
   - i = 0, len(sorted) = 4, value = 16
   - 16 > 4? Yes
   - Continue loop: i = 1
   - 16 > 23? No
   - Insert 16 at index 1: [4, 16, 23, 42, 8]
   - sorted = [4, 8, 16, 23, 42]

6. Iteration 5:
   - Insert( [4, 8, 16, 23, 42], 15)
   - i = 0, len(sorted) = 5, value = 15
   - 15 > 4? Yes
   - Continue loop: i = 1
   - 15 > 16? No
   - Insert 15 at index 1: [4, 8, 15, 16, 23, 42]
   - sorted = [4, 8, 15, 16, 23, 42]

7. Final sorted array: [4, 8, 15, 16, 23, 42]

## Efficency
### Time: 
* The Insert function has a time complexity of O(n) 
* The InsertionSort function has a time complexity of O(n^2)
### Space:
* The Insert function has a space complexity of O(1)
* The InsertionSort function has a space complexity of O(n)