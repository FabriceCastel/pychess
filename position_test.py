from position import Position
import pytest
from illegal_position_exception import IllegalPositionException

def test_invalid_row_throws_exception():
  with pytest.raises(IllegalPositionException):
    position = Position(1, 10)

def test_invalid_column_throws_exception():
  with pytest.raises(IllegalPositionException):
    position = Position(10, 1)

def test_valid_piece_can_be_created():
  position = Position(2, 2)
  assert position.column == 2
  assert position.row == 2

def test_stringify_a1():
  assert str(Position(0, 0)) == 'A1'

def test_stringify_c5():
  assert str(Position(2, 4)) == 'C5'