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