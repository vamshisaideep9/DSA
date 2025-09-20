"""
Longest subarray with sum <= k
"""

def longest_subarray(arr, k):
    n = len(arr)

    l=0
    r=0
    sum = 0
    maxlen = 0

    while(r<n):
        sum = sum + arr[r]
        if(sum > k):
            sum = sum - arr[l]
            l = l + 1
        if sum <= k:
            maxlen = max(maxlen, r-l+1)
        r+=1
    return maxlen 


print(longest_subarray([-1,1,1],1))