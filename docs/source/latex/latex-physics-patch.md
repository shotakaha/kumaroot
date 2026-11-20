# 物理したい（`physics-patch`）

```latex
\usepackage{siunitx}
\usepackage[siintegrate]{physics-patch}
```

`physics-patch`は、Willie Shenさんが[physics](./latex-physics.md)パッケージを改良した派生版です。
`physics`を読み込まなくても使えます。
`physics`パッケージのコマンドをそのまま使えるようにしつつ、いくつかの機能を追加しています。

既定では、`physics`と同じ名前のコマンド（`\qty`、`\dv`、`\mqty`など）が`physics-patch`の定義に置き換わります。
改良されたコマンドは、`PT`（Physics Patch）という接頭辞を付けても使えます（例：`\PTqty`、`\PTdv`、`\PTmqty`）。

## オプション

| オプション | 説明 |
|---|---|
| `override` / `nooverride` | 同名のコマンドを置き換える／置き換えない（既定は`override`） |
| `siintegrate` / `nosiintegrate` | `siunitx`の`\qty`と統合する／しない（既定は`nosiintegrate`） |
| `italicdiff` / `uprightdiff` | 微分の`d`を斜体／立体にする（既定は`uprightdiff`） |
| `forcedefault` | 既定値をまとめて指定する |

`siintegrate`を指定すると、`\qty{5}{m}`（単位）と`\qty(x+y)`（括弧）を、同じ`\qty`で使い分けられます（パッケージのソースに基づく説明です）。
