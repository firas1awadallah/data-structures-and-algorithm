
## to Run  code : python python/sorting/merge/merge.py
## to Test code : pytest python/sorting/merge/test_merge.py

## Pseudocode
----------------------------------------------------------------
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
----------------------------------------------------------------

##  Trace

### Sample Array:
[8,4,23,42,16,15]


1. Initial function : `merge_sort()`
   - The length >  1
   - middle index: `mid = 6 // 2 = 3`.
   - Split the array :
     - `left = [8, 4, 23]`
     - `right = [42, 16, 15]`
   - Recursive left : `merge_sort([8, 4, 23])`.

2. Recursive left : `merge_sort([8, 4, 23])`
   - The length > 1,  continue.
   - middle index: `mid = 3 // 2 = 1`.
   - Split 
     - `left = [8]`
     - `right = [4, 23]`
   - Recursive left : `merge_sort([8])`.

3. Recursive left : `merge_sort([8])`
   - The length 1,  no sort.
   - Return .

4. previous call: `merge_sort([8, 4, 23])`
   - right : `merge_sort([4, 23])`.

5. Recursive right : `merge_sort([4, 23])`
   - The length > 1.
   - middle index: `mid = 2 // 2 = 1`.
   - Split :
     - `left = [4]`
     - `right = [23]`
   - Recursive left : `merge_sort([4])`.

6. Recursive left : `merge_sort([4])`
   - The length = 1 .
   - Return .

7. call: `merge_sort([4, 23])`
   - Merge  right : `merge([4], [23], [4, 23])`.
   - array is sorted: `[4, 23]`.

8.  call: `merge_sort([8, 4, 23, 42, 16, 15])`
   - right : `merge_sort([42, 16, 15])`.

9. Recursive right : `merge_sort([42, 16, 15])`
   - The length > 1, continue.
   -  middle index: `mid = 3 // 2 = 1`.
   - Split the array :
     - `left = [42]`
     - `right = [16, 15]`
   - Recursive left : `merge_sort([42])`.

10. Recursive  left : `merge_sort([42])`
    - length = 1, .
    - Return .

11. call: `merge_sort([42, 16, 15])`
    - right : `merge_sort([16, 15])`.

12. Recursive right : `merge_sort([16, 15])`
    - The length > 1.
    - middle index: `mid = 2 // 2 = 1`.
    - Split  two halves:
      - `left = [16]`
      - `right = [15]`
    - Recursive left : `merge_sort([16])`.

13. Recursive left : `merge_sort([16])`
    - length = 1.
    - Return .

14.  call: `merge_sort([16, 15])`
    - Merge  left and right : `merge([16], [15], [16, 15])`.
    - ascending order: `[15, 16]`.

15. initial call: `merge_sort([8, 4, 23, 42, 16, 15])`
    - Merge right : `merge([8, 4, 23], [15, 16], [8, 4, 23, 15, 16])`.
    - Merge sorted array: `[4, 8, 15, 16, 23, 42]`.

* input  `[8, 4, 23, 42, 16, 15]` is sorted .

## Efficency

### Time: 
* function has a time complexity of O(n log n)
### Space:
* function has a space complexity of O(n)