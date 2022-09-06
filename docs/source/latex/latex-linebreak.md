# 改行・改ページしたい（``\linebreak``）

改行や改ページは基本的にLaTeXにお任せで問題ありません。
しかし、時には、強制的に調整した場合があります。
そのような時は``\linebreak``や``\pagebreak``を使います。
また、その逆の効果がある``\nolinebreak``と``\nopagebreak``もあります。

## 改行したい

```tex
\linebreak
```

## 改行したくない

```tex
\nolinebreak
```

## 改ページしたい

```tex
\pagebreak
\clearpage
```

## 改ページしたくない

```tex
\nopagebreak
\samepage
```
