def solver(sudo):
    find = find_empty(sudo)
    if not find:
        return True
    else:
        y, x = find

    for i in range(1, 10):
        if legit(sudo, i, (y, x)):
            sudo[y][x] = i

            if solver(sudo):
                return True

            sudo[y][x] = 0
    return False


def legit(sudo, num, pos):
    # Horizontal
    for i in range(len(sudo[pos[0]])):
        if num == sudo[pos[0]][i] and pos[1] != i:
            return False

    # Vertical
    for i in range(len(sudo)):
        if num == sudo[i][pos[1]] and pos[0] != i:
            return False

    # 9 Cell
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if sudo[i][j] == num and pos != (i, j):
                return False
    return True


def find_empty(sudo):
    for i in range(len(sudo)):
        for j in range(len(sudo[0])):
            if sudo[i][j] == 0:
                # i vertical pos , j horizontal
                return i, j
    return None


def print_cool(sudo):
    for i in sudo:
        for j in i:
            print(j, end=" ")
        print("\r")





