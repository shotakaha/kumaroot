# ロゴしたい（``html_logo``）

```python
html_log = None
html_logo = "ロゴ画像のパス"
```

``html_logo``でロゴ画像を設定できます。
設定したロゴは、サイドバーの上部に表示されます。
横幅は200px以下にするのがよいみたいです。

画像のパスは{file}`conf.py`からの相対パスを指定してください。
外部のURLを指定することもできます。

## ファビコンしたい（``html_favicon``）

```python
html_favicon = None
html_favicon = "ファビコン画像のパス.ico"
```

``html_favicon``でファビコン画像を設定できます。
設定したファビコンは、ブラウザのタブだったり、ブックマークだったりに表示されます。
画像は``16x16`` もしくは ``32x32`` の``.ico``形式で作成してください。

画像のパスは{file}``conf.py``からの相対パスを指定してください。
外部のURLを指定することもできます。
