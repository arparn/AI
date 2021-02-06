from queue import Queue


def minu_otsing(kaart, start):
    # kaart - List with rows
    # start - tuple (x, y) -> row = kaart[y]  row[x]

    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    finish = None

    while not frontier.empty():
        current = frontier.get()
        neighbours = []

        # meid ei huvita kõik teed, seega peaks kontrollima, kas current on teemant.
        # Kui on, siis katkestame otsingu
        # (ja loomulikult jätame teemandi koordinaadid meelde)
        row = kaart[current[1]]
        point = row[current[0]]
        if point == "D":
            finish = current
            break
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
# TODO:
        for nextTipp in neighbours:  # see osa tuleb suht palju ümber teha.
            # tuleb leida sobivad naaberruudud kaardilt
            # nagu ta meile ette on antud (ülal, all,
            # paremal ja vasakul olev ruut)
            if nextTipp not in came_from:
                frontier.put(nextTipp)
                came_from[nextTipp] = current

    # Kui teemant on leitud, tuleb ka teekond rekonstrueerida
    # mis andmestruktuurina teekonda esitada, pole oluline,
    # aga loomulik viis oleks list
    return path
