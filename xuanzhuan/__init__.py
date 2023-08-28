# -*- coding: utf-8 -*-

__version__ = "7.7.7"

# 以下のモジュール名の前に「.」をつけるのが重要でした!
from .moga import *


import codecs
from jinja2 import Environment, FileSystemLoader, Template
import os
import json
import re

class CaseConverter:
    def __init__(self, word):
        self.word_list = list()

        # スネークケースの場合を先に処理する
        if '_' in word:
            self.word_list = [i.lower() for i in word.split('_')]
        else:
            word = re.sub('([A-Z])', '_\\1', word)
            if word[0] == '_':
                word = word[1:]
            if '_' in word:
                self.word_list = word.split('_')
            else:
                self.word_list.append(word.lower())
                pass
    def to_upper_snake_case(self):
        snake_case = '_'.join(self.word_list).upper()
        return snake_case
    def to_lower_snake_case(self):
        snake_case = '_'.join(self.word_list).lower()
        return snake_case
    def to_upper_camel_case(self):
        upper_camel_case_word = ''.join([i[0].upper() + i[1:] for i in self.word_list])
        return upper_camel_case_word
    def to_lower_camel_case(self):
        tmp = self.to_upper_camel_case()
        lower_camel_case_word = tmp[0].lower() + tmp[1:]
        return lower_camel_case_word
    def to_kebab_case(self):
        return self.to_lower_snake_case().replace('_', '-')

def to_lower_snake_case(param):
    return CaseConverter(param).to_lower_snake_case()
def to_upper_snake_case(param):
    return CaseConverter(param).to_upper_snake_case()
def to_lower_camel_case(param):
    return CaseConverter(param).to_lower_camel_case()
def to_upper_camel_case(param):
    return CaseConverter(param).to_upper_camel_case()

def create_concrete_from_params(template_file_name: str, params: dict, output_file_name: str):

    # テンプレートファイル読み込み
    if not os.path.isfile(template_file_name):
        print('テンプレートファイル[' + template_file_name + ']が見つかりませんでした')
    sep = template_file_name.rfind('/')
    dir = template_file_name[:sep]
    file_name = template_file_name[sep+1:]
    env = Environment(loader=FileSystemLoader(dir), trim_blocks=False)
    env.filters['to_lower_snake_case'] = to_lower_snake_case
    env.filters['to_upper_snake_case'] = to_upper_snake_case
    env.filters['to_lower_camel_case'] = to_lower_camel_case
    env.filters['to_upper_camel_case'] = to_upper_camel_case
    template = env.get_template(file_name)

    # 出力ファイル書き込み
    try:
        output_file = codecs.open(output_file_name, 'w', 'utf8')
        output_file.write(template.render(params))
        output_file.close()
        print('[' + output_file_name + ']を作成しました')
    except:
        print('ファイル[' + output_file_name + ']を作成できませんでした')
        pass
    return

def create_concrete_from_files(template_file_name: str, params_file_name: str, output_file_name: str):

    # パラメータファイル読み込み
    if not os.path.isfile(params_file_name):
        print('パラメータファイル[' + params_file_name + ']が見つかりませんでした')
        return
    params_file = codecs.open(params_file_name, 'r', 'utf8')
    params = json.load(params_file)
    params_file.close()
    create_concrete_from_params(template_file_name, params, output_file_name)
    return


print(CaseConverter('hoge_fuge').to_upper_snake_case())
print(CaseConverter('hoge_fuge').to_upper_camel_case())
print(CaseConverter('hoge_fuge').to_lower_snake_case())
print(CaseConverter('hoge_fuge').to_lower_camel_case())
print(CaseConverter('hoge_fuge').to_kebab_case())

print(CaseConverter('HOGE_FUGA').to_upper_snake_case())
print(CaseConverter('HOGE_FUGA').to_upper_camel_case())
print(CaseConverter('HOGE_FUGA').to_lower_snake_case())
print(CaseConverter('HOGE_FUGA').to_lower_camel_case())
print(CaseConverter('HOGE_FUGA').to_kebab_case())

print(CaseConverter('HOGE_FUGA').to_upper_snake_case())
print(CaseConverter('HOGE_FUGA').to_upper_camel_case())
print(CaseConverter('HOGE_FUGA').to_lower_snake_case())
print(CaseConverter('HOGE_FUGA').to_lower_camel_case())
print(CaseConverter('HOGE_FUGA').to_kebab_case())


# 今はhogeみたいな適当な名前だが、基本的なテンプレートをXuanZhuanに統合したい