# 数式したい（`MathJax`）

```yaml
title: 数式したい（MathJax）
format:
  html:
    toc: true
    html-math-method:
      method: mathjax
      url: https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js
```

`MathJax`は、ウェブ上で数式を表示するためのJavaScriptライブラリです。
`html-math-method: mathjax`で、QuartoのHTML出力でMathJaxを使うことができます。
`url`で、MathJaxのCDNを変更できます。
`tex-chtml-full.js`にすると、physicsパッケージ記法を利用できます。
