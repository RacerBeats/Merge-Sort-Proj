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
    i, j = 0 # i is for L_half, j is for R_half
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
    ''' sort a list using iterave merge sort'''
    #Base case: if list is empty or has only one element, it is already sorted
    if len(arr) <= 1:
        return arr
    
    #1: start with subarrays of size 1, since that's already sorted
    size = 1
    n = len(arr)

    #2: merge subarrays in increasing size. (1,2,4,8,etc...)
    while size < n:
        left = 0 #start of 1st subarray
        while left < n:
            #find midpoint and end of current subarrays
            mid = min(left + size, n) #end of 1st subarray
            right = min(left + 2*size, n) #end of 2nd subarray

            #3: merge the 2 subarrays
            if mid < right:
                merge(arr, left, mid, right)
            
            #move to next pair of subarrays
            left += right

        #double size for next iteration
        size *= 2
    return arr

    