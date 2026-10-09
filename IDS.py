
def get_neighbors(state):
    neighbors = []
    i = state.index(0)
    row, col = i // 3, i % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            j = r * 3 + c
            new_state = list(state)
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(tuple(new_state))

    return neighbors


def dls(state, goal, limit, path):
    if state == goal:
        return path

    if limit == 0:
        return None

    for neighbor in get_neighbors(state):
        if neighbor not in path:
            result = dls(
                neighbor, goal, limit - 1, path + [neighbor]
            )

            if result is not None:
                return result

    return None


def ids(start, goal):
    depth = 0

    while True:
        result = dls(start, goal, depth, [start])

        if result is not None:
            return result

        depth += 1


def display(path):
    print("Solution found in", len(path) - 1, "moves")

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()


while True:
    try:
        start = tuple(map(int, input(
            "Enter 9 numbers (0 for blank): "
        ).split()))

        if len(start) != 9:
            print("Enter exactly 9 numbers.")
        elif set(start) != set(range(9)):
            print("Enter numbers 0 to 8 exactly once.")
        else:
            break

    except ValueError:
        print("Enter integers only.")

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

display(ids(start, goal))