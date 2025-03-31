# Ryan Cheung
# CS 031
# Prof Ashraf
# 3/30/2025
# Project 1: Week 2 Deliverable - Merge Sort in Python
# Group Members: Ryan Cheung, Francisco Ortega, and Dillan Desai

'''
This code implements the Merge Sort algorithm, whhich is a divide-and-conquer sorting algorithm.
It takes an input list of numbers and sorts them in ascending order using the Merge Sort algorithm.
The code defines three functions: merge, merge_sort, and main.
The merge function takes two sorted lists as input and merges them into a single sorted list.
The merge_sort function takes a list as input and recursively divides it into smaller sublists until each sublist contains only one element.
It then merges the sublists back together in sorted order using the merge function.
The main function prompts the user to enter a list of numbers and calls the merge_sort function to sort the list.
The sorted list is then printed to the console.

I will be using iteration instead of recursion for this particular implementation.
'''

def merge(arr, left, mid, right):
    ''' Merge 2 sorted sublists within orignal array'''
    #Temp arrays to hold 2 subarrays
    L_half = arr[left:mid]
    R_half = arr[mid:right]

    #pointers for L_half, R_half, and original array
    # i is for L_half, j is for R_half
    i = 0
    j = 0 
    k = left # k is for original array

    #merge 2 subarrays
    while i < len(L_half) and j < len(R_half):
        if L_half[i] <= R_half[j]:
            arr[k] = L_half[i]
            i += 1
        else:
            arr[k] = R_half[j]
            j += 1
        k += 1
    #add remaining elements from L_half and R_half
    while i < len(L_half):
        arr[k] = L_half[i]
        i += 1
        k += 1
    while j < len(R_half):
        arr[k] = R_half[j]
        j += 1
        k += 1

def merge_sort(arr):
    """Sort a list using the iterative merge sort algorithm."""
    # Base case: if list is empty or has only one element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Create a working copy of the array to avoid modifying the original
    # during intermediate steps
    working_arr = arr.copy()
    
    # Start with subarrays of size 1, since that's already sorted
    size = 1
    n = len(working_arr)
    
    # Merge subarrays in increasing size (1, 2, 4, 8, etc.)
    while size < n:
        # Process all pairs of adjacent subarrays of current size
        for left in range(0, n, 2*size):
            # Find midpoint and end of current subarrays
            mid = min(left + size, n)
            right = min(left + 2*size, n)
            
            # Merge the 2 subarrays if there are elements in both
            if mid < right:
                merge(working_arr, left, mid, right)
        
        # Double size for next iteration
        size *= 2
    
    # Copy the sorted result back to the original array
    for i in range(len(arr)):
        arr[i] = working_arr[i]
    
    return arr
    
''' TESTING MERGE SORT ON VARIOUS LISTS '''
if __name__ == "__main__":
    # Test case 1: Empty list
    arr1 = []
    print("Original list:", arr1)
    print("Sorted list:", merge_sort(arr1))
    print()

    # Test case 2: Single element list
    arr2 = [5]
    print("Original list:", arr2)
    print("Sorted list:", merge_sort(arr2))
    print()

    # Test case 3: Sorted list
    arr3 = [1, 2, 3, 4, 5]
    print("Original list:", arr3)
    print("Sorted list:", merge_sort(arr3))
    print()

    # Test case 4: Reverse sorted list
    arr4 = [5, 4, 3, 2, 1]
    print("Original list:", arr4)
    print("Sorted list:", merge_sort(arr4))
    print()

    # Test case 5: List with duplicate elements
    arr5 = [5, 2, 8, 2, 1]
    print("Original list:", arr5)
    print("Sorted list:", merge_sort(arr5))
    print()

    # Test case 6: List with negative numbers
    arr6 = [-5, 2, -8, 2, 1]
    print("Original list:", arr6)
    print("Sorted list:", merge_sort(arr6))
    print()

    # Test case 7: Basic unsorted list
    arr7 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Original list:", arr7)
    print("Sorted list:", merge_sort(arr7))
    print()

    # Test case 8: Uniform Elements
    arr8 = [5, 5, 5, 5, 5]
    print("Original list:", arr8)
    print("Sorted list:", merge_sort(arr8))
    print()

    # Test case 9: Almost sorted list
    arr9 = [1, 2, 3, 4, 6, 5]
    print("Original list:", arr9)
    print("Sorted list:", merge_sort(arr9))
    print()

    # Test case 10: Large random array, 50 random ints b/w 1 and 50
    import random
    arr10 = [random.randint(1, 50) for x in range(50)]
    print("Original list:", arr10)
    print("Sorted list:", merge_sort(arr10))
    print()
