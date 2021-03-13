from piece import PieceColor, Piece, PieceRank
from game_manager import GameManager
from board import Board
from position import Position
from move import Move

A3 = Position(0, 4)
A4 = Position(0, 5)
B4 = Position(1, 5)

def test_white_player_goes_first():
  manager = GameManager()
  assert manager.get_active_player() == PieceColor.White

def test_sets_up_game_board():
  manager = GameManager()

  assert str(manager.get_board()) == \
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

def test_get_valid_moves_simple_a3_pawn():
  manager = GameManager()
  board = Board()
  piece = Piece(PieceRank.Pawn, PieceColor.White)
  board.add_piece(piece, A3)
  manager.set_board(board)

  assert manager.get_valid_moves() == {Move(A3, A4)}

def test_get_valid_moves_simple_a3_pawn():
  manager = GameManager()
  board = Board()
  board.add_piece(Piece(PieceRank.Pawn, PieceColor.White), A3)
  board.add_piece(Piece(PieceRank.Knight, PieceColor.Black), B4)
  manager.set_board(board)

  assert manager.get_valid_moves() == {Move(A3, A4), Move(A3, B4)}
