# 数式したい（`KaTeX`）

```toml
[project]
extra_javascript = [
    "javascripts/katex.js",  # docs/javascripts/katex.jsに作成
    "https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js",
    "https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js",
]

extra_css = [
    "https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css",
]

[project.markdown_extensions]
pymdownx.arithmatex.generic = true
```

```js
// docs/javascripts/katex.js
document$.subscribe( ( {body} ) => {
    renderMathInElement(body, {
        delimiters: [
            { left: "$$", right: "$$", display: true},
            { left: "$", right: "$", display: false},
            { left: "\\(", right: "\\)", display: false},
            { left: "\\[", right: "\\]", display: true},
        ],
    })
})
```

`KaTeX`は、ウェブ上で数式を表示するためのJavaScriptライブラリです。
`zensical.toml`の`extra_javascript`と`extra_css`に設定を追加することで、Zensicalでも使うことができます。

プロジェクト内に`katex.js`を作成して、`renderMathInElement`を呼び出すことで、ページ内の数式を自動的にレンダリングできるようにします。

## リファレンス

- [Math - Zensical](https://zensical.org/docs/authoring/math/)
- [KaTeX](https://katex.org/)
