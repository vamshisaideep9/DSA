def left_rotate_an_array_by_one_place(arr):
    n = len(arr)

    if n == 1:
        return arr[0]

    
    rotated_arr = []

    for i in range(1, n):
        rotated_arr.append(arr[i])

    rotated_arr.append(arr[0])


    return rotated_arr


print(left_rotate_an_array_by_one_place([1,2,3,4,5]))

    