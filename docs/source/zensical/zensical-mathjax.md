# 数式したい（`MathJax`）

```toml
[project]
extra_javascript = [
    "javascripts/mathjax.js",  # docs/javascripts/mathjax.jsに作成
    "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
    # "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js",  # physicsパッケージ記法を使う場合
]

[project.markdown_extensions]
pymdownx.arithmatex.generic = true
```

```js
// docs/javascripts/mathjax.js
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
})

component$.subscribe(({ ref }) => {
  if (ref.classList.contains("md-annotation"))
    MathJax.typesetPromise([ref])
})
```

`MathJax`は、ウェブ上で数式を表示するためのJavaScriptライブラリです。
`zensical.toml`の`extra_javascript`に設定を追加することで、Zensicalでも使うことができます。

プロジェクト内に`mathjax.js`を作成して、`window.MathJax`に設定を追加することで、ページ内の数式を自動的にレンダリングできるようにします。

## リファレンス

- [Math - Zensical](https://zensical.org/docs/authoring/math/)
- [MathJax](https://www.mathjax.org/)
