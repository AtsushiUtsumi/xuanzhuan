# -*- coding: utf-8 -*-

def readme():
    print('コードやドキュメントを生成するツールを書くためのライブラリ的な立ち位置です')
    print('このメソッドが「xuanzhuan.readme()」で実行できるのは直下の「__init__.py」に定義しているからです')
    print('それはそうと、ここにREADMEを書くのはありなのか...')
    return

__version__ = "7.7.7"

__templates_dir__ = __path__[0] + '\\templates'

from .core import CaseConverter
from .core import to_lower_camel_case
from .core import to_lower_snake_case
from .core import to_upper_camel_case
from .core import to_upper_snake_case
from .core import create_concrete_from_files
from .core import create_concrete_from_params
from .core import create_files_from_dir# これで直接アクセスできる
from .layer.presentation.spring import PresentationSpring
