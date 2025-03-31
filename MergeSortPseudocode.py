# This is the pseudocode for the MergeSort algorithm.

def merge_sort(arr):
    # 1: Start with subarrays of size 1, since that's already sorted
    size  = 1
    n = len(arr)

    # 2: Merge subarrays in increasing size. (1,2,4,8,etc...)
    while size <  n:
        left = 0 #start of 1st subarray
        while left < n:
	# find midpoint and end of current subarrays
	mid = end of 1st subarray
	right = end of 2nd subarray

	#3: merge the 2 subarrays
	merge(arr, left, mid, right)
	
	move to next pair of subarrs
     double size for next iteration
    return arr

def merge(arr, left, mid, right):
    # Temporary arrays to hold 2 subarrs
    L_half = arr[left:mid]
    R_half = arr[mid:right]

    i = j = ptrs for L & R half
    k = ptr for original array

    #3a: merge 2 subarrs
    while i < len(L_half) and j < len(R_half):
        if left_half[i] < right_half[j]: 
	       place in original array
	       move L pointer
        else: #if right element is smaller or equal
	        arr[k] = R_half[j]
	        move R pointer
    #3b: add remaining elements from L and R half
    while i < len(L_half):
        arr[k] = L_half[i]
        i += 1
        k += 1
    while j < len(R_half):
        arr[k] = R_half[j]
        j += 1
        k += 1