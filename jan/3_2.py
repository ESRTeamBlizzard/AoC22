with open('input/3.txt', mode='rt') as f:
    total_prios = 0

    for (line1, line2, line3) in zip(*[iter(f)] * 3, strict=True):

        line1 = line1.strip()
        line2 = line2.strip()
        line3 = line3.strip()

        set1 = set(line1)
        set2 = set(line2)
        set3 = set(line3)

        common_item = set.intersection(set1, set2).intersection(set3).pop()

        if 'a' <= common_item <= 'z':
            total_prios += ord(common_item) - (ord('a') - 1)
        else:
            total_prios += ord(common_item) - (ord('A') - 1) + 26

print(total_prios)
