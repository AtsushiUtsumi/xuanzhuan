import os

def show():
    load_hoge()
    print('__init__.pyがなかっただけ?')

def load_hoge():
    print(__path__[0] + '<- このパスを参照している(「pip install -e .」の「-e」の有無で変わるので注意)')
    input_file_name = __path__[0] + '/hoge.txt'
    input_file = open(input_file_name, 'r')
    for i in input_file.readlines():
        print(i)
    return

def get_template_file_path():
    print(__path__[0] + '<- このパスを参照している(「pip install -e .」の「-e」の有無で変わるので注意)')
    input_file_name = __path__[0][:-5] + '/templates/hoge.java.j2'
    return input_file_name

# テンプレートファイルパスとそのテンプレートファイルのレンダリングに必要なパラメータファイルのサンプルのパスのペアを返す
# サンプルファイルは出力するなり、レンダリングのサンプルに使うなり好きにすれば良いが、内蔵ファイル自体を書き換えられるのは避けたいので権限かパラメータはjsonで返した方がいいかもしれない
def get_file_path_pair():
    print(__path__[0] + '<- このパスを参照している(「pip install -e .」の「-e」の有無で変わるので注意)')
    template_file_path = __path__[0][:-5] + '/templates/entity.java.j2'
    params_file_path = __path__[0][:-5] + '/templates/entity.json'
    # TODO:両方の存在確認を行ってから返す
    return template_file_path, params_file_path