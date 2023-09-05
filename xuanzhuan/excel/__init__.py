from .docs import create_docs
from .docs import Docs

def readme():
    print('ここでマニュアルを出せばいいのでは')
    print('xuanzhuan内蔵の仕様書作成メソッド群です。出力する文字列の先頭docs.add(座標(0オリジン),"文字列")の形で入力することを目標にします座標とはシートオブジェクトなら行と列、行オブジェクトなら列番号、のように自身でセルを特定する座標')
    return