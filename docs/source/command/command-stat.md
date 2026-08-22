# ファイル情報したい（`stat`）

```console
$ stat ファイル名
$ stat -f "%N %z %m" ファイル名
$ stat -t "%Y-%m-%d %H:%M:%S" ファイル名
```

`stat`は、ファイルの情報を表示するコマンドです。
`-f`で、出力フォーマットを指定できます。
`-t`で、タイムスタンプのフォーマットを指定できます。

:::{seealso}

- [](./command-ls.md)
- [](./command-lsd.md)
- [](./command-du.md)

:::
