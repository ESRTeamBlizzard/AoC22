with open('input.txt') as f:
  
  team_pairs = []
  sum_total = 0
  sum_partial = 0
  
  for line in f.readlines():
    if not line.strip():
      break
    
    parts = line.split(',')
    
    def convert_to_int_pair(part):
      boundaries = part.split('-')
      return (int(boundaries[0]), int(boundaries[1]))
    
    one = convert_to_int_pair(parts[0])
    two = convert_to_int_pair(parts[1])
    
    def total_overlapse(one, two):
      if (one[0] <= two[0]) and (one[1] >= two[1]):
        return True
      if (two[0] <= one[0]) and (two[1] >= one[1]):
        return True
      return False
    
    if total_overlapse(one, two):
      sum_total += 1
    
    def partial_overlapse(one, two):
      def in_range(a_num, a_range):
        return (a_num >= a_range[0]) and (a_num <= a_range[1])
      
      if (in_range(one[0], two)
       or in_range(one[1], two)
       or in_range(two[0], one)
       or in_range(two[1], one)):
        return True
      
      return False
    
    if partial_overlapse(one, two):
      sum_partial += 1
    
    team_pairs.append((one, two))
    
  for x in team_pairs:
    print(x)

  print ("Sum total:   ", sum_total)  
  print ("Sum partial: ", sum_partial)  
