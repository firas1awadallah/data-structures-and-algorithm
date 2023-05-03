arr = [1, 2, 3, 4, 5, 6]
def reverseArray(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr
reversed_arr = reverseArray(arr)
print(reversed_arr)