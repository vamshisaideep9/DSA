def linear_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


print(linear_search([1,2,3,4,5,6], 9))
