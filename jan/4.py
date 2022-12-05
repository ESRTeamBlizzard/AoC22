import re

with open('input/4.txt', mode='rt') as f:
    total_contained = 0
    total_overlap = 0

    for line in f:
        s1, e1, s2, e2 = map(lambda x: int(x), re.findall(r"^(\d+)-(\d+),(\d+)-(\d+)$", line)[0])

        if (e1 >= s2 and s1 <= e2) \
                or (e2 >= s1 and s2 <= e1):
            total_overlap += 1

            if (s1 <= s2 and e1 >= e2) \
                    or (s2 <= s1 and e2 >= e1):
                total_contained += 1

    print(total_contained)
    print(total_overlap)
