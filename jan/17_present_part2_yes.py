import itertools
import time


def main():
    jets = []
    jet_max = 0

    with open('input/17.txt', mode='rt') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue

            jet_max = len(line)
            jets = itertools.cycle(line)
            break

    r1 = [
        [(0, 0)],
        [(1, 0)],
        [(2, 0)],
        [(3, 0)],
    ]

    r2 = [
        [(0, 1)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 1)],
    ]

    r3 = [
        [(0, 0)],
        [(1, 0)],
        [(2, 0), (2, 1), (2, 2)],
    ]

    r4 = [
        [(0, 3), (0, 2), (0, 1), (0, 0)],
    ]

    r5 = [
        [(0, 0), (0, 1)],
        [(1, 0), (1, 1)],
    ]

    rocks = [r1, r2, r3, r4, r5]
    rock_heights = [1, 3, 3, 4, 2]
    # rocks_width = [len(r1), len(r2), len(r3), len(r4), len(r5)]

    rock_sets = []
    for rock in rocks:
        rock_sets.append(set([p for col in rock for p in col]))

    rocks = itertools.cycle(rocks)

    cave = set()
    cave_width = 7

    highest = -1
    rock_i = 0

    # max_rocks = 2022
    max_rocks = 1000000000000

    tick = 100000
    n_ticks = max_rocks / tick
    avg = 1

    last = start = time.time_ns()

    states = dict()
    highest_hist = []
    jet_i = -1
    max_ys = [-1, -1, -1, -1, -1, -1, -1]
    cycle_found = False

    i = -1
    while True:
        i += 1
        if i >= max_rocks:
            break

        if i > 0 and i % tick == 0:
            since_last = time.time_ns() - last
            i_tick = i // tick
            if i_tick == 1:
                avg = since_last
            else:
                avg = avg * ((i_tick - 1) / i_tick) + since_last * (1 / i_tick)

            # print(f"{since_last / 1000 / 1000} ms")
            # print(f"{avg / 1000 / 1000} ms")
            print(f"{(avg * n_ticks) / 1000 / 1000 / 1000 / 60 / 60 / 24} d")
            last = time.time_ns()

            # print(i)
            # print(max_rocks)

        rock = next(rocks)

        x = 2
        y = highest + 4

        # draw(cave, rock, x, y, highest)

        stopped = False
        while not stopped:
            jet = next(jets)
            jet_i = (jet_i + 1) % jet_max

            if jet == '>':
                apply_jet = True
                new_max_x = x + len(rock)
                # collision with right cave wall
                if new_max_x >= cave_width:
                    apply_jet = False
                else:
                    # collision with rocks to the right
                    # only possible if we are not above the tower
                    if y <= highest:
                        new_rock_right = [(p[0] + x + 1, p[1] + y) for p in rock_sets[rock_i]]
                        if not cave.isdisjoint(new_rock_right):
                            apply_jet = False

                if apply_jet:
                    x += 1
            else:  # jet == '<'
                apply_jet = True
                new_min_x = x - 1
                # collision with left cave wall
                if new_min_x < 0:
                    apply_jet = False
                else:
                    # collision with rocks to the left
                    # only possible if we are not above the tower
                    if y <= highest:
                        new_rock_left = [(p[0] + x - 1, p[1] + y) for p in rock_sets[rock_i]]
                        if not cave.isdisjoint(new_rock_left):
                            apply_jet = False

                if apply_jet:
                    x -= 1

            # draw(cave, rock, x, y, highest)

            fall = True
            # skip test if we are above highest + 1
            if y <= highest + 1:
                # collision with stopped rocks
                new_rock_down = [(p[0] + x, p[1] + y - 1) for p in rock_sets[rock_i]]
                if not cave.isdisjoint(new_rock_down):
                    fall = False
                else:
                    # collision with bottom of cave
                    if y <= 0:
                        fall = False

            if fall:
                y -= 1
            else:
                stopped_rock = [(p[0] + x, p[1] + y) for p in rock_sets[rock_i]]
                cave.update(stopped_rock)
                for rock_x, rock_y in stopped_rock:
                    if max_ys[rock_x] < rock_y:
                        max_ys[rock_x] = rock_y

                if (top := y + rock_heights[rock_i] - 1) > highest:
                    highest = top

                stopped = True

                if not cycle_found:
                    rel_ys = [-1, -1, -1, -1, -1, -1, -1]
                    for i_ys in range(len(max_ys)):
                        rel_ys[i_ys] = highest - max_ys[i_ys]

                    entry = (rock_i, jet_i, str(rel_ys))
                    if entry not in states:
                        states[entry] = i
                    else:
                        cycle_start = states[entry]
                        cycle_end = i
                        cycle_len = cycle_end - cycle_start
                        print(f"cycle detected: {cycle_start=}, {cycle_end=}, {cycle_len=}")

                        height_per_cycle = highest - highest_hist[cycle_start]
                        num_cycles = (max_rocks - i) // cycle_len

                        highest += (num_cycles * height_per_cycle)
                        i += (num_cycles * cycle_len)

                        print(f"{rel_ys=}")
                        print(f"{max_ys=}")
                        for i_ys in range(len(max_ys)):
                            max_ys[i_ys] += (num_cycles * height_per_cycle)
                            cave.add((i_ys, max_ys[i_ys]))
                        print(f"new {max_ys=}")

                        print(f"{height_per_cycle=}")
                        print(f"{num_cycles=}")
                        print(f"{highest=}")
                        print(f"{i=}")

                        cycle_found = True

                highest_hist.append(highest)
                rock_i = (rock_i + 1) % 5

            # draw(cave, rock, x, y, highest)

    # draw(cave, [], 0, 0, highest)

    print(f"final {max_ys=}")

    end = time.time_ns()
    print(f"wall time: {(end - start) / 1000 / 1000} ms")

    print(f"tower height: {highest + 1}")


def draw(cave, rock, x, y, highest):
    print('')

    rock_as_set = set([(p[0] + x, p[1] + y) for col in rock for p in col])
    for cave_y in range(highest + 8, -1, -1):
        for cave_x in range(0, 7):
            if (cave_x, cave_y) in rock_as_set:
                sym = '@'
            elif (cave_x, cave_y) in cave:
                sym = '#'
            else:
                sym = '.'
            print(sym, end='')
        print('')
    return


if __name__ == '__main__':
    main()
