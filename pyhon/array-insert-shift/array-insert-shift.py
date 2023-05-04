
arr = [42,8,15,23,42]
val = 16

def insertShiftArray(arr, val):
    n = len(arr)
    mid = (n + 1) // 2

    arr.append(None)
    for i in range(n-1, mid-1, -1):
        arr[i+1] = arr[i]

    arr[mid] = val
    return arr

new_arr = insertShiftArray(arr, val)
print(new_arr)


# python pyhon/array-insert-shift/array-insert-shift.py