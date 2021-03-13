from piece import Piece
from position import Position

class PiecePlacement:
  def __init__(self, piece: Piece, position: Position):
    self.piece = piece
    self.position = position

  def __eq__(self, obj):
    return isinstance(obj, PiecePlacement)\
      and self.piece == obj.piece\
      and self.position == obj.position