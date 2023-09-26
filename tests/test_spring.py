import pytest

from xuanzhuan.cmd import show_spring

def test_spring():
    show_spring()
    assert 1 == 1