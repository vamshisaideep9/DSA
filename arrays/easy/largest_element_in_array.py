class LargestElementInArray:
    def __init__(self, arr):
        self.arr = arr

    def find_largest_element(self):
        max = 0
        for i in range(len(self.arr)):
            if self.arr[i] > max:
                max = self.arr[i]
        return max

if __name__ == "__main__":
    arr = [1, 2, 5, 4, 3]
    largest_element = LargestElementInArray(arr)
    print(largest_element.find_largest_element())
