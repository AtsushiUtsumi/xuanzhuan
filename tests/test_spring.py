import os
import pytest

from xuanzhuan.cmd import show_spring
from xuanzhuan.layer.presentation.spring import PresentationSpring

def test_spring():
    show_spring()
    assert 1 == 1

def test_create_spring():
    spring: PresentationSpring = PresentationSpring(os.environ['OUTPUT_ROOT_PATH'], 'test', 'com.au')# Springアプリケーション出力
    table = dict()
    table["name"] = 'user'
    table["tableName"] = 'user'
    table["columnList"] = ['hoge','fuga']
    spring.add_table(table=table)
    return
