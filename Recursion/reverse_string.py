def switch(array, left, right):
    if left >=right:
        return array

    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    return switch(array, left+1, right-1)

def splice_reverse(str, output = ""):
    output = output + str[-1]
    str = str[:-1]

    if len(str) == 0:
        return output
    else:
        return splice_reverse(str, output)