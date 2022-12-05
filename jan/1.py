import heapq

sums_heap = [0, 0, 0]

with open('input/1.txt', mode='rt') as f:
    current_sum = 0
    for line in f:

        if len(line.strip()) == 0:
            if current_sum > sums_heap[0]:
                heapq.heapreplace(sums_heap, current_sum)

            current_sum = 0
            continue

        current_sum += int(line)

print(sums_heap[-1])
print(sum(sums_heap))
