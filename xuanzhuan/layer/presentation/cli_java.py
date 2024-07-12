import os
from xuanzhuan import create_concrete_from_params

# ここでアプリケーション層「UseCase」をしてのimport は避けた方が良い気がする「UseCase」
from xuanzhuan.layer.application.use_case import UseCase

pre = """
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Main {
    public static void main(String[] args) {
        // 正規表現パターンを定義
        String regexPattern = "^[0-9-]+$";

        // テストする文字列
        String inputString = "123-456-7890";

        // 正規表現のパターンをコンパイル
        Pattern pattern = Pattern.compile(regexPattern);

        // マッチャーを作成
        Matcher matcher = pattern.matcher(inputString);

        // マッチングを確認
        if (matcher.matches()) {
            System.out.println("入力文字列はハイフンと半角数字のみです。");
        } else {
            System.out.println("入力文字列にはハイフンと半角数字以外の文字が含まれています。");
        }
    }
"""

pro="""
}
"""

# CLIのプレゼンテーション層を作成する、といってもCLIなのでコマンドラインに機能を呼び出す関数を追加するだけ
# アプリケーション層のディレクトリからメソッドをスキャンする機能をつけてもいいかも。
class PresentationCliJava:
    def __init__(self, output_dir, project_name):
        self._project_name = project_name
        self.project_root = f'{output_dir}/{project_name}'
        self.use_case_list = list()
        os.makedirs(self.project_root, exist_ok=True)
        return
    def add_use_case(self, use_case: UseCase):
        self.use_case_list.append(use_case)
        return
    def file_out(self):
        file_name = f'{self.project_root}/Main.java'
        f = open(file_name, 'w', encoding='UTF8')
        f.write(pre)
        for u in self.use_case_list:
            f.write('// ' + u.description)
        f.write(pro)
        f.close()
        return