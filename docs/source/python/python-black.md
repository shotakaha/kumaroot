# フォーマッタしたい（`black`）

```console
$ black .
```

`black`はPEP8準拠したフォーマッタです。
**初期設定不要**なことが特徴で、インストールしてすぐに使うことができます。

:::{note}

Pythonのフォーマッターはいろいろありますが、
それぞれ初期設定が必要で初心者にはとっつきにくい面がありました。
2018年に登場した`black`は「フォーマッターを導入してみようかな」という
気持ちにさせてくれるツールでした。

:::

## インストールしたい（`black`）

```console
$ pip3 install black
$ pip3 install "black[jupyter]"
```

Jupyter Notebookもフォーマット対象にしたい場合は
``black[jupyter]``のオプションをつけてインストールします。

## フォーマットしたい

```console
$ black .
```

カレントディレクトリの下にある対象ファイルを修正します。

## フォーマットを確認したい

```console
$ black --check .
```

`--check`オプションで、修正が必要なファイルがあるかを確認します。

## 部分的に除外したい（`fmt: skip` / `fmt: on` / `fmt: off`）

```python
skip_line = True # fmt: skip

# fmt: off
def skip_block():
    pass
# fmt: on
```

``# fmt:skip``を行末に追加すると、その1行をスキップできます。
``# fmt:off``と``# fmt:on``で囲むと、ブロックごとスキップできます。

`black`は細かな設定ができませんが、このようにして
**部分的に除外**できるようになっています。

