
def moves(pos):
    # pos - dict
    return []


def make_move(pos, move):
    for row in range(6):
        if pos["board"][-1 - row][move] == " ":
            pos["board"][-1 - row][move] = pos["flag"]
            return pos, (move, 5 - row)


def simulate(pos, move, my_side):
    return ""


def dump_pos(pos):
    # prindi info seisu kohta
    for row in pos["board"]:
        for i in range(7):
            if i == 0:
                print("|" + row[i], end="")
            elif i == 6:
                print(row[i] + "|", end="\n")
            else:
                print(row[i], end="")
    print("|0123456|")


def parse_move(move_str):
    validate = ("0", "1", "2", "3", "4", "5", "6")
    # tõlgi kasutaja tekst oma sisemisse käiguformaati
    if move_str in validate:
        move = int(move_str)
        return move
    else:
        move_str = input("Wrong symbol! Your move: ")
        return parse_move(move_str)


def is_over(pos, last_move):
    flag = pos["flag"]
    board = pos["board"]
    over = False
    check_down = False
    check_x_left = False
    check_x_right = False
    check_x_right_dio = False
    check_x_left_dio = False
    if last_move[1] <= 2 and not (check_down or check_x_left or check_x_right or check_x_left_dio or check_x_right_dio):
        for y in range(last_move[1], last_move[1] + 4):
            if board[y][last_move[0]] == flag:
                check_down = True
            else:
                check_down = False
                break
    if last_move[0] >= 3 and not (check_down or check_x_left or check_x_right or check_x_left_dio or check_x_right_dio):
        for x_left in range(last_move[0] - 3, last_move[0] + 1):
            if board[last_move[1]][x_left] == flag:
                check_x_left = True
            else:
                check_x_left = False
                break
    if last_move[0] <= 3 and not (check_down or check_x_left or check_x_right or check_x_left_dio or check_x_right_dio):
        for x_right in range(last_move[0], last_move[0] + 4):
            if board[last_move[1]][x_right] == flag:
                check_x_right = True
            else:
                check_x_right = False
                break
    if last_move[1] <= 2 and last_move[0] <= 3 and not (check_down or check_x_left or check_x_right or check_x_left_dio or check_x_right_dio):
        x = last_move[0]
        for y in range(last_move[1], last_move[1] + 4):
            if board[y][x] == flag:
                check_x_right_dio = True
                x += 1
            else:
                check_x_right_dio = False
                break
    if last_move[1] <= 2 and last_move[0] >= 3 and not (check_down or check_x_left or check_x_right or check_x_left_dio or check_x_right_dio):
        x = last_move[0]
        for y in range(last_move[1], last_move[1] + 4):
            if board[y][x] == flag:
                check_x_left_dio = True
                x -= 1
            else:
                check_x_left_dio = False
                break
    if check_down or check_x_left or check_x_right or check_x_left_dio or check_x_right_dio:
        over = True
    return over


def pure_mc(pos, N=200):
    # kõik käigud algseisus
    my_side = pos["flag"]
    initial_moves = moves(pos)
    # loendurid iga käigu jaoks
    win_counts = dict((move, 0) for move in initial_moves)

    for move in initial_moves:
        for i in range(N):
            # mängi juhuslikult seis kuni lõpuni
            res = simulate(pos, move, my_side)
            if res == "WIN":
                win_counts[move] += 1
            elif res == "DRAW":
                win_counts[move] += 0.5

    # leia suurima võitude arvuga käik, tagasta

    # ...


def play_game(pos, player_side="X"):
    playing = True
    while playing:
        if pos["flag"] == player_side:
            dump_pos(pos)
            move_str = input("Your move: ")
            move = parse_move(move_str)
        else:
            # TODO:
            move = pure_mc(pos)

        pos, xy = make_move(pos, move)
        if is_over(pos, xy):
            dump_pos(pos)
            print("Game Over!")
            playing = False
        else:
            if pos["flag"] == "X":
                pos["flag"] = "0"
            else:
                pos["flag"] = "X"


if __name__ == '__main__':
    starting_pos = {
        "flag": "X",
        "board": [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]
    }
    play_game(starting_pos)
