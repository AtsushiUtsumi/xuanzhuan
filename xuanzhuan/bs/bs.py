from bs4 import BeautifulSoup

html = """
<h3 class="ramen title" summary="メニュー">ラーメンメニュー</h3>
<ul>
  <li id="syouyu" class="ramen item">醤油ラーメン</li>
  <li id="tonkotsu" class="ramen item favorite">とんこつラーメン</li>
  <li id="miso" class="ramen item">味噌ラーメン</li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")

for i in soup.find_all('li'):
	print(i.text)

def show_men():
	print('HOGE')