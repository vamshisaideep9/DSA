def remove_duplicates_from_sorted_array(arr):
    n = len(arr)
    arr = list(set(arr))
    return arr


print(remove_duplicates_from_sorted_array([1, 2, 2, 3, 4, 4, 5]))