# icecream

```bash
pip3 install icecream
```

```python
from icecream ic
```

デバッグ時に使う``print``の代替パッケージです。


## どこまで実行できたのかを確認したい

```python
ic()
```

デバッグの時のメッセージはきちんと書いたほうがいいのですが、
プログラムがどこでスタックしているのかを確認したいときは、
単に``print("近くの関数名")``などするほうが楽だったりします。

``ic()``を引数なしで書いておくと、その場所での
「ファイル名 / 行番号 / 関数名」を表示してくれるので、
このようなデバッグ確認には最適です。

## 表示／非表示を切り替えたい

```python
ic.enable()    # 有効にする
ic.disable()   # 無効にする
```

デバッグを終えたあとに、追加したデバッグメッセージを削除（もしくはコメントアウト）するのはとてもめんどくさいです。
ファイルの先頭に``ic.disable()``を追記すれば、一括で非表示にできます。

再度デバッグが必要な場合は、``#ic.disable()``もしくは、
確認したい場所に``ic.enable()``を追記すれば、表示できます。

## 表示形式を設定したい

```python
ic.configureOutput(prefix, outputFunction, argToStringFunction, includeContext)
```

``prefix``（デフォルト ``ic|``）
: 関数を指定できます

``outputFunction``（デフォルト ``stderr``）
: 出力先にロガーを指定できます

``includeContext``（デフォルト ``ファイル名 / 行番号 / 関数名``）
: 表示内容を指定できます
