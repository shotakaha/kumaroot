# ドキュメントクラスしたい（`\documentclass`）

```latex
\documentclass[オプション]{クラス名}
```

**ドキュメントクラス** は文書全体の構成やスタイルを決めるテンプレート的なものです。
LaTeXの文書作成は、まず、このドキュメントクラス選びからはじまります。
目的や使用する言語に応じて、適切なクラスを選択してください。
また、学会や雑誌によっては専用のクラスを用意している場合もあります。

## クラスオプションしたい

`jlreq`と`ltjsclasses`を中心に、目的別にクラスオプションを整理しました。

```{toctree}
---
maxdepth: 1
---
latex-documentclass-paper
latex-documentclass-fontsize
latex-documentclass-twocolumn
latex-documentclass-landscape
latex-documentclass-hanging
latex-documentclass-tate
latex-documentclass-twoside
```

## 欧文クラスしたい

```latex
% classes
\documentclass[オプション]{article}
\documentclass[オプション]{report}
\documentclass[オプション]{book}
```

欧文の場合は、標準クラス（`article`、`report`、`book`）でOKです。
日報のような短い文書の場合は`article`、
修士論文や博士論文などのように、ある程度の構成がある文書は`report`、
それらを製本したい場合は`book`が適しています。

国際会議のカスタムクラスも、これらを拡張したものが多い印象です。

```{toctree}
latex-classes
```

## 和文クラスしたい

和文の場合は、歴史的な経緯からいくつかの選択肢があります。
ただし、新しく書きはじめる場合は`jlreq`クラスを利用すればOKです。

```latex
% jlreq
\documentclass{jlreq}
\documentclass[report]{jlreq}
\documentclass[book]{jlreq}
```

`jlreq`はLuaTeX-jaコミュニティが開発している和文クラスです。
W3Cワーキンググループで議論されている「[日本語組版処理の要件](https://www.w3.org/TR/jlreq/)」の実装を試しているクラスです。

美文書LaTeXも第9版からこのクラスに移行したそうなので、
これからの日本語標準クラスといってよいと思います。
これから作成する文書は、迷わず`jlreq`でよいと思います。

```{toctree}
---
maxdepth: 1
---
latex-jlreq
```

```latex
% ltjsclasses
\documentclass[オプション]{ltjsarticle}
\documentclass[オプション]{ltjsreport}
\documentclass[オプション]{ltjsbook}
```

`ltjsclasses`もLuaTeX-jaコミュニティが開発している和文クラスです。
後述する`jsclasses`クラスと高い互換性があるため、
昔からのLaTeXユーザーにはこのクラスが使いやすいと思います。

```latex
% jsclasses
\documentclass[uplatex, dvipdfmx]{jsarticle}
\documentclass[uplatex, dvipdfmx]{jsreport}
\documentclass[uplatex, dvipdfmx]{jsbook}
```

`jsclasses`は三重大の奥村さんが作成した和文クラスです。
(u)pLaTeXを利用するときにお世話になるクラスです。
オプションにエンジン（`uplatex`）とドライバー（`dvipdfmx`）は必須です。
また、他に追加したほうがよいパッケージもいくつかあります。

ウェブ検索したときに、まだまだ多数ヒットする情報だと思うので、知っておくとよいです。

:::{note}

``(u)pLaTeX + jsclasses系``のサンプルも、わかる範囲で載せておきます。

:::

```{toctree}
---
maxdepth: 1
---
latex-jsclasses
```

## 早見表したい

| 機能 | `article` | `report` | `book` |
|---|---|---|---|
| 用途 | 記事／論文 | 技術書／修論 | 教科書／博論 |
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
