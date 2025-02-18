# 用語集したい（`glossaries`）

```latex
\usepackage{glossaries}

\makeglossaries
\newglossaryentry{キー}{
    name={用語},
    description={用語の説明}
}

% 本文
\printglossaries
```

`glossaries`パッケージで用語集を作成できます。
用語集はプリアンブルで定義し、
本文中の`\printglossaries`の位置に出力できます。

[makeglossaries](./latex-makeglossaries.md)コマンドで
用語集をタイプセットできます。
