# 和文クラスしたい（`ltjsclasses`）

```latex
% ltjsclasses
\documentclass[オプション]{ltjsarticle}
\documentclass[オプション]{ltjsreport}
\documentclass[オプション]{ltjsbook}
```

`ltjsclasses`もLuaTeX-jaコミュニティが開発している和文クラスです。
後述する`jsclasses`クラスと高い互換性があるため、
昔からのLaTeXユーザーにはこのクラスが使いやすいと思います。

## 欧文スタイルしたい（`english`）

```latex
% プリアンブル
\documentclass[english]{ltjsreport}
```

`english`オプションで、欧文組みに変更できます。
見出し語が英語表記になったり、
目次のアキが欧文インデントになったり、
最初の段落の字頭インデントがなくなったり、します。

| コマンド | 和文 | `english` |
|---|---|---|
| `\tableofcontents` | 目次 | Contents |
| `\chapter` | 第1章 | Chapter 1 |
| `\section` | 1.1 | 1.1 |
| `\subsection` | 1.1.1 | 1.1.1 |

あまり使う場合はないかもしれません。
