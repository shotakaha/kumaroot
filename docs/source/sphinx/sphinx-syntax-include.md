# インクルードしたい（``include``）

````md
```{include} 相対パス.md
```
````

``include``ディレクティブを使って、別ファイルの内容を埋め込むことができます。
ファイルは``Markdown``として読み込まれます。

:::{seealso}

reST形式だと次のようになります。

```rst
.. include:: 相対パス.md
   :parser: myst_parser.sphinx_
```

``.rst``ファイルで``.md``ファイルを読み込む場合は``:parser:``オプションを使います。

:::

## reSTファイルをインクルードしたい（``eval-rst``）

````md
```{eval-rst}
.. include:: 相対パス
```
````

``.md``ファイルに``.rst``ファイルを``include``するとMarkdown形式として認識されてしまうそうです。
``eval-rst``ディレクティブを使うと、``.rst``ファイルをreST形式で読み込むことができます。

## そのままインクルードしたい（``literalinclude``）

````md
```{literalinclude} 相対パス
language: python
emphasize-line: 10,15-20
linenos: true
```
````

``literalinclude``ディレクティブを使って、コードサンプルなどの外部のファイルを読み込んでそのまま表示できます。

## リファレンス

- [include - Docutils](https://docutils.sourceforge.io/docs/ref/rst/directives.html#include)
- [literalinclude - Sphinx document](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude)
- [Include rst files into a markdown file - MyST Parser](https://myst-parser.readthedocs.io/en/latest/faq/index.html#include-rst-files-into-a-markdown-file)
- [Include a file from outside the docs folder like readme.md - MyST Parser](https://myst-parser.readthedocs.io/en/latest/faq/index.html#include-a-file-from-outside-the-docs-folder-like-readme-md)
