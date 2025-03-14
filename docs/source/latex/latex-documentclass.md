# ドキュメントクラスしたい（`\documentclass`）

```latex
\documentclass[オプション]{クラス名}
```

**ドキュメントクラス** は文書全体の構成やスタイルを決めるテンプレート的なものです。
LaTeXの文書作成は、まず、このドキュメントクラス選びからはじまります。
目的や使用する言語に応じて、適切なクラスを選択してください。
また、学会や雑誌によっては専用のクラスを用意している場合もあります。

```{toctree}
latex-classes
latex-jlreq
latex-ltjsclasses
latex-jsclasses
latex-documentclass-beamer
```

和文の場合は、歴史的な経緯からいくつかの選択肢があります。
ただし、新しく書きはじめる場合は`jlreq`クラスを利用すればOKです。



## クラス早見表したい

| 機能 | `article` | `report` | `book` |
|---|---|---|---|
| 用途 | 記事／論文 | 技術書／修論 | 教科書／博論 |
| 印刷面 | 片面（`oneside`） | 片面（`oneside`） | 両面（`twoside`） |
| 目次の深さ | 小節まで | 小節まで | （カスタム） |
| 最上位の見出し | 節（`\section`） | 章（`\chapter`） | 章（`\chapter`） |
| 章の開始 | 連続 | 新ページ | 新ページ |
| ページ番号 | 連番（アラビア数字） | 連番（アラビア数字） | 前付（ローマ数字）／本文（アラビア数字） |
| 図表の番号 | 連番（図1、表1） | 章ごと（図1.1、表1.1） | 章ごと（図1.1、表1.1） |
| ヘッダー／フッター | なし／ページ番号 | （章名）／ページ番号 | 章名・節名／ページ番号 |
| 前付／後付 | 非対応 | （カスタム） | `\frontmatter` / `\mainmatter` / `\backmatter` |
| 索引サポート | なし | なし | あり |
| `jlreq` | （デフォルト） | `[report]` | `[book]` |
| `ltjsclasses` | `ltjsarticle` | `ltjsreport` | `ltjsbook` |
| `jsclasses` | `jsarticle` | `jsreport` | `jsbook` |

機能別の早見表を作成しました。
クラス選びの参考にしてください。
