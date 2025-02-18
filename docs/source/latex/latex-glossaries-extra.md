# 用語集したい（`glossaries-extra`）

```latex
\usepackage{glossaries-extra}

\setabbreviationstyle{long-short}

\makeglossaries

\newabbreviation{lhc}{LHC}{Large Hadron Collider}
\newglossaryentry{キー}{
    name={用語},
    description={用語の説明},
}

% 本文
\printglossaries
```

`glossaries-extra`は[glossariesパッケージ](./latex-glossaries.md)の拡張版です。
より簡単に用語や略語を扱うことができます。
