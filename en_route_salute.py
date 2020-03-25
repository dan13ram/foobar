def answer(hall):
    numMore = 0
    lastLess = 0
    answer = 0
    for i, c in enumerate(hall):
        if c == ">":
            numMore += 1
        elif c == "<":
            answer += numMore
        elif c == "-":
            pass
        else:
            print "invalid input"
    return answer * 2


print answer("--->-><-><-->-")
print answer(">----<")
print answer("<<>><")
