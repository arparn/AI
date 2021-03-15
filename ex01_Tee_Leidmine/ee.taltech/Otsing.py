from queue import Queue, PriorityQueue


def bfs(kaart, start):
    # kaart - List with rows
    # start - tuple (x, y) -> row = kaart[y]  row[x]

    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    finish = None
    path = []
    loops = 0

    while not frontier.empty():
        current = frontier.get()
        neighbours = []
        # meid ei huvita kõik teed, seega peaks kontrollima, kas current on teemant.
        # Kui on, siis katkestame otsingu
        # (ja loomulikult jätame teemandi koordinaadid meelde)
        row = kaart[current[1]]
        point = row[current[0]]
        loops += 1
        if point == "D":
            finish = current
            break
        elif point != "*":
            if len(kaart) == current[1] + 1:
                neighbours.append((current[0], current[1] - 1))
            elif 0 == current[1]:
                neighbours.append((current[0], current[1] + 1))
            else:
                neighbours.append((current[0], current[1] - 1))
                neighbours.append((current[0], current[1] + 1))

            if len(row) == current[0] + 1:
                neighbours.append((current[0] - 1, current[1]))
            elif 0 == current[0]:
                neighbours.append((current[0] + 1, current[1]))
            else:
                neighbours.append((current[0] - 1, current[1]))
                neighbours.append((current[0] + 1, current[1]))
        for next_tipp in neighbours:  # see osa tuleb suht palju ümber teha.
            # tuleb leida sobivad naaberruudud kaardilt
            # nagu ta meile ette on antud (ülal, all,
            # paremal ja vasakul olev ruut)
            if next_tipp not in came_from.keys():
                frontier.put(next_tipp)
                came_from[next_tipp] = current

    current_tipp = finish
    path.append(finish)
    while start not in path:
        current_tipp = came_from.get(current_tipp)
        path.append(current_tipp)
    # Kui teemant on leitud, tuleb ka teekond rekonstrueerida
    # mis andmestruktuurina teekonda esitada, pole oluline,
    # aga loomulik viis oleks list
    path.reverse()
    return len(path), loops


def h(node, goal):
    return abs(goal[0] - node[0]) + abs(goal[1] - node[1])


def greedy(kaart, start, goal):
    # kaart - List with rows
    # start - tuple (x, y) -> row = kaart[y]  row[x]

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    finish = None
    path = []
    loops = 0

    while not frontier.empty():
        current_h = frontier.get()
        current = current_h[1]
        neighbours = []
        # meid ei huvita kõik teed, seega peaks kontrollima, kas current on teemant.
        # Kui on, siis katkestame otsingu
        # (ja loomulikult jätame teemandi koordinaadid meelde)
        row = kaart[current[1]]
        point = row[current[0]]
        loops += 1
        if point == "D":
            finish = current
            break
        elif point != "*":
            if len(kaart) == current[1] + 1:
                neighbours.append((current[0], current[1] - 1))
            elif 0 == current[1]:
                neighbours.append((current[0], current[1] + 1))
            else:
                neighbours.append((current[0], current[1] - 1))
                neighbours.append((current[0], current[1] + 1))

            if len(row) == current[0] + 1:
                neighbours.append((current[0] - 1, current[1]))
            elif 0 == current[0]:
                neighbours.append((current[0] + 1, current[1]))
            else:
                neighbours.append((current[0] - 1, current[1]))
                neighbours.append((current[0] + 1, current[1]))
        for next_tipp in neighbours:  # see osa tuleb suht palju ümber teha.
            # tuleb leida sobivad naaberruudud kaardilt
            # nagu ta meile ette on antud (ülal, all,
            # paremal ja vasakul olev ruut)
            if next_tipp not in came_from.keys():
                priority = h(next_tipp, goal)
                frontier.put((priority, next_tipp))
                came_from[next_tipp] = current

    current_tipp = finish
    path.append(finish)
    while start not in path:
        current_tipp = came_from.get(current_tipp)
        path.append(current_tipp)
    # Kui teemant on leitud, tuleb ka teekond rekonstrueerida
    # mis andmestruktuurina teekonda esitada, pole oluline,
    # aga loomulik viis oleks list
    path.reverse()
    return len(path), loops


