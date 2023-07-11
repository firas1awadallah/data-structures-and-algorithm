def Insert(sorted, value):
    i = 0
    while i < len(sorted) and value > sorted[i]:
        i = i + 1
    sorted.insert(i, value)


def InsertionSort(input):
    if len(input) == 0:
        return []
    
    sorted = [input[0]]
    for i in range(1, len(input)):
        Insert(sorted, input[i])
    return sorted




