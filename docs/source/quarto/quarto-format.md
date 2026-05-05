# 出力形式したい（`format`）

```yaml
format:
  html:
    theme: cosmo
    toc: true
    number-sections: true
    mainfont: "Noto Sans JP"
    monofont: "Noto Mono"
    include-in-header: |
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP&family=Noto+Mono&display=swap">
  typst:
    papersize: a4
    number-sections: true
    mainfont: "Hiragino Sans"
    # include-before-body: templates/preamble.typ
  pdf:
    pdf-engine: lualatex
    toc: true
    number-sections: true
    documentclass: jsarticle
    # include-in-header: templates/preamble.tex
  docx:
    toc: true
    number-sections: true
    # reference-doc: templates/reference.docx
  revealjs:
    theme: solarized
    slide-number: true
    chalkboard: false
    incremental: false
    transition: fade
    controls: true
    progress: true
    center: false
    scrollable: true
    width: 1920
    height: 1080
```

`format`フィールドで出力形式ごとのオプションを指定できます。
`_quarto.yml`ファイルでグローバル設定、個々の`.qmd`ファイルのフロントマターでローカル設定できます。

## HTML形式したい（`format: html`）

```yaml
format: html
  title: "ドキュメントのタイトル"
  subtitle: "ドキュメントのサブタイトル"
  date: 2026-04-19
  date-modified: last-modified
  author: "著者"
  abstract: "ドキュメントの概要"
  # doi: "10.1234/5678"
  theme: cosmo
  tabsets: true
  smooth-scroll: true
  html-math-method: katex
  # mainfont: "Noto Sans JP"
  # monofont: "Noto Mono"
  # keywords:
  # copyright: "Copyright (c) 2026 著者"
```

:::{seealso}

- [Reference > Formats > HTML](https://quarto.org/docs/reference/formats/html.html)

:::

## Typst形式したい（`format: typst`）

```yaml
format: typst
  title: "ドキュメントのタイトル"
  author: "著者"
  date: 2026-04-19
  keep-typ: true
```

:::{seealso}

- [Reference > Formats > Typst](https://quarto.org/docs/reference/formats/typst.html)

:::

## スライド形式したい（`format: revealjs`）

```yaml
format: revealjs
  title: "プレゼンテーションのタイトル"
  subtitle: "プレゼンテーションのサブタイトル"
  date: 2026-04-19
  author: "著者"
  institute: "所属"
  theme: solarized
  # logo: "logo.png"
  # footer: "フッターのテキスト"
  scrollable: true
```

:::{seealso}

- [Reference > Formats > Presentations > Reveal.js](https://quarto.org/docs/reference/formats/presentations/revealjs.html)

:::

## スライド形式したい（`format: pptx`）

```yaml
format: pptx
  title: "プレゼンテーションのタイトル"
  date: 2026-04-19
  author: "著者"
```

:::{seealso}

- [Reference > Formats > Presentations > PowerPoint](https://quarto.org/docs/reference/formats/presentations/pptx.html)

:::

## ドキュメント形式したい（`format: docx`）

```yaml
format: docx
  title: "ドキュメントのタイトル"
  subtitle: "ドキュメントのサブタイトル"
  date: 2026-04-19
  author: "著者"
  abstract: "ドキュメントの概要"
```

:::{seealso}

- [Reference > Formats > Docx](https://quarto.org/docs/reference/formats/docx.html)

:::
