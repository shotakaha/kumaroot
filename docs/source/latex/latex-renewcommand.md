# コマンドを再定義したい（`\renewcommand`）

```latex
\renewcommand{\既存のコマンド名}[引数の数]{やりたいこと}
```

`\renewcommand`で、既存のコマンドを再定義できます。
存在しないコマンド名に対して使うと**未定義エラー**が出力されます。

## 目次したい

```latex
\renewcommand{\contentsname}{目次}
```

`\contentsname`は、目次の見出しの文字列を表すコマンドです。
`article`や`book`クラスで定義されていて、言語によって自動的に翻訳されます。
`\renewcommand`で書き換えると、目次の見出しが「目次」に変わります。

## 安全に再定義したい（`\providecommand`）

```latex
\providecommand{\コマンド名}{}
\renewcommand{\コマンド名}[引数の数]{やりたいこと}
```

`\providecommand`は、コマンドが未定義がどうかの確認に利用できます。
コマンドが定義済みの場合は何もせず、未定義の場合は定義します。
この挙動を利用して`\renewcommand`の前に置くことで、未定義エラーを回避できます。
`\newcommand`との違いは[\newcommand](./latex-newcommand.md)を参照してください。
