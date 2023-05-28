# データテンプレートしたい（``sphinxcontrib.datatemplates``）

```console
$ pip3 install sphinxcontrib.datatemplates
```

```python
extensions = [
    "sphinxcontrib.datatemplates"
    ]
```

CSVなどのデータを、Jinjaテンプレート構文で表示できます。

## CSVを読み込みたい（``datatemplate:csv``）

```md
:::{datatemplate:csv} ファイル名
---
template: テンプレート名.tmpl
headers: true / false
dialect: auto / excel / excel-tab / unix
---

テンプレート構文

:::
```

CSVデータを表示するテンプレートは、ディレクティブの本文にJinja構文で定義します。

複数のCSVデータをそれぞれ読み込んで表示する場合、テンプレート構文を外部ファイルにすると便利です。
その場合、{file}`conf.py`で定義した``template_path``（デフォルトだと{file}`_templates`）にファイルを配置し、``template``オプションで外部ファイルを指定します。

``headers``オプションを使うと、データをリスト型で読み込むか、辞書型で読みこむか切り替えることができます。
デフォルトは``false``（＝リスト型）です。

``dialect``は``excel`` / ``excel-tab`` / ``unix``から選べます。
詳しくは、CSVを読み込む際に使っている[csvモジュール](https://docs.python.org/ja/3/library/csv.html)の[Dialectクラス](https://docs.python.org/ja/3/library/csv.html#csv.Dialect)を参照してください。
