def find_missing_number(arr, n):
    sum1=0
    sum2 = int(n*(n+1)/2)
    for i in range(len(arr)):
        sum1 = sum1 + arr[i]
    return sum2 - sum1


print(find_missing_number([1,3,4,5],5))