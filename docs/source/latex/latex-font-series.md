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
