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
        self.repository_root = f'{self.project_root}/src/main/java/com/example/{project_name}/domain'
        self.entity_root = f'{self.project_root}/src/main/java/com/example/{project_name}/entity'
        self.service_root = f'{self.project_root}/src/main/java/com/example/{project_name}/service'
        self.service_root = f'{self.project_root}/src/test/java/com/example/{project_name}/service'
        self.controller_root = f'{self.project_root}/src/main/java/com/example/{project_name}/controller'
        self.form_root = f'{self.project_root}/src/main/java/com/example/{project_name}/form'
        self.templates_root = f'{self.project_root}/src/main/resources/templates'
        cmd = '(cd ' + output_dir + ') && (spring init -d=web,thymeleaf,postgresql,data-jpa,lombok --type gradle-project --build=gradle -n=' + project_name + ' ' + project_name + ')'
        # 各種ディレクトリ作成
        subprocess.run(cmd, shell=True, capture_output=True, text=True)
        os.mkdir(self.form_root)
        os.mkdir(self.controller_root)
        os.mkdir(self.service_root)
        os.mkdir(self.repository_root)
        os.mkdir(self.entity_root)
        #subprocess.run(f'(cd {self.project_root}) && (git init) && (git add --all) && (git commit -m プロジェクト作成)', shell=True, capture_output=True, text=True)
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
        #subprocess.run(f'(cd {self.project_root}) && (git add --all) && (git commit -m {screen_name}画面作成)', shell=True, capture_output=True, text=True)
        return

    def add_table(self, table):
        # Entity,Repository,生成クエリの追加
        # こういうのは「sugumi」に入れた方が良いんじゃないか
        upper_camel = xz.CaseConverter(table.get('name')).to_upper_camel_case()
        lower_camel = xz.CaseConverter(table.get('name')).to_lower_camel_case()

        # htmlファイル名前設定
        list_html_file_name = f'{self.templates_root}/{lower_camel}List.html'
        register_html_file_name = f'{self.templates_root}/{lower_camel}Register.html'
        edit_html_file_name = f'{self.templates_root}/{lower_camel}Edit.html'
        # javaファイル名設定
        controller_file_name = f'{self.controller_root}/{upper_camel}Controller.java'
        service_file_name = f'{self.service_root}/{upper_camel}Service.java'
        list_form_file_name = f'{self.controller_root}/{upper_camel}ListForm.java'
        detail_form_file_name = f'{self.controller_root}/{upper_camel}DetailForm.java'
        entity_file_name = f'{self.entity_root}/{upper_camel}.java'
        repository_file_name = f'{self.repository_root}/{upper_camel}Repository.java'

        package_root = f'com.example.{self._project_name}'
        # HTML
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/list.html.j2', {'table': table}, list_html_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/register.html.j2', {'table': table}, register_html_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/edit.html.j2', {'table': table}, edit_html_file_name)
        # Formクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/ListForm.java.j2', {'table': table, 'package': package_root+'.controller'}, list_form_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/DetailForm.java.j2', {'table': table, 'package': package_root+'.controller'}, detail_form_file_name)
        # Controllerクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/Controller.java.j2', {'table': table, 'package': package_root+'.controller'}, controller_file_name)
        # Serviceクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/Service.java.j2', {'table': table, 'package': package_root+'.service'}, service_file_name)
        # Repositoryクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/Entity.java.j2', {'table': table, 'package': package_root+'.entity'}, entity_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/Repository.java.j2', {'table': table, 'package': package_root+'.domain'}, repository_file_name)
        # クエリ
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/query.sql.j2', {'table': table}, f'{self.templates_root}/{lower_camel}.sql')
        #subprocess.run(f'(cd {self.project_root}) && (git add --all) && (git commit -m {table}テーブル作成)', shell=True, capture_output=True, text=True)
        return
    
    def add_use_case(self, table):
        # 「ユーザーを登録する」みたいな責務を持ったクラスを生成する
        # テストケースはサンプル
        # アプリケーションサービスクラス、コマンドクラス、テストクラスの追加
        upper_camel = xz.CaseConverter(table.get('name')).to_upper_camel_case()
        # javaファイル名設定
        service_file_name = f'{self.service_root}/{upper_camel}ApplicationService.java'
        command_file_name = f'{self.service_root}/{upper_camel}ServiceCommand.java'
        test_file_name = f'{self.service_root}/{upper_camel}ServiceTest.java'
        package_root = f'com.example.{self._project_name}'
        # Serviceクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/Service.java.j2', {'table': table, 'package': package_root+'.service'}, service_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/ServiceCommand.java.j2', {'table': table, 'package': package_root+'.service'}, command_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/ServiceTest.java.j2', {'table': table, 'package': package_root+'.service'}, test_file_name)
        subprocess.run(f'(cd {self.project_root}) && (git add --all) && (git commit -m "add {table} table")', shell=True, capture_output=True, text=True)
        return