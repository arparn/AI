class NQPosition:
    def __init__(self, N):
        # choose some internal representation of the NxN board
        # put queens on it
        self.N = N
        queens = []
        for i in range(N):
            queens.append((i, 0))
        self.queens = queens

    def value(self):
        # return current number of conflicts
        conflicts = []
        for queen in self.queens:
            for i in range(self.N):
                if (i, queen[1]) != queen and (i, queen[1]) in self.queens and (queen, (i, queen[1])) not in conflicts and ((i, queen[1]), queen) not in conflicts:
                    conflicts.append((queen, (i, queen[1])))
                if (queen[0], i) != queen and (queen[0], i) in self.queens and (queen, (queen[0], i)) not in conflicts and ((queen[0], i), queen) not in conflicts:
                    conflicts.append((queen, (queen[0], i)))
                x = queen[0] - (i + 1)
                y = queen[1] - (i + 1)
                if x >= 0 and y >= 0 and (x, y) != queen and (x, y) in self.queens and (queen, (x, y)) not in conflicts and ((x, y), queen) not in conflicts:
                    conflicts.append((queen, (x, y)))
                x = queen[0] + (i + 1)
                y = queen[1] + (i + 1)
                if x <= self.N - 1 and y <= self.N - 1 and (x, y) != queen and (x, y) in self.queens and (queen, (x, y)) not in conflicts and ((x, y), queen) not in conflicts:
                    conflicts.append((queen, (x, y)))
                x = queen[0] + (i + 1)
                y = queen[1] - (i + 1)
                if x <= self.N - 1 and y >= 0 and (x, y) != queen and (x, y) in self.queens and (queen, (x, y)) not in conflicts and ((x, y), queen) not in conflicts:
                    conflicts.append((queen, (x, y)))
                x = queen[0] - (i + 1)
                y = queen[1] + (i + 1)
                if x >= 0 and y <= self.N - 1 and (x, y) != queen and (x, y) in self.queens and (queen, (x, y)) not in conflicts and ((x, y), queen) not in conflicts:
                    conflicts.append((queen, (x, y)))
        return len(conflicts)

    def make_move(self, move):
        # actually execute a move (change the board)
        index = self.queens.index(move[0])
        self.queens[index] = move[1]

    def best_move(self):
        # find the best move and the value function after making that move
        best_m = None
        value = self.value()
        same_values = []
        for queen in self.queens:
            for i in range(self.N):
                if i == queen[1]:
                    continue
                else:
                    new_pos = (queen[0], i)
                    move = (queen, new_pos)
                    self.make_move(move)
                    new_value = self.value()
                    if new_value < value:
                        value = new_value
                        best_m = move
                        same_values.clear()
                        same_values.append(move)
                    elif new_value == value:
                        same_values.append(move)
                    self.make_move((new_pos, queen))
        if len(same_values) > 0:
            import random
            best_m = random.choice(same_values)
        return best_m, value

    def draw(self):
        queen_map = []
        for y in range(self.N):
            queen_map.append([])
            for x in range(self.N):
                if (x, y) in self.queens:
                    queen_map[y].append(1)
                else:
                    queen_map[y].append(0)
        return queen_map


def hill_climbing(pos):
    curr_value = pos.value()
    while True:
        move, new_value = pos.best_move()
        if new_value == 0:
            pos.make_move(move)
            return pos, new_value
        elif new_value >= curr_value and new_value != 0:
            return hill_climbing(NQPosition(pos.N))
        else:
            # position improves, keep searching
            curr_value = new_value
            pos.make_move(move)


if __name__ == '__main__':
    pos = NQPosition(8)  # test with the tiny 4x4 board first
    print("Initial position value", pos.value())
    best_pos, best_value = hill_climbing(pos)
    print("Final value", best_value)
    print("Final positions: ", best_pos.queens)
    mapp = best_pos.draw()
    for row in mapp:
        print(row)
    # if best_value is 0, we solved the problem
