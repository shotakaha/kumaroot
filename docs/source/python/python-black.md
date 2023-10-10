# フォーマッタしたい（``black``）

```bash
$ pip3 install black
$ pip3 install "black[jupyter]"
```

PEP8に準拠したフォーマッタです。
Pythonのフォーマッタにもいろいろありますが、``black``は**初期設定不要**なことが特徴です。
インストールしてすぐに使うことができるので便利です。

Jupyter Notebookもフォーマット対象にする場合は、``black[jupyter]``のオプションをつけてインストールします。

## フォーマットを確認したい

```bash
$ black --check .
```

## 自動フォーマットしたい

```bash
$ black .
```

## フォーマット対象から除外したい

```python
skip_line = True # fmt: skip

# fmt: off
def skip_block():
    pass
# fmt: on
```

フォーマット対象から除外したいコードを部分的に指定できます。
``# fmt:skip``を行末に追加すると、その1行をスキップできます。
``# fmt:off``と``# fmt:on``で挟まれた部分は、そのブロックごとスキップできます。
