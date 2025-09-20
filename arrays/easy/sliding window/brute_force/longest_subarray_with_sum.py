"""
Longest subarray with sum <= k: Brute Force approach
"""

def longest_subarray(arr, k):
    n = len(arr)
    sub = []
    max_length = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum = sum + arr[j]
            if sum <= k:
                max_length = max(max_length, j-i+1)
    return max_length  

print(longest_subarray([1,2,3,4,5], 7))
