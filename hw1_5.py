"""
Write a function, binary_search, that takes as input an array and a value,
and produce a boolean as its output. The function should binary search the array,
looking for the value and returning true if found, and false otherwise.
"""

array = [2, 4, 6, 8, 10, 12, 14, 16]

# Write a function that searches an array for a particular value
def binary_search(array, value):

    # Check if array is empty
    if len(array) == 0:
        return False

    # Set pointers for low, high, and middle guess
    low = 0
    high = len(array)-1
    mid = (high - low) // 2

    # Change pointers for high, low, and mid based on comparison result
    while (high-low) > 0:
        if array[mid] == value:
            return True
        elif value < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
        mid = ((high - low) // 2) + low

    # When there is one element left, check to see if it is equal to the value
    if array[high] == value:
        return True
    else:
        return False

#Print Array and test numbers
print("Array", array)
print("0", binary_search(array, 0))
print("2", binary_search(array, 2))
print("7", binary_search(array, 7))
print("16", binary_search(array, 16))
print("20", binary_search(array, 20))
