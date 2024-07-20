import os
import subprocess
import xuanzhuan as xz

from xuanzhuan import create_concrete_from_params
def create_spring():
	cmd = 'spring --version'
	result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
	print('このマシンにインストールされているSPRINGバージョン情報:' + result.stdout.split('\n')[0])
	return
class Presentation:
    def __init__(self):
        pass
    def show(self):
        print('HOGE')
        return
class PresentationSpring(Presentation):
    def __init__(self, output_dir, project_name, package_root: str):
        os.makedirs(output_dir, exist_ok=True)
        self._project_name = project_name
        self._package_root = package_root
        package_path = self._package_root.replace('.', '/')
        self.project_root = f'{output_dir}/{project_name}'
        self.repository_root = f'{self.project_root}/src/main/java/{package_path}/{project_name}/domain'
        self.dao_root = f'{self.project_root}/src/main/java/{package_path}/{project_name}/dao'
        self.entity_root = f'{self.project_root}/src/main/java/{package_path}/{project_name}/entity'
        self.service_root = f'{self.project_root}/src/main/java/{package_path}/{project_name}/service'
        self.service_test_root = f'{self.project_root}/src/test/java/{package_path}/{project_name}/service'
        self.controller_root = f'{self.project_root}/src/main/java/{package_path}/{project_name}/controller'
        self.controller_test_root = f'{self.project_root}/src/test/java/{package_path}/{project_name}/controller'
        self.form_root = f'{self.project_root}/src/main/java/{package_path}/{project_name}/controller'
        self.templates_root = f'{self.project_root}/src/main/resources/templates'
        # cmd = '(cd ' + output_dir + ') && (spring init -d=web,thymeleaf,postgresql,data-jpa,lombok --type gradle-project --build=gradle -n=' + project_name + ' ' + project_name + ')'
        # いったんMavenプロジェクトに変更
        cmd = '(cd ' + output_dir + f') && (spring init --groupId={self._package_root} -d=web,thymeleaf,lombok,h2,data-jpa --build=maven -n=' + project_name + ' ' + project_name + ')'
        # 各種ディレクトリ作成
        subprocess.run(cmd, shell=True, capture_output=True, text=True)
        os.makedirs(self.form_root, exist_ok=True)
        os.makedirs(self.controller_root, exist_ok=True)
        os.makedirs(self.service_root, exist_ok=True)
        os.makedirs(self.repository_root, exist_ok=True)
        os.makedirs(self.dao_root, exist_ok=True)
        os.makedirs(self.entity_root, exist_ok=True)
        subprocess.run(f'(cd {self.project_root}) && (git init) && (git add --all) && (git commit -m プロジェクト作成)', shell=True, capture_output=True, text=True)
        return

    def add_screen(self, screen_name):
        # HTML,Form,Contorllerの追加
        # こういうのは「sugumi」に入れた方が良いんじゃないか
        upper_camel = xz.CaseConverter(screen_name).to_upper_camel_case()
        lower_camel = xz.CaseConverter(screen_name).to_lower_camel_case()
        controller_file_name = f'{self.controller_root}/{upper_camel}Controller.java'
        form_file_name = f'{self.controller_root}/{upper_camel}Form.java'
        package = f'{self._package_root}.{self._project_name}.controller'
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
        list_html_file_name = f'{self.templates_root}/{lower_camel}/{lower_camel}List.html'
        register_html_file_name = f'{self.templates_root}/{lower_camel}/{lower_camel}Register.html'
        edit_html_file_name = f'{self.templates_root}/{lower_camel}/{lower_camel}Edit.html'
        # javaファイル名設定(「パッケージルート + パッケージをスラッシュ区切りにしたもの + クラス名 + .java」のほうがよさそう)
        list_controller_file_name = f'{self.controller_root}/{lower_camel}/{upper_camel}ListController.java'
        list_controller_test_file_name = f'{self.controller_root}/{lower_camel}/{upper_camel}ListControllerTest.java'# TODO: 一覧画面のテストクラスはまた今度
        detail_controller_file_name = f'{self.controller_root}/{lower_camel}/{upper_camel}DetailController.java'
        detail_controller_test_file_name = f'{self.controller_test_root}/{lower_camel}/{upper_camel}DetailControllerTest.java'
        service_file_name = f'{self.service_root}/{lower_camel}/{upper_camel}Service.java'
        service_test_file_name = f'{self.service_test_root}/{lower_camel}/{upper_camel}ServiceTest.java'
        list_form_file_name = f'{self.controller_root}/{lower_camel}/{upper_camel}ListForm.java'
        list_row_file_name = f'{self.controller_root}/{lower_camel}/{upper_camel}ListRow.java'
        detail_form_file_name = f'{self.controller_root}/{lower_camel}/{upper_camel}DetailForm.java'
        detail_row_file_name = f'{self.controller_root}/{lower_camel}/{upper_camel}DetailRow.java'
        # entity_file_name = f'{self.entity_root}/{lower_camel}/{upper_camel}.java'
        # repository_file_name = f'{self.repository_root}/{lower_camel}/{upper_camel}Repository.java'
        # いったんDAO使うパターンで作成する
        crud_entity_file_name = f'{self.dao_root}/crud/{lower_camel}/{upper_camel}.java'
        crud_dao_file_name = f'{self.dao_root}/crud/{lower_camel}/{upper_camel}Dao.java'
        search_entity_file_name = f'{self.dao_root}/search/{lower_camel}/{upper_camel}FindEntity.java'
        search_dao_file_name = f'{self.dao_root}/search/{lower_camel}/{upper_camel}FindDao.java'

        package_root = f'{self._package_root}.{self._project_name}'
        # importするときどのパッケージのどのクラスをimportするかを登録しておく(「UserRepository」といえば「com.example.domain.repository.UserRepository」をimportすれば良い)
        import_dict = dict()
        import_dict[f'{upper_camel}'] = f'{self._package_root}.{self._project_name}.dao.crud.{lower_camel}.{upper_camel}'
        import_dict[f'{upper_camel}Dao'] = f'{self._package_root}.{self._project_name}.dao.crud.{lower_camel}.{upper_camel}Dao'
        import_dict[f'{upper_camel}Service'] = f'{self._package_root}.{self._project_name}.service.{lower_camel}.{upper_camel}Service'

        # HTML
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/list.html.j2', {'table': table}, list_html_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/register.html.j2', {'table': table}, register_html_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/edit.html.j2', {'table': table}, edit_html_file_name)
        # Formクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/ListForm.java.j2', {'table': table, 'package': package_root+'.controller.' + lower_camel}, list_form_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/ListRow.java.j2', {'table': table, 'package': package_root+'.controller.' + lower_camel}, list_row_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/DetailForm.java.j2', {'table': table, 'package': package_root+'.controller.' + lower_camel}, detail_form_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/DetailRow.java.j2', {'table': table, 'package': package_root+'.controller.' + lower_camel}, detail_row_file_name)
        # Controllerクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/ListController.java.j2', {'table': table, 'package': package_root+'.controller.' + lower_camel, 'import_dict': import_dict}, list_controller_file_name)
        # TODO: 一覧画面のテストクラスはまた今度
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/DetailController.java.j2', {'table': table, 'package': package_root+'.controller.' + lower_camel, 'import_dict': import_dict}, detail_controller_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/DetailControllerTest.java.j2', {'table': table, 'package': package_root+'.controller.' + lower_camel, 'import_dict': import_dict}, detail_controller_test_file_name)
        # Serviceクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/Service.java.j2', {'table': table, 'package': package_root+'.service.' + lower_camel, 'import_dict': import_dict}, service_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/ServiceTest.java.j2', {'table': table, 'package': package_root+'.service.' + lower_camel, 'import_dict': import_dict}, service_test_file_name)
        # Repositoryクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/CrudEntity.java.j2', {'table': table, 'package': package_root+'.dao.crud.' + lower_camel}, crud_entity_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/CrudDao.java.j2', {'table': table, 'package': package_root+'.dao.crud.' + lower_camel}, crud_dao_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/SearchEntity.java.j2', {'table': table, 'package': package_root+'.dao.search.' + lower_camel}, search_entity_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/SearchDao.java.j2', {'table': table, 'package': package_root+'.dao.search.' + lower_camel}, search_dao_file_name)
        # クエリ
        # xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_table/query.sql.j2', {'table': table}, f'{self.templates_root}/{lower_camel}.sql')
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
        package_root = f'{self._package_root}.{self._project_name}'
        # Serviceクラス
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/Service.java.j2', {'table': table, 'package': package_root+'.service'}, service_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/ServiceCommand.java.j2', {'table': table, 'package': package_root+'.service'}, command_file_name)
        xz.create_concrete_from_params(f'{xz.__templates_dir__}/add_use_case/ServiceTest.java.j2', {'table': table, 'package': package_root+'.service'}, test_file_name)
        # Gitでコミット
        # subprocess.run(f'(cd {self.project_root}) && (git add --all) && (git commit -m "add {table} table")', shell=True, capture_output=True, text=True)
        return