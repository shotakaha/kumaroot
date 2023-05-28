```{eval-rst}
.. index::
    pair: Sphinx; toc
```

# 目次したい（``toctree``）

````md
```{toctree}
---
maxdepth: 1
caption: 目次のキャプション
name: ラベル名
---
ファイル名1
ファイル名2
ファイル名3
```
````

ドキュメントの目次を自動生成するには、``toctree``ディレクティブを使います。

:::{seealso}
reST形式で書くと次のようになります。

```rest
.. toctree::
   :maxdepth: 1
   :caption: 目次のキャプション
   :name: ラベル名
   :numbered:

   ファイル名1
   ファイル名2
   ファイル名3
```
:::

## 目次の深さを設定したい（``maxdepth:``）

ファイルの中にある見出しを表示する**深さ**を設定できます。
このドキュメントのように、ファイルを小さな単位に分割して
管理している場合は ``maxdepth: 1``に設定するとよいと思います。

````md
```{toctree}
---
maxdepth: 1
---
ファイル名1
ファイル名2
ファイル名3
```
````

## 目次にキャプションをつけたい（``caption:``）

````md
```{toctree}
---
caption: 目次のキャプション
---
ファイル名1
ファイル名2
ファイル名3
```
````

## 目次を参照したい（``name:``）

````md
```{toctree}
---
name: ラベル名
---
ファイル名1
ファイル名2
ファイル名3
```
````

## 章番号を表示したい（``numbered:``）

````md
```{toctree}
---
numbered:
---
ファイル名1
ファイル名2
ファイル名3
```
````

HTMLドキュメントでも章番号を表示したい場合は、``numbered:``オプションを指定します。

## リファレンス

- [toctree - Sphinx Documentation](https://www.sphinx-doc.org/ja/master/usage/restructuredtext/directives.html#directive-toctree)
- [toctree - MyST Parser Documentation](https://myst-parser.readthedocs.io/en/latest/syntax/organising_content.html#using-toctree-to-include-other-documents-as-children)
