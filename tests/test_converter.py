import pytest

from xuanzhuan import CaseConverter
from xuanzhuan import to_lower_camel_case# VSCodeはたどれる
from xuanzhuan import to_lower_snake_case# VSCodeはたどれない、けどimportは出来てる

@pytest.mark.parametrize(
    "x, y", [
        #("aaa", "bbb"),
        ("aaa", "aaa"),
        ("bbb", "bbb")
    ]
)
def test_1(x, y):
    assert x == y

@pytest.mark.parametrize(
    "x, y, z", [
        (0, 1, 3),(0, 1, 5)
    ]
)
def test_2(x, y, z):
    assert x * y * z== 0

@pytest.mark.parametrize(
    "before, after", [
        ('hoge_fuga', 'HOGE_FUGA'),# lowerスネークから
        ('HOGE_FUGA', 'HOGE_FUGA'),# upperスネークから
        ('hogeFuga', 'HOGE_FUGA'),# lowerキャメルから
        ('HogeFuga', 'HOGE_FUGA'),# upperキャメルから
        ('hoge', 'HOGE'),
        ('Hoge', 'HOGE'),
        #('_Hoge', ''),# 問題はこういう場合
    ]
)
def test_アッパースネークケースへの変換(before, after):
    assert CaseConverter(before).to_upper_snake_case() == after

def test_スネークフィルター():
    assert to_lower_snake_case('HOGE_HOGE') == 'hoge_hoge'

def test_キャメルフィルター():
    assert to_lower_camel_case('HOGE_HOGE') == 'hogeHoge'