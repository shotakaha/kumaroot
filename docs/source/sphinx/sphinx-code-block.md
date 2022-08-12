# コードサンプルを表示したい

コードサンプルを表示したい場合は、
``code-block``ディレクティブを使います。

```rst
.. code-block:: python

   import pandas as pd
   data = pd.read_csv("example.csv)
```

## 行番号を表示したい（``:linenos:``）

```rst
.. code-block:: python
   :linenos:

   import pandas as pd
   data = pd.read_csv("example.csv)
```

## 特定の行をハイライトしたい（``:emphasize-lines:``）

```rst
.. code-block:: python
   :emphasize-lines: 1,3

   import pandas as pd
   data = pd.read_csv("example.csv)
```

## コードのキャプションをつけたい（``:caption:``）

```rst
.. code-block:: python
   :caption: コードサンプルのキャプション

   import pandas as pd
   data = pd.read_csv("example.csv)
```

## コードを参照したい（``:name:``）

```rst
.. code-block:: python
   :name: ラベル名

   import pandas as pd
   data = pd.read_csv("example.csv)
```
