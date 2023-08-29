from xuanzhuan import CaseConverter

def create_entity_and_bean(column_list):
    output = ''
    output += '// おそらく以下はEntityクラスに使用できる(型は書き換えること!)\n'
    for i in column_list:
        output += f'\t@Column=(name = "{CaseConverter(i).to_upper_snake_case()}")\n'
        output += f'\tprivate String {CaseConverter(i).to_lower_camel_case()};\n'
    output += '// おそらく以下はリスト表示項目の行クラスに使用できる\n'
    for i in column_list:
        output += f'\tprivate String {CaseConverter(i).to_lower_camel_case()};\n'
    return output