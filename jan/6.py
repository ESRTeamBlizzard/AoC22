with open('input/6.txt', mode='rt') as f:
    # part 1
    marker_length = 4

    # part 2
    # marker_length = 14

    for line in f:
        count = 0
        recent = []

        for char in line:
            count += 1
            recent.append(char)

            if count > marker_length:
                recent.pop(0)

                comp = set(recent)
                if len(comp) == marker_length:
                    break

        print(recent)
        print(count)
