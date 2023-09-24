# リンターしたい（``ruff``）

```console
$ pip3 install ruff
```

Rustで書かれたPython用のリンターです。

## 確認したい

```console
$ ruff check .
```

確認したいファイル／ディレクトリで``ruff check``を実行します。
修正したほうがよい箇所がターミナルに出力されます。

スキップしたいエラーなどは設定ファイル（``pyproject.toml``）で除外できます。
