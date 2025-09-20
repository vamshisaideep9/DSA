def generate_all_subarr(arr):
    n = len(arr)
    subarrays = []

    for i in range(n):
        for j in range(i, n):
            subarrays.append(arr[i:j+1])
    
            

    return subarrays


print(generate_all_subarr([1,2,3,4,5]))