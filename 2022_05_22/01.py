def array_diff(a, b):
    for num in a[::-1]:
        if num in b: del a[a.index(num)]
    return a
