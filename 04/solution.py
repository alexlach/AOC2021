input = open("04/input.txt").read().split("\n\n")
draws = input[0]
boards = input[1:]


def print_board(board):
    for row in board:
        print(row)


clean_boards = []
for board in boards:
    board = board.replace("\n ", "\n").replace(" \n", "\n").replace("  ", " ").strip()
    board_arr = board.split("\n")
    board_arr = [a.split(" ") for a in board_arr]
    clean_boards.append(board_arr)


testWinR = [
    ["1", "2", "3", "4", "5"],
    ["x", "x", "x", "x", "x"],
    ["6", "7", "8", "x", "9"],
    ["x", "x", "10", "11", "x"],
    ["12", "x", "13", "x", "14"],
]
testWinC = [
    ["1", "2", "3", "x", "5"],
    ["x", "x", "x", "x", "4"],
    ["6", "7", "8", "x", "9"],
    ["x", "x", "10", "x", "x"],
    ["12", "x", "13", "x", "14"],
]


def board_wins(board):
    # check for row wins
    for row in board:
        sols = set(row)
        if len(sols) == 1 and "x" in sols:
            return True

    # check for col wins
    for col_ind in range(0, 5):
        sols = []
        for row in board:
            sols.append(row[col_ind])
        sols = set(sols)
        if len(sols) == 1 and "x" in sols:
            return True
    return False


draws = draws.split(",")


def conduct_drawing():
    total = 0
    counter = 0
    for draw in draws:
        print(f"removing draw: {draw}")
        # update boards
        for i, board in enumerate(clean_boards):
            for j, row in enumerate(board):
                for k, spot in enumerate(row):
                    if spot == draw:
                        clean_boards[i][j][k] = "x"

        # check for winners
        for ind, board in enumerate(clean_boards):
            if board_wins(board):
                for row in board:
                    for spot in row:
                        if spot != "x":
                            total += int(spot)
                print(f"found a winner {ind}")
                return draw, total


result = conduct_drawing()
print(result)
print(result[0] * result[1])
