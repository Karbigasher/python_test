from app.first import SquareMinArea
import pytest


@pytest.mark.parametrize("test_input1, test_input2, expected_result", [
    ("1 1 3 6", "7 6 10 10", 81),
    ("1 8 6 10", "2 0 4 6", 100),
    ("1 1 5 3", "6 1 10 5", 81),
    ("1 5 3 7", "4 1 10 10", 81),
    ("1 1 2 3", "5 7 6 9", 64)

])
def test_positive(test_input1, test_input2, expected_result):
    assert SquareMinArea(test_input1, test_input2) is expected_result


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1/0 == 1


def test_invalid_input():
    with pytest.raises(ValueError):
        SquareMinArea("aaa a ", "2 2 2 2") == 64

# def test_positive():
#     assert SquareMinArea("1 1 3 6", "7 6 10 10") is 81, "Wrong answer"
#     assert SquareMinArea("1 8 6 10", "2 0 4 6") is 100, "Wrong answer"
#     assert SquareMinArea("1 1 5 3", "6 1 10 5") is 81, "Wrong answer"
#     assert SquareMinArea("1 5 3 7", "4 1 10 10") is 81, "Wrong answer"
#     assert SquareMinArea("1 1 2 3", "5 7 6 9") is 64, "Wrong answer"
