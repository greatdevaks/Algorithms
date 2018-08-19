# Program to implement the Insertion Sort Algorithm.

# Worst-Case Complexity of Insertion Sort is O(n^2).

# Function to do the Insertion Sort:
def insertion_sort(arr):
    # Traverse the array through 1 to len(arr):
    for i in range(1, len(arr)):
        value = arr[i]

        # Variable 'j' stores the index of the previous element.
        j = i - 1
        # Run while loop until j >= 0 and until the current value is less than the value at previous index.
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Assign the value to the correct place in array.
        arr[j + 1] = value

# Driver program to test the insertion_sort function.
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array is:", arr )

