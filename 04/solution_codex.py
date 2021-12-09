"""
Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. If all numbers in any row or any column of a board are marked, that board wins. Diagonals don't count. Your puzzle input contains the numbers to draw and three boards separated by two line breaks:
"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space). After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners. Finally, 24 is drawn. At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

Figure out which board will win first. What will your final score be if you choose that board?
"""

import re


def main():
    with open("08/input.txt", "r") as f:
        lines = f.readlines()

    # parse input
    boards = []
    for i in range(0, len(lines), 3):
        board = []
        for j in range(3):
            board.append([int(x) for x in re.split("\D", lines[i + j + 1]) if x != ""])
        boards.append(board)

    # find the first winning board and calculate its score
    for i in range(len(boards)):
        board = boards[i]

        # check rows and columns for a winner
        for j in range(3):
            if all([x != 0 for x in board[j]]):
                print("Row {} won!".format(j))

            col = [board[x][j] for x in range(3)]
            if all([x != 0 for x in col]):
                print("Column {} won!".format(j))

        # check diagonals for a winner (only one diagonal can win)
        diag1 = [board[x][x] for x in range(3)]
        diag2 = [board[2 - x][x] for x in range(3)]

        if all([x != 0 for x in diag1]):
            print("Diagonal 1 won!")

        if all([x != 0 for x in diag2]):
            print("Diagonal 2 won!")

        # calculate score
        score = 0
        for j in range(3):
            for k in range(3):
                if board[j][k] != 0:
                    score += board[j][k]

        print("Score: {}".format(score))


if __name__ == "__main__":
    main()
