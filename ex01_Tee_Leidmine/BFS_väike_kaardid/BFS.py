from queue import Queue


def minu_otsing(kaart, start):
    # kaart - List with rows
    # start - tuple (x, y) -> row = kaart[y]  row[x]

    frontier = Queue()
    frontier.put(start)
    came_from = {start: None}
    finish = None
    path = []

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
    return path


if __name__ == '__main__':
    k = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
    ]
    s = (16, 14)
    print("map1 : " + str(minu_otsing(k, s)))
    m2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
    ]
    print("map2 : " + str(minu_otsing(m2, s)))
