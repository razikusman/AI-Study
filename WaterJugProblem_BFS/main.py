def waterJugBFS(jugA, jugB, goal):
    # Insert the initial state to the queue/ Set the initial state (empty jugs)
    queue = [(0, 0)]
    # create a set(explored) to store previously explored states. (so that they can be pruned without exploring those duplicates again)
    explored = set()
    # Add initial state (empty jugs) to the explored set
    explored.add((0, 0))
    # Just to print the initial state (Empty state)
    for initial_state in explored:
        print(initial_state)

    while len(queue) > 0:
        # a is the actual water amount in jugA(Here, in 4L jug)
        # b is the actual water amount in jugB(Here, in 3L jug)
        # Here we remove states from the queue and assign them to a and b (one after the other)
        # So that we can further explore those states(Go to the next level and explore) and achieve our goal/desired state gradually
        a, b = queue.pop(0)
        # if we achieve the goal state, then it returns true and stops the execution
        if (a == goal and b == 0) or (a == 0 and b == goal):
            return True

        states = set()

        states.add((jugA, b))  # fill jug A;
        states.add((a, jugB))  # fill jug B;
        states.add((0, b))  # empty jug A;
        states.add((a, 0))  # empty jug B;
        states.add((min(a + b, jugA), 0 if jugA >= a + b else b - (jugA - a)))  # pour jug B to A;
        states.add((0 if jugB >= a + b else a - (jugB - b), min(a + b, jugB)))  # pour jug A to B;

        for state in states:
            # if the state is previously explored (state is in the 'explored' set) then it is not added to the queue, instead continue the execution.
            if state in explored:
                continue
            # just to print (So that we can get an idea how BFS works)
            print(state)
            # Insert the new states (previously not explored) into the queue, so that we can further explore them in upcoming steps
            queue.append(state)
            # Add the states (that are just now added to the queue) into the "explored" set, So that we can prune those states if they appear again in future. (duplicates)
            explored.add(state)
    return False


# main method from where the execution starts
if __name__ == '__main__':
    jug1 = 4
    jug2 = 3
    target = 2
    print("****Solving Water Jug Problem using Breadth First Search****\n")
    print("\nPath from the initial state to solution state: \n")

    # Call the Function that solve Water Jug Problem using BFS (With parameters)
    waterJugBFS(jug1, jug2, target)
