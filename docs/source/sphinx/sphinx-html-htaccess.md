# .htaccessしたい（``html_static_path``）

```python
html_static_path = [
    "_static",
    "_static/.htaccess"
]
```

``.htaccess``を使いたい場合は、``html_static_path``に直接追加してください。
``html_static_path``の中のドットファイルは、セキュリティの関係でビルド先にコピーされないため、直接記述する必要があります。
もしくは次項で紹介する``html_extra_path``に記述します。

## .htaccessしたい（``html_extra_path``）

```python
html_static_path = ["_static"]
html_extra_path = [".htaccess", "robots.txt"]
```

``html_extra_path``を使って、ドキュメントに直接含まれない``.htaccess``や``robots.txt``のようなファイルをHTML出力に追加できます。
パスは{file}`conf.py`からの相対パスで指定します。
出力先に同じ名前のファイルがある場合、上書きします。
