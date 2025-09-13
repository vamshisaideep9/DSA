def max_consecutive_ones(arr):
    count = 0
    max_count = 0
    n = len(arr)

    for i in range(n):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        
        max_count = max(count, max_count)
    
    return max_count

print(max_consecutive_ones([1, 0, 1, 1, 1, 0, 1, 1, 1, 1]))