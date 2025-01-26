# 文献リストしたい（`.bib`）

```bibtex
@種類{引用キー,
  フィールド = {値},
}
```

文献リストは、BibLaTeX形式（`.bib`）のテキスト情報として管理します。
フィールドは、文献の種類によって変わりますが、
文字列は`{}`もしくは`""`で囲む必要があります。
また、LaTeXで解釈される特殊文字（`%`、`$`、`_`、`&`など）はエスケープが必要です。

```bibtex
@inproceedings{takahashi_rapporteur_2024,
  author = {Takahashi, Shota},
  booktitle = {Proceedings of 38th International Cosmic Ray Conference — {PoS}({ICRC2023})},
  date = {2024-07-29},
  doi = {10.22323/1.444.0038},
  eventtitle = {38th International Cosmic Ray Conference},
  langid = {english},
  location = {Nagoya, Japan},
  pages = {038},
  publisher = {Sissa Medialab},
  title = {The rapporteur report on the diversity session at the ICRC2023},
  url = {https://pos.sissa.it/444/038},
  urldate = {2025-01-26},
}
```

このサンプルは`Zotero`という文献管理ツールから出力したものです。
BibLaTeXファイルは手動でも作成できますが、
文献管理ツールを使うのがよいと思います。

## 文献の形式

同じ`.bib`ファイルにも**BibTeX形式**と**BibLaTeX形式**の2種類があります。

BibTeX形式は1985年に開発され、長い間使われてきた形式です。
古いプロジェクトや既存のスタイルを利用する場合には、
こちらの形式がよいです。

BibLaTeX形式は新しい形式です。
`biblatex`パッケージと`biber`コマンドで文献リストを生成します。
BibTeX形式に比べてより多くのフィールドがサポートされています。
また、フィールドの追加・変更も可能で、カスタム拡張性が高くなっています。

BibLaTeX形式は、BibTeX形式と互換性があるので、
新しいプロジェクトではBibLaTeX形式を採用するとよいと思います。

:::{note}

BibLaTeXは、BibTeX形式に最適化された古いスタイルファイルとの互換性はありません。

:::

## 文献の種類

| 文献の種類 | 説明 |
|---|---|
| `article` | 学術雑誌に掲載された論文 |
| `book` | 書籍 |
| `booklet` | 小冊子 |
| `inbook` | 書籍の一部 |
| `proceedings` | プロシーディングス（の全体）|
| `inproceedings` | プロシーディングスの一部 |
| `manual` | 操作マニュアル |
| `masterthesis` | 修士論文 |
| `phdthesis` | 博士論文 |
| `misc` | 分類が難しい論文 |
| `unpublished` | 未発表の論文 |

利用可能な文献の種類の一部をリストしました。
自分で考えると迷うこともあるので、
公開されている文献に関しては、文献管理ツール自動分類してもらうと楽ちんです。

## 文献のフィールド

| フィールド名 | 説明 |
|---|---|
| `address` | 出版社や機関の所在地 |
| `annote` | 注釈 |
| `author` | 著者名 |
| `booktitle` | 書籍や会議録のタイトル |
| `chapter` | 書籍の特定の章番号 |
| `edition` | 書籍の版数 |
| `editor` | 編集者名 |
| `howpublished` | 公開方法 |
| `institution` | 発行機関名 |
| `journal` | 学術雑誌の名前 |
| `key` | 文献の参照用キー |
| `month` | 発行月 |
| `number` | 号数 |
| `note` | 文献に関するメモ |
| `organization` | 主催／後援の団体名 |
| `pages` | ページ番号または範囲 |
| `publisher` | 出版社名 |
| `school` | 学位論文を発行した大学名 |
| `series` | 雑誌や書籍のシリーズ名 |
| `title` | 文献のタイトル |
| `type` | 文献の種類 |
| `volume` | 巻号 |
| `year` | 発行年 |
| `abstract` | 文献の概要 |
| `doi` | DOI識別子 |
| `isbn` | 書籍のISBN番号 |
| `issn` | 雑誌のISSN番号 |
| `url` | 文献のURL |
| `eprint` | プレプリントの識別子 |
| `language` | 文献の言語 |

## 学術雑誌したい（`article`）

```bibtex
@article{引用キー,
  // 必須
  author = {著者名},
  title = {タイトル},
  journal = {ジャーナル名},
  year = {発行年},
  // オプション
  volume = {巻号},
  number = {号数},
  pages = {ページ範囲},
  doi = {DOI番号},
}
```

## プロシーディングスしたい（`inproceedings`）

```bibtex
@inproceedings{引用キー,
  author = {著者名},
  title = {タイトル},
  booktitle = {会議名},
  year = {発行年},
  pages = {ページ範囲},
  publisher = {出版社},
}
```

## 書籍したい（`book`）

```bibtex
@book{引用キー,
  author = {著者名},
  title = {書籍タイトル},
  publisher = {出版社},
  year = {発行年},
  month = {発行月},
  edition = {版数},
  volume = {巻号},
  series = {シリーズ名},
  address = {出版社の所在地},
  doi = {DOI識別子}
}
```
