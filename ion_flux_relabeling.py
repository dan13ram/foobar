def answer(h, q):
    return [parent(a, h) for a in q]

def parent(a, h):
    if h <= 1 or a >= 2**h - 1:
        return -1
    if a == 1 or a == 2:
        return 3
    if a == 2**(h-1) - 1 or a == 2**(h) - 2:
        return 2**h - 1
    if a > 2**(h-1) - 1:
        return 2**(h-1) - 1 + parent(a - 2**(h-1) + 1, h-1)
    else:
        return parent(a, h-1)

assert( answer(3, [7, 3, 5, 1]) == [-1, 7, 6, 3] )
print "1"
assert( answer(5, [19, 14, 28]) == [21, 15, 29] )
print "2"
