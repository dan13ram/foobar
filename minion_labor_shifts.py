def answer(data, n):
    points = {}
    for a in data:
        if str(a) in points:
            points[str(a)] += 1
        else:
            points[str(a)] = 1
    answer = []
    for a in data:
        if points[str(a)] <= n:
            answer.append(a)
    print answer


answer([1,2,4,5,67,01], 2)
answer([1,2,4,5,67,01], 1)
answer([1, 2, 3], 0)
answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
answer([1, 2, 3], 6)

