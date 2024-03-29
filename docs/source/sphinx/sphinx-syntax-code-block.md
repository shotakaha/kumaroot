# コードブロックしたい（``code-block``）

````md
```言語
コード
```
````

コードブロックはMarkdown記法の`` ```言語名 ``を使って挿入できます。


:::{seealso}

MySTを使っている場合コロンフェンス（``:::``）でディレクティブ宣言を代用できるオプションがあります。
コードの中にコードを書く場合など、入れ子になったディレクティブを記述する場合にとても便利です。

```python
# conf.py
myst_enable_extensions = [
    "colon_fence",
]

```

:::

## シンタックスハイライトしたい

```python
# conf.py
pygments_style = "sphinx"
```

シンタックスハイライトには``Pygments``というPythonモジュールが使われています。
``pygments_style``を使って色使いを変更できます。
デフォルトは``sphinx``になっています。

指定可能なプログラミング言語は[PygmentsのAvaileble lexers](https://pygments.org/docs/lexers/)で確認できます。
知らない言語もたくさん列挙されていて、眺めるだけでもおもしろいです。

## 行番号を表示したい（``linenos``）

````md
```{code-block} python
---
linenos: true
---
import pandas as pd
data = pd.read_csv("example.csv)
```
````

``linenos``オプションで、行番号を表示できます。
オプションを有効にする場合は``code-block``ディレクティブを使います。

:::{note}

``conf.py``で``myst_number_code_blocks = ["言語"]``を設定すると、ドキュメント全体を変更できます。

```python
myst_number_code_blocks = [
    "bash",
    "python",
    "dockerfile",
]
```

:::

:::{seealso}

reST形式で書くと次のようになります。

```rst
.. code-block: python
   :linenos:

   import pandas as pd
   data = pd.read_csv("example.csv")
```

:::

## 特定の行をハイライトしたい（``emphasize-lines``）

````md
```{code-block} python
---
emphasize-lines: 1,3,9-20
---
import pandas as pd
data = pd.read_csv("example.csv)
```
````

``emphasize-lines``オプションで、特定の行をハイライトできます。
複数行を飛び飛びで指定する場合は``,（カンマ）``で区切ります。
連続で指定する場合は``-（ハイフン）``で接続します。

## キャプションをつけたい（``caption``）

````md
```{code-block} python
---
caption: コードサンプルのキャプション
---
import pandas as pd
data = pd.read_csv("example.csv)
```
````

## コードを参照したい（``name``）

````md
```{code-block} python
---
name: ラベル名
---
import pandas as pd
data = pd.read_csv("example.csv)
```
````

## リファレンス

- [Source code and APIs - MyST Parser](https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html)
- [Available lexers - Pygments](https://pygments.org/docs/lexers/)
