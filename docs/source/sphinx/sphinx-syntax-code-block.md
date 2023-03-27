# コードサンプルしたい（``code-block``）

````md
```{code-block} python
---
linenos: true
emphasize-lines: 1, 3
caption: コードサンプルのキャプション
name: ラベル名
---
import pandas as pd
data = pd.read_csv("example.csv)
```
````

プログラムのコードサンプルを挿入し、シンタックスハイライトできます。
ハイライトには``Pygments``とうPythonモジュールが使われています。
利用可能なプログラミング言語は[PygmentsのAvaileble lexers](https://pygments.org/docs/lexers/)で確認できます。

```{note}
通常のMarkdown記法でコードブロックを挿入することもできます。
行番号の表示など、オプションを使いたい場合はディレクティブ形式のMySTを使う必要があります。
```

:::{seealso}
reST形式で書くと次のようになります。

```rst
.. code-block:: python

    :linenos:
    :empphasize-lines: 1,3
    :caption: コードサンプルのキャプション
    :name: ラベル名

   import pandas as pd
   data = pd.read_csv("example.csv)
```
:::

## 行番号を表示したい（``linenos:``）

```md
:::{code-block} python
---
linenos: true
---
import pandas as pd
data = pd.read_csv("example.csv)
:::
```

## 特定の行をハイライトしたい（``:emphasize-lines:``）

```md
:::{code-block} python
---
emphasize-lines: 1,3
---
import pandas as pd
data = pd.read_csv("example.csv)
:::
```

## キャプションをつけたい（``caption:``）

```md
:::{code-block} python
---
:caption: コードサンプルのキャプション
---
import pandas as pd
data = pd.read_csv("example.csv)
:::
```

## コードを参照したい（``name:``）

```md
:::{code-block} python
---
name: ラベル名
---
import pandas as pd
data = pd.read_csv("example.csv)
:::
```

## リファレンス

- [Source code and APIs - MyST Parser](https://myst-parser.readthedocs.io/en/latest/syntax/code_and_apis.html)
- [Available lexers - Pygments](https://pygments.org/docs/lexers/)
