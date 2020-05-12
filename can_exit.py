#Input: Maze denoted with grid nxm
#0 denotes walkable path, 1 denotes wall

"""
can_exit([
	[0, 1, 1, 1, 1, 1, 1], 
	[0, 0, 1, 1, 0, 1, 1], 
	[1, 0, 0, 0, 0, 1, 1], 
	[1, 1, 1, 1, 0, 0, 1], 
	[1, 1, 1, 1, 1, 0, 0]
]) -> True
"""

def can_exit(lst):
  maze = lst
  #Denote goal = 5
  maze[-1][-1] = 5
  return search(0,0, maze)

def search(row, column, maze):
  print("Scanning", row, column)
  #Get a visual of where I am, where 2 = location
  state = maze[row][column]
  maze[row][column] = 2
  for i in maze:
    print(i)

  #Change the 2 (position) back to what it was before
  maze[row][column] = state

  #False where we visited and walls
  #Only allow true if exit is found
  if maze[row][column] == 5:
    print("Found exit at: ", row, column)
    return True
  elif maze[row][column] == 1:
    print("Hit wall at ", row, column)
    return False
  elif maze[row][column] == 3:
    print("Visited", row, column)
    return False

  #Mark area visited
  maze[row][column] = 3 

  #Look right, then down, then left, then up
  if ((row < len(maze) - 1 and search(row + 1, column, maze))
    or (column > 0 and search(row, column - 1, maze))
    or (row > 0 and search(row - 1, column, maze))
    or (column < len(maze[0]) - 1 and search(row, column + 1, maze))):
    return True

  return False


can_exit([
	[0, 1, 1, 1, 1, 1, 1], 
	[0, 0, 1, 1, 0, 1, 1], 
	[1, 0, 0, 0, 0, 1, 1], 
	[1, 1, 1, 1, 0, 0, 1], 
	[1, 1, 1, 1, 1, 0, 0]
])
