def left_rotate_array_by_k_places(arr, k):
    n = len(arr)
    rotated_arr = []

    for i in range(n-k, n):
        rotated_arr.append(arr[i])
    rotated_arr.extend(arr[:n-k])
    return list(rotated_arr)



print(left_rotate_array_by_k_places([1,2,3,4,5,6,7,8], 4))


