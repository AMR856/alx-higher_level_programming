#!/usr/bin/python3
"""A code to solve the problem of n queens"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    myNum = int(sys.argv[1])
except Exception as Everything:
    print("N must be a number")
    sys.exit(1)

if myNum < 4:
    print("N must be at least 4")
    sys.exit(1)


def solevNQueens():
    col = set()
    posDig = set()
    negDig = set()

    res = []

    board = [["."] * myNum for i in range(myNum)]
    counter = 0
    backtrack(0, col, posDig, negDig, board, res)
    newRes = [[]]
    for i in range(len(res)):
        for j in range(len(res[0])):
            for k in range(len(res[i][j])):
                if res[i][j][k] == 'Q':
                    newRes[counter].append(j)
                    newRes[counter].append(k)
                    counter = counter + 1
                    if (j != len(res[0]) - 1):
                        newRes.append([])
        print(newRes)
        newRes.clear()
        newRes = [[]]
        counter = 0


def backtrack(r, col, posDig, negDig, board, res):
    if r == myNum:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return

    for c in range(myNum):
        if c in col or (c + r) in posDig or (r - c) in negDig:
            continue

        col.add(c)
        posDig.add(r + c)
        negDig.add(r - c)
        board[r][c] = 'Q'

        backtrack(r + 1, col, posDig, negDig, board, res)

        col.remove(c)
        posDig.remove(r + c)
        negDig.remove(r - c)
        board[r][c] = '.'


solevNQueens()
