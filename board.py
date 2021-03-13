from piece import Piece, PieceRank, PieceColor
from position import Position
from illegal_move_exception import IllegalMoveException
from piece_placement import PiecePlacement
from typing import List

BOARD_WIDTH = 8

class Board:
  # A1, C2 are examples of positions
  def __init__(self):
    self._initialize_pieces()

  def _initialize_pieces(self):
    self._pieces = []
    for column in range(BOARD_WIDTH):
      self._pieces.append([])

      for row in range(BOARD_WIDTH):
        self._pieces[column].append(None)

  def setup(self):
    self._initialize_pieces()

    B = PieceColor.Black
    W = PieceColor.White

    p = PieceRank.Pawn
    k = PieceRank.Knight
    K = PieceRank.King
    Q = PieceRank.Queen
    b = PieceRank.Bishop
    r = PieceRank.Rook

    piece_positions = {
      # Back row for white
      Position(0, 0): Piece(r, W),
      Position(1, 0): Piece(k, W),
      Position(2, 0): Piece(b, W),
      Position(3, 0): Piece(Q, W),
      Position(4, 0): Piece(K, W),
      Position(5, 0): Piece(b, W),
      Position(6, 0): Piece(k, W),
      Position(7, 0): Piece(r, W),

      # Front row for white
      Position(0, 1): Piece(p, W),
      Position(1, 1): Piece(p, W),
      Position(2, 1): Piece(p, W),
      Position(3, 1): Piece(p, W),
      Position(4, 1): Piece(p, W),
      Position(5, 1): Piece(p, W),
      Position(6, 1): Piece(p, W),
      Position(7, 1): Piece(p, W),

      # Back row for black
      Position(0, 7): Piece(r, B),
      Position(1, 7): Piece(k, B),
      Position(2, 7): Piece(b, B),
      Position(3, 7): Piece(Q, B),
      Position(4, 7): Piece(K, B),
      Position(5, 7): Piece(b, B),
      Position(6, 7): Piece(k, B),
      Position(7, 7): Piece(r, B),

      # Front row for black
      Position(0, 6): Piece(p, B),
      Position(1, 6): Piece(p, B),
      Position(2, 6): Piece(p, B),
      Position(3, 6): Piece(p, B),
      Position(4, 6): Piece(p, B),
      Position(5, 6): Piece(p, B),
      Position(6, 6): Piece(p, B),
      Position(7, 6): Piece(p, B),
    }

    for position, piece in piece_positions.items():
      self.add_piece(piece, position)

  def add_piece(self, piece: Piece, position: Position) -> None:
    self._pieces[position.column][position.row] = piece

  def move_piece(self, old: Position, new: Position) -> None:
    piece = self._pieces[old.column][old.row]

    if (piece == None or old == new):
      raise IllegalMoveException

    self._pieces[new.column][new.row] = piece
    self._pieces[old.column][old.row] = None

  def remove_piece(self, position: Position) -> None:
    piece = self._pieces[position.column][position.row]

    if (piece == None):
      raise IllegalMoveException

    self._pieces[position.column][position.row] = None

  def get_pieces(self) -> List[PiecePlacement]:
    piece_placements = []
    for column in range(BOARD_WIDTH):
      for row in range(BOARD_WIDTH):
        piece = self._pieces[column][row]
        if (piece != None):
          piece_placement = PiecePlacement(piece, Position(column, row))
          piece_placements.append(piece_placement)

    return piece_placements

  def get_piece(self, position: Position):
    return self._pieces[position.column][position.row]

  def __str__(self):
    line_divider = "+------+------+------+------+------+------+------+------+\n"

    # Each string in this array should look like:
    # |      | w-Q  |      | b-p  |      |      |      |      |
    # |      |      |      |      |      |      |      |      |
    row_strings = []

    for row in range(BOARD_WIDTH - 1, -1, -1):
      # Each string in this array should look like (minus quotes)
      # eg 1
      # "      "
      # eg 2
      # " w-Q  "
      square_strings = []

      for column in range(BOARD_WIDTH):
        piece = self._pieces[column][row]

        if (piece == None):
          square_strings.append('      ')
        else:
          square_string = ' {0}  '.format(str(piece))
          square_strings.append(square_string)

      # square_strings: [' w-Q  ', '     ', '     ', ' b-K  ', ...]
      # '|'.join(square_strings) -> ' w-Q  |     |     | b-K  | .....'
      # row_string -> '| w-Q  |     |     | b-K  | .... |'
      row_inner_string = '|'.join(square_strings)
      row_string = '|{0}|\n{1}'.format(\
        row_inner_string,\
        '|      |      |      |      |      |      |      |      |\n')

      row_strings.append(row_string)

    string = '{0}{1}{0}'.format(\
      line_divider,\
      line_divider.join(row_strings))

    return string

