"""
Graham's scan is a method of finding the convex hull of a finite set of points in the plane with time complexity O(n log n).
It is named after Ronald Graham, who published the original algorithm in 1972. The algorithm finds all vertices of the convex hull ordered along its boundary.
It uses a stack to detect and remove concavities in the boundary efficiently.
"""

import sys


def tangent(x: int, y: int) -> tuple:
    if x == a:
        return 1, y
    if x > a:
        return 0, (y - b) / (x - a), x
    if x < a:
        return 2, (y - b) / (x - a), x


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1)


n = int(sys.stdin.readline())

coord = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
coord.sort(key=lambda x: (x[1], x[0]))
a, b = coord.pop(0)
coord.sort(key=lambda x: tangent(*x))

stack = [(a, b), coord[0]]

for i in range(1, n - 1):
    while len(stack) >= 2:
        if ccw(*stack[-2], *stack[-1], *coord[i]) <= 0:
            stack.pop()
        else:
            break
    stack.append(coord[i])

if (len(stack) >= 3) and (ccw(*stack[-2], *stack[-1], *stack[0]) <= 0):
    stack.pop()