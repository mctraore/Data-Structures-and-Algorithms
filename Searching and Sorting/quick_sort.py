def quicksort(array):
    if len(array) <= 1:
        return array
    left_array = []
    right_array = []
    
    pivot = array.pop()
    for num in array:
        if num <= pivot:
            left_array.append(num)
        else:
            right_array.append(num)
    
    return quicksort(left_array) + [pivot] + quicksort(right_array)
    
        


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)