def quicksort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()
    item_greater=[]
    item_lower=[]
    for item in sequence:
        if item>pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)
    return quicksort(item_lower)+[pivot]+quicksort(item_greater)
print(quicksort([19,40,6,5,3,8,98,231]))