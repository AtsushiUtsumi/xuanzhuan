import pytest

from xuanzhuan.utils import list_dot

def test_リストの総当たり作成():
    source = [['A', 'B'],['C', 'D'],['E', 'F']]
    result = list_dot(source)
    prediction = [['A', 'C', 'E'], ['B', 'C', 'E'], ['A', 'D', 'E'], ['B', 'D', 'E'], ['A', 'C', 'F'], ['B', 'C', 'F'], ['A', 'D', 'F'], ['B', 'D', 'F']]
    assert result == prediction