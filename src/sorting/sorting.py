# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # number of elements
    elements = len(arrA) + len(arrB)
    # merged array contains a 0 in the array per element 5 elements = [0,0,0,0,0]
    merged_arr = [0] * elements
    # Your code here
    # set a to 0
    a = 0
    # set b to 0
    b = 0

    # for each item in merged array 
    for i in range(len(merged_arr)):
        # if a is >= length of Array A; only arrB remains
        if a >= len(arrA):
            # current item in merged array becomes current item in Array B
            merged_arr[i] = arrB[b]
            # Increment b by 1
            b += 1
        # if b is >= length of Array B; only arrA remains
        elif b >= len(arrB):
            # current item in merged array becomes current item in Array A
            merged_arr[i] = arrA[a]
            # Increment a by 1
            a += 1
        # if item in Array A at a, is < item in Array B at b
        elif arrA[a] < arrB[b]:
            # current item in merged array becomes current item in Array A
            merged_arr[i] = arrA[a]
            # Increment a by 1
            a += 1
        # otherwise
        else:
            # current item in merged array becomes current item in Array B
            merged_arr[i] = arrB[b]
            # Increment b by 1
            b += 1 

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    # base case
    # run as long as length of array > 1
    if len(arr) > 1:
        midpoint = len(arr) // 2 
        # split array into halves
        # store everything to left of midpoint
        left = arr[:midpoint]
        # store everything from midpoint to the right
        right = arr[midpoint:]
        # recursively call merge_sort() on LHS; repeat splitting arrays until each item is in its own array
        # recursively call merge_sort() on RHS; repeat splitting arrays until each item is in its own array
        # call on merge to combine 2 sorted arrays
        arr = merge(merge_sort(left), merge_sort(right))
        # keep merging until only 1 sorted array remains
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

