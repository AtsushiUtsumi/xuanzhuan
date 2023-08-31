from openpyxl import Workbook

# 新しいワークブックを作成
workbook = Workbook()
sheet = workbook.active

# セルに値を設定
sheet['A1'] = '結合されるセルA1'
sheet['B1'] = '結合されないセルB1'
sheet['A2'] = '結合されるセルA2'
sheet['B2'] = '結合されないセルB2'

# セルを結合
sheet.merge_cells('A1:A2')

# ワークブックを保存
workbook.save('merged_cells.xlsx')