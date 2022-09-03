def findMaxNumber(arr, end_index):
    max_index = 0
    for i in range(0,end_index):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

def reverseArray(arr, end_index):
    start = 0
    while start < end_index:
        temp = arr[start]
        arr[start] = arr[end_index]
        arr[end_index] = temp
        start += 1
        end_index -= 1

def pancakeSort(arr):
    arr_length = len(arr)
    arr_size = arr_length
    while arr_size > 1:

        # Finding the index of current maximum number
        max_index = findMaxNumber(arr, arr_size)
        if max_index != arr_size - 1:
            # Moving the max number to the beginning 
            reverseArray(arr, max_index)
  
            # Moving the max number to the end
            reverseArray(arr, arr_size - 1)
        arr_size -= 1

arr = [100, 6, 1, 52, 600]
pancakeSort(arr)