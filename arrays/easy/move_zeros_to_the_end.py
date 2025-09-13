# 1, 0 , 3, 0, 2, 1, 4, 0

# output: 1,3,2,1,4,0,0,0

def move_zeros_to_the_end(arr):
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    
    for i in range(non_zero_index, len(arr)):
        arr[i] = 0
    
    return arr


print(move_zeros_to_the_end([1,0,3,0,2,1,4,0]))


    

