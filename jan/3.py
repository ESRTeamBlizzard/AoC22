with open('input/3.txt', mode='rt') as f:
    total_prios = 0

    for line in f:
        line = line.strip()
        compartment1 = line[0:len(line) // 2]
        compartment2 = line[len(line) // 2:]

        set1 = set(compartment1)
        set2 = set(compartment2)

        common_item = set.intersection(set1, set2).pop()

        if 'a' <= common_item <= 'z':
            total_prios += ord(common_item) - (ord('a') - 1)
        else:
            total_prios += ord(common_item) - (ord('A') - 1) + 26

print(total_prios)
