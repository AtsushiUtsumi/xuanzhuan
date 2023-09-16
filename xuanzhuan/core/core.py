# -*- coding: utf-8 -*-

import codecs
from jinja2 import Environment, FileSystemLoader#, Template
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
def to_lower_camel_case(param: str) -> str:
    """
    与えられた文字列をローワーキャメルケースに変換して返します

    Args:
        param (string): 変換前の文字列
    """
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

def create_files_from_dir(input_dir: str, output_dir: str):
    """
    与えられたディレクトリ内をスキャンして出力ディレクトリに複数のファイルを出力
    パラメータファイル「json」ファイル(必ず1つ)
    テンプレートファイル「j2」ファイル(1つ以上)
    を入力ディレクトリ内に入れておく必要がある
    Args:
        input_dir (stirng): 入力ディレクトリ
        output_dir (stirng): 出力ディレクトリ
    """
    files = os.listdir(input_dir)
    print(files)
    template_file_path_list = []
    json_file_path = ''
    for i in files:
        path = f'{input_dir}/{i}'
        if path.endswith('.j2'):
            template_file_path_list.append(path)
        elif path.endswith('.json'):
            json_file_path = path
    for t in template_file_path_list:
        create_concrete_from_files(t, json_file_path, t.rstrip('.j2').replace(input_dir, output_dir))
    return