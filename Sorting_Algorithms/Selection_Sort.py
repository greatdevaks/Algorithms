# Program to implement the Selection Sort Algorithm.

# Worst-Case Complexity of Selection Sort is O(n^2).

# Function to implement the Selection Sort Algorithm:
def selection_sort(arr):
    size_arr = len(arr)
    # Traverse the whole array.
    for i in range(size_arr):
        min_val_index = i
        # Loop in the remaining array.
        for j in range(i + 1, size_arr):
            if arr[min_val_index] > arr[j]:
                min_val_index = j
        # Swap the current index element with the minimum value index element.
        arr[i], arr[min_val_index] = arr[min_val_index], arr[i]

# Driver program to test the selection_sort function.
arr = [12, 11, 13, 5, 6]
selection_sort(arr)
print("Sorted array is:", arr )