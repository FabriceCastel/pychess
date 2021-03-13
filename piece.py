import enum

class PieceRank(enum.Enum):
  Pawn = 1
  Queen = 2
  King = 3
  Knight = 4
  Bishop = 5
  Rook = 6

class PieceColor(enum.Enum):
  White = 1
  Black = 2

# TODO add the other ranks
RANK_TO_STRING = {
  PieceRank.Pawn: 'p',
  PieceRank.Queen: 'Q',
  PieceRank.Knight: 'k',
  PieceRank.Bishop: 'b',
  PieceRank.Rook: 'r',
  PieceRank.King: 'K'
}

COLOR_TO_STRING = {
  PieceColor.White: 'w',
  PieceColor.Black: 'b'
}

class Piece:
  def __init__(self, rank: PieceRank, color: PieceColor):
    self.rank = rank
    self.color = color

  # Piece string representations:
  # - pawn    p
  # - queen   Q
  # - king    K
  # - knight  k
  # - rook    r
  # - bishop  b
  #
  # Piece representations with color:
  # w (white), b (black)
  #
  # Example piece representations:
  # w-Q (white queen)
  # b-k (black knight)

  def __str__(self):
    return '{0}-{1}'.format(\
      COLOR_TO_STRING[self.color],\
      RANK_TO_STRING[self.rank])

  def __eq__(self, obj):
    return isinstance(obj, Piece)\
      and self.rank == obj.rank\
      and self.color == obj.color

