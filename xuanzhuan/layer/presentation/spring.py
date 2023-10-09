import os
import subprocess
import xuanzhuan as xz

from xuanzhuan.layer.layer import Presentation
from xuanzhuan import create_concrete_from_params
def create_spring():
	cmd = 'spring --version'
	result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
	print('このマシンにインストールされているSPRINGバージョン情報:' + result.stdout.split('\n')[0])
	return

class PresentationSpring(Presentation):
    def __init__(self, output_dir, project_name):
        self._project_name = project_name
        self.project_root = f'{output_dir}/{project_name}'
        self.controller_root = f'{self.project_root}/src/main/java/com/example/{project_name}/controller'
        self.templates_root = f'{self.project_root}/src/main/resources/templates'
        cmd = '(cd ' + output_dir + ') && (spring init -d=web,thymeleaf,postgresql,data-jpa --type gradle-project --build=gradle -n=' + project_name + ' ' + project_name + ')'
        # 各種ディレクトリ作成
        subprocess.run(cmd, shell=True, capture_output=True, text=True)
        os.mkdir(self.controller_root)
        subprocess.run(f'(cd {self.project_root}) && (git init) && (git add --all) && (git commit -m プロジェクト作成)', shell=True, capture_output=True, text=True)
        return

    def add_screen(self, screen_name):
        # HTML,Form,Contorllerの追加
        # こういうのは「sugumi」に入れた方が良いんじゃないか
        upper_camel = xz.CaseConverter(screen_name).to_upper_camel_case()
        lower_camel = xz.CaseConverter(screen_name).to_lower_camel_case()
        controller_file_name = f'{self.controller_root}/{upper_camel}Controller.java'
        form_file_name = f'{self.controller_root}/{upper_camel}Form.java'
        package = f'com.example.{self._project_name}.controller'
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/Controller.java.j2', {'name': screen_name, 'package': package}, controller_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/Form.java.j2', {'name': screen_name, 'package': package}, form_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/list.html.j2', {'name': screen_name}, f'{self.templates_root}/{lower_camel}List.html')
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/detail.html.j2', {'name': screen_name}, f'{self.templates_root}/{lower_camel}Detail.html')
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/edit.html.j2', {'name': screen_name}, f'{self.templates_root}/{lower_camel}Edit.html')
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/register.html.j2', {'name': screen_name}, f'{self.templates_root}/{lower_camel}Register.html')
        subprocess.run(f'(cd {self.project_root}) && (git add --all) && (git commit -m {screen_name}画面作成)', shell=True, capture_output=True, text=True)
        return

    def add_table(self, table):
        # Entity,Repository,生成クエリの追加
        # こういうのは「sugumi」に入れた方が良いんじゃないか
        upper_camel = xz.CaseConverter(table).to_upper_camel_case()
        lower_camel = xz.CaseConverter(table).to_lower_camel_case()
        controller_file_name = f'{self.controller_root}/{upper_camel}Entity.java'
        form_file_name = f'{self.controller_root}/{upper_camel}Repository.java'
        package = f'com.example.{self._project_name}.controller'
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/Entity.java.j2', {'table': table, 'package': package}, controller_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/Repository.java.j2', {'table': table, 'package': package}, form_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/query.sql.j2', {'table': table}, f'{self.templates_root}/{lower_camel}.sql')
        subprocess.run(f'(cd {self.project_root}) && (git add --all) && (git commit -m {table}テーブル作成)', shell=True, capture_output=True, text=True)
        return