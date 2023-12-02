# リンターしたい（``ruff``）

```console
$ pip3 install ruff
```

Rustで書かれたPython用のリンター&フォーマッタです。

## リンターしたい

```console
$ ruff check パス
```

確認したいファイル／ディレクトリで``ruff check``を実行します。
修正したほうがよい箇所がターミナルに出力されます。

スキップしたいエラーなどは設定ファイル（``pyproject.toml``）で除外できます。

## フォーマッタしたい

```console
$ ruff format パス
```
