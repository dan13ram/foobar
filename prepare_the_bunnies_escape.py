from collections import namedtuple
qnode = namedtuple("qnode", "x y z")
rowNum = [-1, 0, 0, 1];
colNum = [0, -1, 1, 0];

class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0,item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def isValid(x, y, row, col):
    return (x >= 0) and (x < row) and (y >= 0) and (y < col)

def BFS(mat, row, col):
    if (mat[0][0] != 0 or mat[row-1][col-1] != 0):
        return row * col
    visited = [[False for i in xrange(col)] for j in xrange(row)]
    q = Queue()
    q.put(qnode(0,0,1))
    while (not q.empty()):
        node = q.get()
        if node.x == row-1 and node.y == col-1:
            return node.z
        for i in range(4):
            x = node.x + rowNum[i]
            y = node.y + colNum[i]
            if (isValid(x, y, row, col) and mat[x][y] == 0 and not visited[x][y]):
                visited[x][y] = True
                q.put(qnode(x,y,node.z+1))
    return row * col

def answer(maze):
    row = len(maze)
    col = len(maze[0])
    answer = BFS(maze, row, col)
    for i in range(row):
        for j in range(col):
            if maze[i][j] == 1:
                maze[i][j] = 0
                temp = BFS(maze, row, col)
                if temp < answer:
                    answer = temp
                maze[i][j] = 1
    return answer


print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
print answer([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
