# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    # start = left
    # end = right

    # base case
    # run until end is < start
    if end >= start:
        midpoint = (start + end) // 2

        # check if midpoint = target
        if arr[midpoint] == target:
            return midpoint

        # check if midpoint value > target
        if arr[midpoint] > target:
        # recursive case
            # if true right is updated to whatever was to the left of midpoint
            # rerun function
            return binary_search(arr, target, start, midpoint -1)
        # check if midpoint value < target
        else:
        # recursive case
            # if true left is updated to whatever was to the right of midpoint
            # rerun function
            return binary_search(arr, target, midpoint + 1, end)
    else:
        return -1

    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
