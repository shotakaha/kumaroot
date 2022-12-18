# OGPを設定したい（``sphinxext-opengraph``）

```python
extensions = [
    ...,
    "sphinxext.opengraph",
    ...
]
```

SphinxJPハッカソンに参加して教えてもらった拡張パッケージです。
設定ファイルに追記するだけで、HTML中に``og:title``、``og:type``、``og:url``、``og:site_name``、``og:description``が追記されます（他にもメタ要素が追加されているかも）。

このサイトの場合、以下の情報が追記されました。
``og:description``はきちんと設定したほうがよさそうなので、変更します。

```html
<meta property="og:title" content="KumaROOT" />
<meta property="og:type" content="website" />
<meta property="og:url" content="index.html" />
<meta property="og:site_name" content="KumaROOT" />
<meta property="og:description" content="はじめに, ROOTの使い方, Geant4の使い方, コマンドラインの使い方, Gitの使い方, LaTeXの使い方, Sphinxの使い方, Pythonの使い方, Pandasの使い方, Altairの使い方, Goole Apps Script の使い方, ウェブ開発, Hugoの使い方, VS Codeの使い方, Emacsの使い方, Rustの使い方, Docker の使い方, ..." />
<meta name="description" content="はじめに, ROOTの使い方, Geant4の使い方, コマンドラインの使い方, Gitの使い方, LaTeXの使い方, Sphinxの使い方, Pythonの使い方, Pandasの使い方, Altairの使い方, Goole Apps Script の使い方, ウェブ開発, Hugoの使い方, VS Codeの使い方, Emacsの使い方, Rustの使い方, Docker の使い方, ..." />
```

## サイト設定を変更したい




## リファレンス

- https://pypi.org/project/sphinxext-opengraph/
- https://sphinx-users.jp/cookbook/ogp/index.html
