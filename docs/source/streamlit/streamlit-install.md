# インストールしたい（`streamlit`）

```console
// uv toolを使ってシステム全体にインストール
$ uv tool install streamlit

$ streamlit --version
Streamlit, version 1.56.0

$ which -a streamlit
/Users/shotakaha/.local/bin/streamlit

// uvを使ってプロジェクトに追加
$ uv add --group dev streamlit
```

Steamlitは`uv`でインストールできます。
インストールした後は、`streamlit`コマンドが使えるようになります。

## 実行したい

```console
$ streamlit run ファイル名
```

`streamlit`はコマンドでもあります。
`run`コマンドで、ローカルサーバーを起動し、ウェブアプリをライブ編集できます。

## インポートしたい

```console
import streamlit as st
```

ライブラリとして使う場合は`st`という名前で読み込むようです。
