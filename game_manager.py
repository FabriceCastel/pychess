from board import Board
from piece import Piece, PieceRank, PieceColor
from move import Move
from typing import List, Set
from position import Position

class GameManager:
  def __init__(self):
    self._board = Board()
    self._board.setup()

  def get_active_player(self) -> PieceColor:
    return PieceColor.White

  def set_board(self, board: Board) -> None:
    self._board = board

  def get_board(self) -> Board:
    return self._board

  # Get all of the valid moves for the player whose turn
  # it is, for all of their pieces.
  def get_valid_moves(self) -> Set[Move]:
    active_color = self.get_active_player()
    all_pieces = self._board.get_pieces()

    active_player_pieces = filter(\
      lambda piece_placement: piece_placement.piece.color == active_color,\
      all_pieces)

    valid_moves = set()
    for piece_placement in active_player_pieces:
      piece = piece_placement.piece
      position = piece_placement.position
      rank = piece.rank

      if (rank == PieceRank.Pawn):
        for target_position in self._get_pawn_moves(self._board, active_color, position):
          valid_moves.add(Move(position, target_position))

    return valid_moves

  def _get_pawn_moves(self, board: Board, color: PieceColor, position: Position) -> List[Position]:
    moves = []

    if (color == PieceColor.White):
      # If no one is blocking the way forward, move up 1
      one_up_is_valid = board.get_piece(position.up()) == None

      # If it hasn't moved yet and isn't blocked, move up 2
      two_up_is_valid = position.row == 1\
        and one_up_is_open\
        and board.get_piece(position.up().up()) == None

      diag_left_is_valid = position.column > 0\
        and board.get_piece(position.up().left()) != None\
        and board.get_piece(position.up().left()).color == PieceColor.Black

      diag_right_is_valid = position.column < 7\
        and board.get_piece(position.up().right()) != None\
        and board.get_piece(position.up().right()).color == PieceColor.Black

      if (one_up_is_valid):
        moves.append(position.up())

      if (two_up_is_valid):
        moves.append(position.up().up())

      if (diag_left_is_valid):
        moves.append(position.up().left())

      if (diag_right_is_valid):
        moves.append(position.up().right())
    else:
      pass

    return moves
