# 物理したい（`physics-patch`）

```latex
\usepackage{siunitx}
\usepackage[siintegrate]{physics-patch}
```

`physics-patch`は、Willie Shenさんが[physics](./latex-physics.md)パッケージを改良した派生版です。
`physics`を読み込まなくても使えます。
`physics`パッケージのコマンドをそのまま使えるようにしつつ、いくつかの機能を追加しています。

デフォルトでは、`physics`と同じ名前のコマンド（`\qty`、`\dv`、`\mqty`など）が`physics-patch`の定義に置き換わります。
改良されたコマンドは、`PT`（Physics Patch）という接頭辞を付けても使えます（例：`\PTqty`、`\PTdv`、`\PTmqty`）。

## 置き換えたい（`override` / `nooverride`）

```latex
\usepackage[override]{physics-patch}    % デフォルト
\usepackage[nooverride]{physics-patch}
```

`override`は、`physics`と同じ名前のコマンド（`\qty`、`\dv`、`\mqty`など）を`physics-patch`の定義に置き換えます。デフォルトの動作です。
`nooverride`は、同名のコマンドを置き換えません。`PT`接頭辞付きのコマンド（`\PTqty`など）だけを使います。

## 単位したい（`siintegrate` / `nosiintegrate`）

```latex
\usepackage{siunitx}
\usepackage[siintegrate]{physics-patch}    % 単位と統合
\usepackage[nosiintegrate]{physics-patch}  % デフォルト
```

`siintegrate`を指定すると、`\qty{5}{m}`（単位）と`\qty(x+y)`（括弧）を、同じ`\qty`で使い分けられます（パッケージのソースに基づく説明です）。
`nosiintegrate`は、`siunitx`の`\qty`と統合しません。デフォルトの動作です。

## 微分を斜体にしたい（`italicdiff` / `uprightdiff`）

```latex
\usepackage[italicdiff]{physics-patch}    % 斜体
\usepackage[uprightdiff]{physics-patch}   % 立体（デフォルト）
```

`italicdiff`は微分の`d`を斜体に、`uprightdiff`は立体にします。

## 一括指定したい（`forcedefault`）

```latex
\usepackage[forcedefault]{physics-patch}
```

`forcedefault`は、デフォルト値をまとめて指定します。
