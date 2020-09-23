def distance(target, start):
  total = 0
  row_dist = abs(target[0]- start[0])
  col_dist = abs(target[1]- start[1])
  total = row_dist + col_dist
  return total
  
def pacman(target, ghosts):
  closest_ghost = float('inf')
  for ghost in ghosts:
    dist= distance(target, ghost)
    if dist < closest_ghost:
      closest_ghost = dist
      
  player_dist = distance(target, [0,0])
  
  return player_dist < closest_ghost

print(pacman([0, 1], [[1, 0], [0, 3]]))
