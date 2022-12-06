import re

with open('input/5.txt', mode='rt') as f:
    stacks = [
        ['Q', 'W', 'P', 'S', 'Z', 'R', 'H', 'D'],
        ['V', 'B', 'R', 'W', 'Q', 'H', 'F'],
        ['C', 'V', 'S', 'H'],
        ['H', 'F', 'G'],
        ['P', 'G', 'J', 'B', 'Z'],
        ['Q', 'T', 'J', 'H', 'W', 'F', 'L'],
        ['Z', 'T', 'W', 'D', 'L', 'V', 'J', 'N'],
        ['D', 'T', 'Z', 'C', 'J', 'G', 'H', 'F'],
        ['W', 'P', 'V', 'M', 'B', 'H'],
    ]

    for line in f:
        count, start, end = map(lambda x: int(x), re.findall(r"^move (\d+) from (\d+) to (\d+)$", line)[0])

        # CrateMover9000 (part 1)
        for i in range(count):
            crate = stacks[start - 1].pop()
            stacks[end - 1].append(crate)

        # CrateMover9001 (part 2)
        # crates = []
        # for i in range(count):
        #     crates.append(stacks[start - 1].pop())
        #
        # crates.reverse()
        # stacks[end - 1] += crates

    for stack in stacks:
        print(stack[-1])
