import random
import copy


def moves(pos):
    # pos - dict; kõik käigud algseisus
    allowed_moves = []
    for move in range(7):
        if can_move(pos, move):
            allowed_moves.append(move)
    return allowed_moves


def can_move(pos, move):
    for row in range(6):
        if pos["board"][-1 - row][move] == " ":
            return True
    return False


def make_move(pos, move):
    if can_move(pos, move):
        for row in range(6):
            if pos["board"][-1 - row][move] == " ":
                pos["board"][-1 - row][move] = pos["flag"]
                return pos, (move, 5 - row)
    else:
        return pos, (move, 0)


def simulate(pos, move):
    pos2 = copy.deepcopy(pos)
    pos2, xy = make_move(pos2, move)
    over = is_over(pos2, xy)
    if over[2]:
        return "DRAW"
    elif over[0] and not over[1]:
        return "WIN"
    elif over[0] and over[1]:
        return "LOSE"
    else:
        pos2["flag"] = "X"
        while True:
            random_move = random.randint(0, 6)
            pos2, xy = make_move(pos2, random_move)
            over = is_over(pos2, xy)
            if over[2]:
                return "DRAW"
            elif over[0] and not over[1]:
                return "WIN"
            elif over[0] and over[1]:
                return "LOSE"
            elif not over[0]:
                if pos2["flag"] == "0":
                    pos2["flag"] = "X"
                else:
                    pos2["flag"] = "0"


def dump_pos(pos):
    # prindi info seisu kohta
    for row in pos["board"]:
        print(row)
        # for i in range(7):
        # if i == 0:
        # print("|" + row[i], end="")
        # elif i == 6:
        # print(row[i] + "|", end="\n")
        # else:
        # print(row[i], end="")
    print("| 0    1    2    3    4    5    6 |")


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
    game_over = False
    p_win = False
    draw = True
    for row in board:
        if " " in row:
            draw = False
            break
    if draw:
        game_over = True
        p_win = False
        return game_over, p_win, draw
    check_down = False
    check_row = False
    check_right_dio = False
    check_left_dio = False
    if last_move[1] <= 2:
        for y in range(last_move[1], last_move[1] + 4):
            if board[y][last_move[0]] == flag:
                check_down = True
            else:
                check_down = False
                break

    if not check_down:
        check_dio_right = 0
        x_begin = 0
        y = 0
        if last_move[0] - last_move[1] >= 0:
            x_begin = last_move[0] - last_move[1]
        elif last_move[0] - last_move[1] < 0:
            y = abs(last_move[0] - last_move[1])
        for x in range(x_begin, 7):
            if check_dio_right == 4:
                break
            elif y <= 5 and board[y][x] == flag:
                check_dio_right += 1
                y += 1
            else:
                check_dio_right = 0
                y += 1
        if check_dio_right == 4:
            check_right_dio = True

    if not (check_down or check_right_dio):
        check_dio_left = 0
        x_end = 7
        y = 0
        if last_move[0] + last_move[1] <= 6:
            x_end = last_move[0] + last_move[1]
        elif last_move[0] + last_move[1] > 6:
            y = (last_move[0] + last_move[1]) - 6
        for x in range(0, x_end):
            if check_dio_left == 4:
                break
            elif y <= 5 and board[y][-2 - x] == flag:
                check_dio_left += 1
                y += 1
            else:
                check_dio_left = 0
                y += 1
        if check_dio_left == 4:
            check_left_dio = True

    if not (check_down or check_left_dio or check_right_dio):
        check = 0
        for x in range(7):
            if check == 4:
                break
            elif board[last_move[1]][x] == flag:
                check += 1
            else:
                check = 0
        if check == 4:
            check_row = True

    if check_down or check_row or check_left_dio or check_right_dio:
        game_over = True
        if flag == "X":
            p_win = True
    return game_over, p_win, draw


def pure_mc(pos, N=200):
    # kõik käigud algseisus
    my_side = pos["flag"]
    initial_moves = moves(pos)
    # loendurid iga käigu jaoks
    win_counts = dict((move, 0) for move in initial_moves)

    for move in initial_moves:
        for i in range(N):
            # mängi juhuslikult seis kuni lõpuni
            res = simulate(pos, move)
            if res == "WIN":
                win_counts[move] += 1
            elif res == "DRAW":
                win_counts[move] += 0.5
    print(win_counts)
    # leia suurima võitude arvuga käik, tagasta
    best_score = 0
    best_move = []
    for move in win_counts.keys():
        if win_counts[move] == best_score:
            best_move.append(move)
        elif win_counts[move] > best_score:
            best_move.clear()
            best_score = win_counts[move]
            best_move.append(move)
    return random.choice(best_move)


def play_game(pos, player_side="X"):
    playing = True
    while playing:
        if pos["flag"] == player_side:
            dump_pos(pos)
            move_str = input("Your move: ")
            move = parse_move(move_str)
        else:
            move = pure_mc(pos)
        pos, xy = make_move(pos, move)
        over = is_over(pos, xy)
        if over[2]:
            dump_pos(pos)
            print("Game Over! Draw")
            playing = False
        elif over[0] and over[1]:
            dump_pos(pos)
            print("Game Over! You win!")
            playing = False
        elif over[0] and not over[1]:
            dump_pos(pos)
            print("Game Over! You lose!")
            playing = False
        elif not over[0]:
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
