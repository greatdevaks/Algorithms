# Program to implement the Bubble Sort Algorithm.

# Worst-Case Complexity of Bubble Sort is O(n^2).

# Function to implement the Bubble Sort Algorithm:
def bubble_sort(arr):
    size_arr = len(arr)
    # Traverse the whole array.
    for i in range(size_arr):
        for j in range(0, size_arr - i - 1):
            # Note that last i elements are already in place.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver program to test the bubble_sort function.
arr = [12, 11, 13, 5, 6]
bubble_sort(arr)
print("Sorted array is:", arr )