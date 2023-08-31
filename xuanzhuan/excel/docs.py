
from openpyxl import Workbook
from openpyxl.styles import Alignment

# 新しいワークブックを作成
workbook = Workbook()
sheet = workbook.active

# セルに改行を含むテキストを設定
text_with_newline = "行1\n行2\n行3"
sheet['A1'] = text_with_newline

# セル内のテキストを中央揃えで改行
alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
sheet['A1'].alignment = alignment

# ワークブックを保存
workbook.save('cell_with_newline.xlsx')