#!/usr/bin/env python

theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    }

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def ticTacToe():
    turn = "X"

    for i in range(9):
        printBoard(theBoard)
        move = input("Turn for %s. Move on which space?" % (turn))
        theBoard[move] = turn
        if turn == "X":
            turn = "O"
        else:
            turn = "X"



if __name__ == '__main__':
    ticTacToe()
