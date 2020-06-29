def switch(array, left, right):
    if left >=right:
        return array

    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    return switch(array, left+1, right-1)
