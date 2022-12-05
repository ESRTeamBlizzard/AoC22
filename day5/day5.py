from collections import deque

with open('input.txt') as f:
  
  SHIP = [deque(),
          deque(['D', 'H', 'R', 'Z', 'S', 'P', 'W', 'Q']),
          deque(     ['F', 'H', 'Q', 'W', 'R', 'B', 'V']),
          deque(                    ['H', 'S', 'V', 'C']),
          deque(                         ['G', 'F', 'H']),
          deque(               ['Z', 'B', 'J', 'G', 'P']),
          deque(     ['L', 'F', 'W', 'H', 'J', 'T', 'Q']),
          deque(['N', 'J', 'V', 'L', 'D', 'W', 'T', 'Z']),
          deque(['F', 'H', 'G', 'J', 'C', 'Z', 'T', 'D']),
          deque(          ['H', 'B', 'M', 'V', 'P', 'W'])
          ]
    
  print("BEFORE:")
  for x in SHIP:
    print(x)
  print("*******")
  
  line_counter = 0
  
  for line in f.readlines():
    if not line.strip():
      break
    
    _, a, _, b, _, c = line.strip().split(' ')
    
    num_crates = int(a)
    move_from  = int(b)
    move_to    = int(c)
    
    line_counter += 1
    
    # CrateMover 9000
    #for i in range(num_crates):
    #  SHIP[move_to].appendleft(SHIP[move_from].popleft())
    
    # CrateMover 9001
    for i in range(num_crates):
      SHIP[0].appendleft(SHIP[move_from].popleft())
    for i in range(num_crates):
      SHIP[move_to].appendleft(SHIP[0].popleft())
        
  print("AFTER", line_counter, ":")
  for x in SHIP:
    print(x)
