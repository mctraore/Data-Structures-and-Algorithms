def binary_search(input_array, value):
    left = 0
    right = len(input_array)-1
    mid = len(input_array) //2
    while left <= right:
        if input_array[mid] > value:
            right = mid-1
            mid = (left+right) // 2
        elif input_array[mid] < value:
            left = mid+1
            mid = (left + right) // 2
        else:
            return mid
    return -1