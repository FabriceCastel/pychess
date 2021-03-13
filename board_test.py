from board import Board
from piece import Piece, PieceRank, PieceColor
from position import Position
from illegal_move_exception import IllegalMoveException
from piece_placement import PiecePlacement

import pytest

EMPTY_BOARD = \
    ("+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n")

def test_can_create_board():
  board = Board()
  assert True

def test_print_empty_board():
  board = Board()
  assert str(board) == EMPTY_BOARD

def test_add_piece_adds_a_black_knigh_to_a1():
  board = Board()
  piece = Piece(PieceRank.Knight, PieceColor.Black)
  position = Position(0, 0)
  board.add_piece(piece, position)
  assert str(board) == \
    ("+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "| b-k  |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n")

def test_add_piece_adds_two_pieces():
  board = Board()
  piece1 = Piece(PieceRank.King, PieceColor.Black)
  position1 = Position(3, 3)

  piece2 = Piece(PieceRank.Pawn, PieceColor.White)
  position2 = Position(1, 2)
  
  board.add_piece(piece1, position1)
  board.add_piece(piece2, position2)

  assert str(board) == \
    ("+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      | b-K  |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      | w-p  |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n")

def test_move_piece_moves_knight():
  board = Board()

  piece = Piece(PieceRank.Knight, PieceColor.Black)
  position = Position(0, 0)
  board.add_piece(piece, position)

  board.move_piece(position, Position(7, 7))

  assert str(board) == \
    ("+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      | b-k  |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n")

def test_move_piece_disallows_non_piece_moves():
  board = Board()
  with pytest.raises(IllegalMoveException):
    board.move_piece(Position(3, 4), Position(0, 0))


def test_move_piece_disallows_moving_to_same_space():
  board = Board()
  piece = Piece(PieceRank.Knight, PieceColor.Black)
  position = Position(3, 4)
  board.add_piece(piece, position)

  with pytest.raises(IllegalMoveException):
    board.move_piece(position, position)

def test_remove_piece_disallows_removing_no_piece():
  board = Board()
  position = Position(3, 4)

  with pytest.raises(IllegalMoveException):
    board.remove_piece(position)

def test_remove_piece_removes_piece():
  board = Board()
  piece = Piece(PieceRank.Knight, PieceColor.Black)
  position = Position(3, 4)
  board.add_piece(piece, position)

  board.remove_piece(position)

  assert str(board) == EMPTY_BOARD

def test_get_pieces():
  board = Board()
  piece = Piece(PieceRank.Knight, PieceColor.Black)
  position = Position(3, 4)
  board.add_piece(piece, position)

  assert board.get_pieces() == [PiecePlacement(piece, position)]

def test_setup_sets_up_board_properly():
  board = Board()
  board.setup()

  assert str(board) == \
    ("+------+------+------+------+------+------+------+------+\n"
     "| b-r  | b-k  | b-b  | b-Q  | b-K  | b-b  | b-k  | b-r  |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "| b-p  | b-p  | b-p  | b-p  | b-p  | b-p  | b-p  | b-p  |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "|      |      |      |      |      |      |      |      |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "| w-p  | w-p  | w-p  | w-p  | w-p  | w-p  | w-p  | w-p  |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n"
     "| w-r  | w-k  | w-b  | w-Q  | w-K  | w-b  | w-k  | w-r  |\n"
     "|      |      |      |      |      |      |      |      |\n"
     "+------+------+------+------+------+------+------+------+\n")
  