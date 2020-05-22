board = [
  [34,21,32,41,25],
  [14,42,43,14,31],
  [54,45,52,42,23],
  [33,15,51,31,35],
  [21,52,33,13,23],
]

def make_coord(coord):
  return coord // 10 - 1, coord % 10 - 1

def make_board(board, make_coord):
  '''Transform coded indices to regular 0-based coords.'''
  new_board = []
  for row in board:
    new_board.append([])
    for coord in row:
      new_board[-1].append(make_coord(coord))
  return new_board

def walk(board, start=(0,0)):
  '''Returns steps of the search thru the board.'''
  coord = start
  while True:
    yield coord
    new_coord = board[coord[0]][coord[1]]
    if new_coord == coord:
      break
    coord = new_coord

if __name__ == '__main__':
  print(list(walk(make_board(board, make_coord))))
