# インストールしたい（``matplotlib``）

```console
$ pip3 install matplotlib
$ pip3 install japanize_matplotlib
```

```console
$ poetry add matplotlib
$ poetry add japanize_matplotlib
```

## バージョンを確認したい

```python
import matplotlib
print(f"matplotlib: {matploblib.__version__}")
```

```python
import matplotlib as mpl
print(f"matplotlib: {mpl.__version__}")
```

`matplotlib`本体をインポートする場合は、
`mpl`という名前を使ったりします。
