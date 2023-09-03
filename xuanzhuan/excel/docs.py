from openpyxl import Workbook
from openpyxl.styles import Alignment

def create_docs(docs_name: str):
    """
    仕様書のエクセルファイルを出力します

    Args:
        docs_name (string): 出力するファイルの名前(拡張子無し)
    """

    # 新しいワークブックを作成
    workbook = Workbook()
    sheet = workbook.active

    # セルに改行を含むテキストを設定
    text_with_newline = "行1\n行2\n行3"
    sheet["A1"] = text_with_newline

    # セル内のテキストを中央揃えで改行
    alignment = Alignment(wrap_text=True, vertical="top", horizontal="left")
    sheet["A1"].alignment = alignment

    # ワークブックを保存
    workbook.save(f'{docs_name}.xlsx')
    return
