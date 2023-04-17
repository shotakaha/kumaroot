# コピーボタンしたい（``sphinx-copybutton``）

```console
$ pip3 install sphinx-copybutton
```

```python
extensions = [
    ...
    "sphinx-copybutton",
    ...
]
```

[sphinx-copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/index.html)を使うと、コードブロックの右上端にコピーボタンを設置できます。
{file}`conf.py`の``extensions``にパッケージ名を追加するだけなので、導入しておきましょう。
