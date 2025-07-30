# 1. Linear Search
# Description: Linear search checks each element in the array one by one until it finds the target or reaches the end of the array. It works for both sorted and unsorted arrays.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Index found
    return -1  # Not found

# 2. Binary Search
# Description: Binary search works only for sorted arrays. It repeatedly divides the array in half, comparing the middle element to the target. Depending on the comparison, it searches in the left or right half.
 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Index found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  

# 3. Using Built-in Functions (Python Example)
# Description: Languages like Python offer built-in functions like .index() or high-level functions that return the location of an element.

def builtin_search(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1 

""" Which is Best and Why?
Binary search is the best for large, sorted arrays due to its logarithmic time complexity, making it far more efficient than linear search as the size of the dataset increases.
Linear search or built-in methods are preferable for small or unsorted arrays, or when convenience and code simplicity are priorities.
Use the built-in function for rapid prototyping or when maximum code clarity is desired."""

