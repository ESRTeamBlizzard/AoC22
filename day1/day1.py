with open('input.txt') as f:
  sums = []
  currSum = 0
  for line in f.readlines():
    if line.strip():
      currSum += int(line)
    else:
      sums.append(currSum)
      currSum = 0
  print(sums)
  print("Max index: ", sums.index(max(sums)))
  print("Max value: ", max(sums))
  
  sums.sort(reverse=True)
  print("Sum of three max: ", sums[0] + sums[1] + sums[2])
  
  