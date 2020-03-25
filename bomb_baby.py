def answer(m,f):
    m = int(m)
    f = int(f)
    if(m<f):
        return answer(f,m)
    if f == 1:
        return m - 1
    r = m % f
    if r == 0:
        return "impossible"
    v = answer(f,r)
    if v == "impossible":
        return "impossible"
    return v + m/f


print answer(1,2)
print answer(1,4)
print answer(7,4)
print answer(7,14)
print answer(2,14)
print answer(5,25)
print answer(6,8)
print answer(18,20)
print answer(26,39)
