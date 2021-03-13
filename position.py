from illegal_position_exception import IllegalPositionException

COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

class Position:
  def __init__(self, column: int, row: int):
    self._check_position_valid(column, row)
    self.column = column
    self.row = row

  def offset(self, column_offset: int, row_offset: int):
    column = self.column + column_offset
    row = self.row + row_offset

    self._check_position_valid(column, row)

    return Position(column, row)

  def up(self):
    return self.offset(0, 1)

  def down(self):
    return self.offset(0, -1)
  
  def left(self):
    return self.offset(-1, 0)

  def right(self):
    return self.offset(1, 0)

  def _check_position_valid(self, column: int, row: int):
    if (column > 7 or column < 0 or row > 7 or row < 0):
      raise IllegalPositionException

  def __str__(self) -> str:
    return '{0}{1}'.format(COLUMN_NAMES[self.column], self.row + 1)

  def __eq__(self, obj):
    return isinstance(obj, Position)\
      and self.column == obj.column\
      and self.row == obj.row

  def __hash__(self):
    return self.column + (self.row * 8)