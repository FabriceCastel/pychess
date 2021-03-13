from piece import Piece, PieceRank, PieceColor

def test_piece_prints_properly():
  white_knight = Piece(PieceRank.Knight, PieceColor.White)
  assert str(white_knight) == 'w-k'