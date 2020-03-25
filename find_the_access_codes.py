def answer(l):
    d = {(i,j):0 for i,j in enumerate(l)}
    count = 0
    for i, j in enumerate(l):
        for m, n in enumerate(l[:i]):
            if j % n == 0:
                d[(i,j)] += 1
                count += d[(m,n)]
    return count


print answer([1,2,3,4,5,6,8])
print answer([1,1,1])
print answer([1,2,3,4,5,6])
