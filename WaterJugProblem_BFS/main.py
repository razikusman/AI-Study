def waterJugBFS(jugA, jugB, z):

    # set the initial state (empty jugs)
    queue = [(0, 0)]
    explored = set((0, 0))

    while len(queue) > 0:
        a, b = queue.pop(0)
        if a + b == z:
            # print(a, b)
            return True

        states = set()

        states.add((jugA, b))  # fill jug A;
        states.add((a, jugB))  # fill jug B;
        states.add((0, b))  # empty jug A;
        states.add((a, 0))  # empty jug B;
        states.add((min(jugA, b + a), 0 if b < jugA - a else b - (jugA - a)))  # pour jug B to A;
        states.add((0 if a + b < jugB else a - (jugB - b), min(b + a, jugB)))  # pour jug A to B;

        for state in states:
            if state in explored:
                continue
            queue.append(state)
            print(str(state))
            explored.add(state)

    return False


if __name__ == '__main__':
    jug1 = 4
    jug2 = 3
    target = 2
    print("****Solving Water Jug Problem using Breadth First Search****")
    print()
    print("Path from the initial state to the solution state: ")

    waterJugBFS(jug1, jug2, target)
