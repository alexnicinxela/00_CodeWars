'''Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.'''

def array_diff(a, b):
    for num in a[::-1]:
        if num in b: del a[a.index(num)]
    return a
