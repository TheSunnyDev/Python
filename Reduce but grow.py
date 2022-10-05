# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

Solution:
def grow(arr):
    product = 1
    for number in arr:
        product = product * number 
    return product