def numbers_that_appear_onetime(arr):
    n = len(arr)
    maxi = max(arr)
    hash = [0]*(maxi+1)
    for num in arr:
        hash[num] += 1

    print(hash)
    
    for num in arr:
        if hash[num] == 1:
            return num

    
    return -1


print(numbers_that_appear_onetime([4, 1, 2, 1, 2]))