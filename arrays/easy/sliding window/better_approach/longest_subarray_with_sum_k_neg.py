def longest_subarray(arr, k):
    n = len(arr)
    l = 0
    sum = 0
    maxsum = 0
    for r in range(n):
        sum = sum + arr[r]

        if sum > k:
            sum = sum - arr[l]
            l += 1
        
        if sum <= k:
            maxsum = max(sum, r-l+1)
        
    r+=1
    return maxsum


print(longest_subarray([-1,1,1],1))
    

