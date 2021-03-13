from position import Position

class Move:
  def __init__(self, start: Position, end: Position):
    self.start = start
    self.end = end

  def __str__(self) -> str:
    return '{0} to {1}'.format(str(self.start), str(self.end))
 
  def __eq__(self, obj):
    return isinstance(obj, Move)\
      and self.start == obj.start\
      and self.end == obj.end

  def __hash__(self):
    return self.start.__hash__() + (1000 * self.end.__hash__())