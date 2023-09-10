from .db import create_entity_and_bean
from .db import create_ld_from_sample_dict
from .db import query_drop_table
from .db import query_create_table
from .db import query_insert

# 以下のメソッドは不要かもしれない
# 「コードを作成するスクリプトを作りやすくするためのライブラリ」という位置づけとしては、
# 以下のようなクエリを実行する機能をつけてしまうのはライブラリとしてオーバーな気がする。
# せめて実行部分をそれ専用に切り出して「テスト環境を構築するためのライブラリ」としたほうが良さげ
from .db import read
from .db import write

from .db import execute_drop_table
from .db import execute_create_table
from .db import execute_insert