def astar(kaart, start, goal):
    # kaart - List with rows
    # start - tuple (x, y) -> row = kaart[y]  row[x]

    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    finish = None
    path = []
    loops = 0

    while not frontier.empty():
        current_h = frontier.get()
        current = current_h[1]
        neighbours = []
        # meid ei huvita kõik teed, seega peaks kontrollima, kas current on teemant.
        # Kui on, siis katkestame otsingu
        # (ja loomulikult jätame teemandi koordinaadid meelde)
        row = kaart[current[1]]
        point = row[current[0]]
        loops += 1
        if point == "D":
            finish = current
            break
        elif point != "*":
            if len(kaart) == current[1] + 1:
                neighbours.append((current[0], current[1] - 1))
            elif 0 == current[1]:
                neighbours.append((current[0], current[1] + 1))
            else:
                neighbours.append((current[0], current[1] - 1))
                neighbours.append((current[0], current[1] + 1))

            if len(row) == current[0] + 1:
                neighbours.append((current[0] - 1, current[1]))
            elif 0 == current[0]:
                neighbours.append((current[0] + 1, current[1]))
            else:
                neighbours.append((current[0] - 1, current[1]))
                neighbours.append((current[0] + 1, current[1]))
        for next_tipp in neighbours:  # see osa tuleb suht palju ümber teha.
            # tuleb leida sobivad naaberruudud kaardilt
            # nagu ta meile ette on antud (ülal, all,
            # paremal ja vasakul olev ruut)
            new_cost = cost_so_far[current] + 1
            if next_tipp not in cost_so_far or new_cost < cost_so_far[next_tipp]:
                cost_so_far[next_tipp] = new_cost
                priority = new_cost + h(next_tipp, goal)  # g(n) + h(n)
                frontier.put((priority, next_tipp))
                came_from[next_tipp] = current

    current_tipp = finish
    path.append(finish)
    while start not in path:
        current_tipp = came_from.get(current_tipp)
        path.append(current_tipp)
    # Kui teemant on leitud, tuleb ka teekond rekonstrueerida
    # mis andmestruktuurina teekonda esitada, pole oluline,
    # aga loomulik viis oleks list
    path.reverse()
    return len(path), loops

if __name__ == '__main__':

    with open("cave900x900") as f:
        map_data = [l.strip() for l in f.readlines() if len(l) > 1]
    with open("cave300x300") as f:
        map_data3 = [l.strip() for l in f.readlines() if len(l) > 1]
    with open("cave600x600") as f:
        map_data6 = [l.strip() for l in f.readlines() if len(l) > 1]
    ss = (2, 2)

    path, loop = bfs(map_data3, ss)
    print("300 bfs path length and loops: " + str(path) + " " + str(loop))

    path, loop = bfs(map_data6, ss)
    print("600 bfs path length and loops: " + str(path) + " " + str(loop))

    path, loop = bfs(map_data, ss)
    print("900 bfs path length and loops: " + str(path) + " " + str(loop))

    print("------------------------------------------------------------")

    path, loop = greedy(map_data3, ss, (257, 295))
    print("300 greedy path length and loops: " + str(path) + " " + str(loop))

    path, loop = greedy(map_data6, ss, (595, 598))
    print("600 greedy path length and loops: " + str(path) + " " + str(loop))

    path, loop = greedy(map_data, ss, (895, 898))
    print("900 greedy path length and loops: " + str(path) + " " + str(loop))

    print("------------------------------------------------------------")

    path, loop = astar(map_data3, ss, (257, 295))
    print("300 astar path length and loops: " + str(path) + " " + str(loop))

    path, loop = astar(map_data6, ss, (595, 598))
    print("600 astar path length and loops: " + str(path) + " " + str(loop))

    path, loop = astar(map_data, ss, (895, 898))
    print("900 astar path length and loops: " + str(path) + " " + str(loop))

