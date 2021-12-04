input = open("04/input.txt").read().split("\n\n")
draws = input[0].split(",")
boards = input[1:]

clean_boards = []
for board in boards:
    board = board.replace("\n ", "\n").replace("  ", " ").strip()
    board_arr = [a.split(" ") for a in board.split("\n")]
    clean_boards.append(board_arr)


def check_win(board):
    for row in board:  # check for row wins
        if all([char == "x" for char in row]):
            return True
    for col_ind in range(5):  # check for col wins
        col = [row[col_ind] for row in board]
        if all([char == "x" for char in col]):
            return True
    return False


def bingo_sim():
    winning_boards = []
    results = []
    for draw in draws:
        print(f"Drawing... {draw}")
        for i, board in enumerate(clean_boards):  # update boards
            for j, row in enumerate(board):
                for k, spot in enumerate(row):
                    if spot == draw:
                        clean_boards[i][j][k] = "x"

        for ind, board in enumerate(clean_boards):  # check for winners
            if check_win(board) and ind not in winning_boards:
                total = 0
                winning_boards.append(ind)
                for row in board:
                    for spot in row:
                        if spot != "x":
                            total += int(spot)
                print(f"Board {ind+1} won with draw {draw} and total {total}")
                results.append((ind, int(draw), total))
                if len(winning_boards) == len(clean_boards):
                    return results


result = bingo_sim()
print(result[0][1] * result[0][2])  # part one
print(result[-1][1] * result[-1][2])  # part two
