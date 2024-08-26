# hoge.txt を読み込んで、テキストの本文を表示するサンプルコード

# カレントディレクトリを取得・表示する
import os
print(os.getcwd())

# hoge.txt の場所を相対パスで設定
source = 'ML/popup.html'
# hoge.txt を読み込む
f = open(source, 'r', encoding='utf-8')
data = f.read()
f.close()
# hoge.txt の本文を表示
print(data)