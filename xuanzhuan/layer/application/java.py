# このモジュール自体もアプリケーションサービス
# 主に「アプリケーションとしての機能クラス」「コマンドクラス」「テストクラス」
# 同時にpythonでプロジェクトを組み立てることができるように列挙型の定数ファイルを生成
import os
import subprocess
import xuanzhuan as xz

from pathlib import Path
from xuanzhuan.layer.layer import Application
from xuanzhuan import create_concrete_from_params
from xuanzhuan.layer.application.use_case import UseCase

class ApplicationJava(Application):
    def __init__(self, project_name: str, application_root: Path, application_test_root: Path):
        application_root.mkdir(parents=True, exist_ok=True)
        print(application_test_root)
        application_test_root.mkdir(parents=True, exist_ok=True)
        self.service_root = str(application_root)
        self.service_test_root = str(application_test_root)
        self._project_name = project_name


    def add_use_case(self, use_case: UseCase):
        # 「ユーザーを登録する」みたいな責務を持ったクラスを生成する
        # テストケースはサンプル
        # アプリケーションサービスクラス、コマンドクラス、テストクラスの追加
        upper_camel = xz.CaseConverter(use_case.function_name).to_upper_camel_case()
        # javaファイル名設定
        service_file_name = f'{self.service_root}/{upper_camel}Service.java'
        command_file_name = f'{self.service_root}/{upper_camel}Command.java'
        test_file_name = f'{self.service_test_root}/{upper_camel}ServiceTest.java'
        package_root = f'com.example.{self._project_name}'
        # Serviceクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/Service.java.j2', {'use_case': use_case, 'package': self._project_name}, service_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/ServiceCommand.java.j2', {'package': self._project_name}, command_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/ServiceTest.java.j2', {'package': self._project_name, 'use_case': use_case}, test_file_name)
        # subprocess.run(f'(cd {self.project_root}) && (git add --all) && (git commit -m "add {table} table")', shell=True, capture_output=True, text=True)
        # 明日にでも使えるようにしたい
        return