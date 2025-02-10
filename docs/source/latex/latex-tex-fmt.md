# 整形したい（`tex-fmt`）

```console
$ brew install tex-fmt

$ tex-fmt --version
tex-fmt 0.5.2

$ tex-fmt main.tex

// チェックのみ
$ tex-fmt --check main.tex

// 一括フォーマット
$ tex-fmt ディレクトリ/*.tex
```

`tex-fmt`はRust製のLaTeX用フォーマッターです。
TeX Liveに含まれてないためhomebrewでインストールします。
細かい設定ができないため、何も考えずに導入できます。

:::{note}

TeX Liveには`latexindent`というフォーマッターもあります。
こちらはPerlで書かれていて細かい設定ができます。

:::
