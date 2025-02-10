# シリーズしたい（`\textbf`）

```latex
{\mdseries ...} または \textmd{...}    % Medium（デフォルト）
{\bfseries ...} または \textbf{...}    % Boldface
{\bxseries ...} または \textbx{...}    % Bold Extended
{\ebseries ...} または \texteb{...}    % Extra Bold
{\ltseries ...} または \textlt{...}    % Light
```

**シリーズ**はフォントの線の太さのことです。
一般的にはウェイトと呼ぶことが多いと思います。
選択できるウェイトの数はフォントに依存します。

本文中で局所的にウェイトを切り替えることができます。

| シリーズ | コマンド形式 | 切り替え形式 | 数式 |
|---|---|---|---|
| Boldface | `\textbf{...}` | `\bfseries` | `\mathbf{...}` |
| Medium | `\textmd{...}` | `\mdseries` | |

フォントのウェイトは、名称ごとに100から900までの数値が割り当てられています。
日本語フォントではWからはじまる番号になっていることもあります。

| ウェイト | W番号 | 名称 |
|---|---|---|
| 100 | W1 | Thin / Hairline |
| 200 | W2 | Extra Light / Ultra Light |
| 300 | W3 | Light |
| 400 | W4 | Regular / Normal |
| 500 | W5 | Medium |
| 600 | W6 | Semi Bold / Demi Bold |
| 700 | W7 | Bold |
| 800 | W8 | Extra Bold / Ultra Bold |
| 900 | W9 | Black / Heavy |

## 太字したい（`\textbf`）

```latex
\textbf{太字}したい
{\bfseries 太字}したい
```

## 極太字したい（`\texteb`）

```latex
\texteb{極太字}したい
{\ebseries 極太字}したい
```

## 細字したい（`\textlt`）

```latex
\textlt{細字}したい
{\ltseries 細字}したい
```
