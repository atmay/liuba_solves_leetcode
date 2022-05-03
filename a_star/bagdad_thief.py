"""
https://stepik.org/lesson/637770/step/7?unit=634236

Sample Input 1:
3
230
001
012
Sample Output 1:
Impossible

Sample Input 2:
4
1112
1001
1101
0111
Sample Output 2:
#---
#---
##--
-###

Sample Input 3:
7
1234567
3010001
5022901
7023201
9022201
7000101
5311111
Sample Output 3:
###----
--#----
--#----
--#----
--###--
----#--
----###
"""
from queue import Queue

sample = [
    (3,
     [[2, 3, 0],
      [0, 0, 1],
      [0, 1, 2]]),
    (4,
     [[1, 1, 1, 2],
      [1, 0, 0, 1],
      [1, 1, 0, 1],
      [0, 1, 1, 1]]
     ),
    (
        7,
        [[1, 2, 3, 4, 5, 6, 7],
         [3, 0, 1, 0, 0, 0, 1],
         [5, 0, 2, 2, 9, 0, 1],
         [7, 0, 2, 3, 2, 0, 1],
         [9, 0, 2, 2, 2, 0, 1],
         [7, 0, 0, 0, 1, 0, 1],
         [5, 3, 1, 1, 1, 1, 1]]
    )
]


def a_star(world: list, size: int) -> list:
    size -= 1
    que = Queue()
    que.put((0, 0, world[0][0], None))
    paths = []

    while not que.empty():
        cur = que.get()
        if cur[2] == 0:
            continue
        if cur[0] == size and cur[1] == size:
            paths.append(cur)
            continue
        x, y = cur[0] + 1, cur[1]
        if x <= size:
            que.put((x, y, world[x][y], cur))

        x, y = cur[0], cur[1] + 1
        if y <= size:
            que.put((x, y, world[x][y], cur))
    return paths


def get_sum_weight(path: tuple) -> int:
    # (3, 3, 1, (3, 2, 1, (3, 1, 1, (2, 1, 1, (2, 0, 1, (1, 0, 1, (0, 0, 1, None)))))))
    weight = 0
    while path:
        weight += path[2]
        path = path[3]
    return weight


def draw_path(path: tuple, size: int) -> None:
    matrix = [['-' for _ in range(size)] for _ in range(size)]
    while path:
        matrix[path[0]][path[1]] = '#'
        path = path[3]
    for row in matrix:
        print(''.join(row))


if __name__ == '__main__':
    size, world = sample[0]
    paths = a_star(world, size)
    paths.sort(key=get_sum_weight)
    print(paths)
    if not paths:
        print('Impossible')
    for path in paths:
        draw_path(path, size)
        print()
