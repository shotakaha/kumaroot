# コマンドを再定義したい（``\renewcommand``）

```latex
\renewcommand{\既存のコマンド名}[引数の数]{やりたいこと}
```

`\renewcommand`で、既存のコマンドを再定義できます。
存在しないコマンド名に対して使うと**未定義エラー**が出力されます。

```latex
\providecommand{\コマンド名}{}
\renewcommand{\コマンド名}[引数の数]{やりたいこと}
```

`\providecommand`と合わせて使うと、未定義デラーを回避できます。
