# レイヤー毎の出力ディレクトリやフレームワーク情報、言語はインスタンス変数に持つと良いかも
# xz.create_spring()
# for i in Presentation(dir,framework='spring',params):
#   i.create_code(params[i])
# for i in Application(dir,lang='java',params):
#   i.create_code(params[i])
# for i in Domain(dir,lang='java', params):
#   i.create_code(params[i])
# for i in Repository(dir,lang='java', database='oracle',params):
#   i.create_code(params[i])
# こんな感じでアプリを書きたい

class Presentation:
    def __init__(self):
        pass
    def show(self):
        print('HOGE')
        return

class Application:
    def __init__(self):
        pass
    def show(self):
        print('アプリケーション層生成(出力ディレクトリはコンストラクタに渡してこのメソッドには個々に必要なパラメータを)')
        return

class Domain:
    def __init__(self):
        pass
    def show(self):
        print('HOGE')
        return