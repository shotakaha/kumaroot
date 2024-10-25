```{eval-rst}
.. index::
    pair: Hugo; 目次したい
```

# 目次したい（``.TableOfContents``）

```html
{{ block "main" . }}
<div class="toc">
  {{ .TableOfContents }}
</div>

{{ .Content }}

<div class="toc">
  {{ .TableOfContents }}
</div>
{{ end }}
```

``{{ .TableOfContents }}``で、コンテンツ内の見出しを目次として表示できます。
上のサンプルでは本文コンテンツの上下に目次を挿入しています。

:::{seealso}

- [](../latex/latex-tableofcontents.md)
- [](../myst/myst-toc.md)
- [](../sphinx/sphinx-syntax-toctree.md)
- [](../typst/typst-outline.md)

:::

## 設定したい（``markup.tableOfContents``）

```toml
[markup]
[markup.tableOfContents]
startLevel = 2   # [1-6]
endLevel = 3     # [1-6]
ordered = false  # [false|true]
```

`[markup]`セクションで目次レベルを設定できます。
`startLevel`と`endLevel`で、表示する見出しの深さを設定できます。
`ordered`で`<ul>`タグを使うか、`<ol>`タグを使うか、切り替えできます。

## リファレンス

- [Table Of Contents - Content Management - Hugo](https://gohugo.io/content-management/toc/)
- [Table Of Contents - Configuration - Hugo](https://gohugo.io/getting-started/configuration-markup/#table-of-contents)
