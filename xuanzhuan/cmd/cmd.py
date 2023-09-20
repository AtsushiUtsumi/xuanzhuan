import subprocess

cmd = 'mvn -v'

result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
for i in result.stdout.split('\n'):
	# print('[' + i + ']')
	pass

def show_maven():
	"""
	このマシンにインストールされているMAVENバージョン情報
	を表示する
	"""
	print('このマシンにインストールされているMAVENバージョン情報:' + result.stdout.split('\n')[0])
