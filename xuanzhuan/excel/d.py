from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Side

# 新しいワークブックを作成
workbook = Workbook()
sheet = workbook.active

header_data = ['項目', '説明', '備考', '優先度']
sheet.append(header_data)
for i in range(5):
    for j in range(10):
        sheet.cell(row=i+2, column=j+1,value=f'{i}{j}')

# ワークブックを保存
workbook.save('セルにインデックスでアクセス.xlsx')
