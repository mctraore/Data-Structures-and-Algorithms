

def switch(array, left, right):
    if left >=right:
        return array

    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    return switch(array, left+1, right-1)



char_array = ["h", "e", "l", "l", "o"]

print (switch(char_array, 0, len(char_array)-1))