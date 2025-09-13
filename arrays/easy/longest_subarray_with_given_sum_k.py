def longest_sub_array(arr, k):
    left = 0
    max_length = 0
    current_sum = 0
    best_subarray = []  # Store the actual subarray

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k:
            current_sum -= arr[left]
            left += 1
        
        if current_sum == k:
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                best_subarray = arr[left:right+1]  # Extract the subarray
    
    return best_subarray


print(longest_sub_array([2,3,5,1,8], k=10))

        
