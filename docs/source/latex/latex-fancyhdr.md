# ヘッダー／フッターを設定したい（``fancyhdr``）

```latex
\usepackage[オプション]{fancyhdr}
\pagestyle{fancy}
\lhead{ヘッダー・左}
\chead{ヘッダー・中央}
\rhead{ヘッダー・右}
\lfoot{フッター・左}
\cfoot{フッター・中央}
\rfoot{フッター・右}
```

文書の柱（ヘッダーやフッター）をいい感じに装飾するパッケージです。
読み込む順番に気をつける必要があります。

## 現在のページに設定したい

```latex
\thispagestyle{fancy}
\lhead{ヘッダー・左}
\chead{ヘッダー・中央}
\rhead{ヘッダー・右}
\lfoot{フッター・左}
\cfoot{フッター・中央}
\rfoot{フッター・右}
```

現在のページに設定する場合は``\thispagestyle``コマンドを使います。
改ページ（``\newpage``）でリセットされます。

## リファレンス

- {command}`texdoc fancyhdr`
