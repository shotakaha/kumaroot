# 欧文クラスしたい（`classes`）

```latex
% classes
\documentclass[オプション]{article}
\documentclass[オプション]{report}
\documentclass[オプション]{book}
```

欧文の場合は、標準クラス（`article`、`report`、`book`）が用意されています。
記事や投稿論文のような短い文書の場合は`article`、
修士論文や博士論文などのように、ある程度の構成がある文書は`report`、
それらを製本したい場合は`book`が適しています。

国際会議のカスタムクラスも、この標準クラスを拡張したものが多い印象です。

## 日本語フォントしたい（`luatexja`）

```latex
\documentclass[オプション]{article}
\usepackage{luatexja}
```

[luatexjaパッケージ](./latex-luatexja.md)を使うと、
欧文クラスの中でも日本語（和文フォント）を出力できるようになります。
