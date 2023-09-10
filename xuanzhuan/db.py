import sqlite3
from xuanzhuan import CaseConverter

def create_entity_and_bean(column_list):
    output = ''
    output += '// おそらく以下はEntityクラスに使用できる(型は書き換えること!)\n'
    for i in column_list:
        output += f'\t@Column(name = "{CaseConverter(i).to_upper_snake_case()}")\n'
        output += f'\tprivate String {CaseConverter(i).to_lower_camel_case()};\n\n'
    output += '// おそらく以下はリスト表示項目の行クラスに使用できる\n'
    for i in column_list:
        output += f'\tprivate String {CaseConverter(i).to_lower_camel_case()};\n'
    return output

def read(query: str):
    ret = list()
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    rs = c.execute(query)
    for i in rs:
        ret.append(i)
    conn.close()
    return ret

def write(query: str):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    conn.close()
    return

# サンプルデータ作成メソッド

def create_ll_from_sample_dict(params: dict[str, str]) -> list[list[str]]:
    query = ''
    ll = list()
    for column_name, sample_value_list in params.items():
        tmp = list()
        for sample_value in sample_value_list:
            tmp.append(f'{column_name}={sample_value}')
        ll.append(tmp)
    return ll

# 亜種だけど、こっちの方が使いやすそう
# 「カラム名:サンプル値のリスト」の辞書型を受け取り、総当たりを返す
def create_ld_from_sample_dict(params: dict[str, str]) -> list[dict[str,str]]:
    ret = list()
    ll = create_ll_from_sample_dict(params)
    ll = list_dot(ll)
    print('以下の通り')
    print(ll)
    for l in ll:
        tmp = dict()
        for s in l:
            tmp[s.split('=')[0]] = s.split('=')[1]
        ret.append(tmp)
    return ret

from .utils.list_dot import list_dot

def create_insert_sample_query(table_name: str, params: dict[str, str]) -> list[str]:
    ret = []
    ll = list_dot(create_ll_from_sample_dict(params))
    for i in ll:
        ret.append('INSERT ' + str(i))
    return ret


def query_create_table(table_name: str, columns: dict[str, str]):# 「カラム名: 型」の辞書
    tmp = []
    for n, t in columns.items():
        tmp.append(f"{n} {t}")
    s = ', '.join(tmp)
    query = f'CREATE TABLE IF NOT EXISTS {table_name} ({s})'
    return query

def execute_create_table(table_name: str, columns: dict[str, str]):# 「カラム名: 型」の辞書
    query = query_create_table(table_name, columns)
    print('以下のクエリを実行します\n' + query)
    write(query)
    return

def query_drop_table(table_name: str):
    query = f'DROP TABLE IF EXISTS {table_name}'
    return query

def execute_drop_table(table_name: str):
    query = query_drop_table(table_name)
    write(query)
    return

def query_insert(table_name: str, record: dict[str, str]):# 「カラム名: 値」の辞書
    columns = ', '.join(record.keys())
    values = ', '.join(["'" + i + "'" for i in record.values()])
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values});"
    return query

def execute_insert(table_name: str, columns: dict[str, str]):# 「カラム名: 値」の辞書
    query = query_insert(table_name, columns)
    write(query)
    return