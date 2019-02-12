def to_cycles(perm):
    pi = {i+1: perm[i] for i in range(len(perm))}
    cycles = []

    while pi:
        elem0 = next(iter(pi))
        this_elem = pi[elem0]
        next_item = pi[this_elem]

        cycle = []
        while True:
            cycle.append(this_elem)
            del pi[this_elem]
            this_elem = next_item
            if next_item in pi:
                next_item = pi[next_item]
            else:
                break

        cycles.append(cycle)

    return cycles


import itertools
n = int(input())
a = []
is_ok = []
cycles = []
for i in itertools.permutations(range(1, n+1)):
    a.append(i)
    is_ok.append(1)
    print(str(to_cycles(i)).replace("[", "(").replace("]", ")").replace(" ", "")[1:-1].replace("),", ")"))
