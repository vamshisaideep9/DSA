def second_largest_element(arr):
    n = len(arr)
    if n < 2:
        return -1
    
    large = float('-inf')
    second_large = float('-inf')

    for i in range(n):
        if arr[i] > large:
            second_large = large
            print(second_large)
            large = arr[i]
            print(large)
        elif arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
            print(second_large)
    return second_large

print(second_largest_element([1, 2, 5, 4, 3]))







