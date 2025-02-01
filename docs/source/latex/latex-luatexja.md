# 和文対応したい（`luatexja`）

```latex
\usepackage{luatexja}
```

`luatexja`は文書を和文対応させるパッケージです。
ドキュメントクラスに依らず、和文のフォントや組版の規則を設定できます。
デフォルトのフォントは原ノ味フォント（`haranoaji`）です。

:::{seealso}

フォントの変更は、以下のページに整理しました。

- [](./latex-luatexja-fontspec.md)
- [](./latex-luatexja-preset.md)

:::

## 欧文クラスしたい（`classes` + `luatexja`）

```latex
% compiler: LuaLaTeX
\documentclass{article}
\usepackage{luatexja}
```

`article`などの欧文クラスで、
和文設定が使えるようになります。
テンプレートが配布されている海外の学会などで、一部（や一時的に）日本語を使いたい場合に役に立ちます。

:::{caution}

欧文用クラスの場合、`Contents`や`Abstract`、`Appendix`などのように
コマンドや環境で表示される内容が英語のまま出力されます。
局所的にカスタマイズすることはできますが、
日本語の文書を作成する場合は、素直に和文クラスを選ぶとよいです。

:::

## スライドしたい（`beamer` + `luatexja`）

```latex
\documentclass[t]{beamer}
\usepackage{luatexja}
```

スライド作成の定番の[beamerクラス](./latex-beamer.md)で、
和文設定が使えるようになります。

:::{note}

`beamer`は`dvipdfm`に対応していないため、
(u)pLaTeXを使ったスライド作成はできません。

:::

## 依存パッケージ

```console
$ kpsewhich luatexja.sty | xargs cat | rg RequirePackage
// \RequirePackage{expl3} needed if the version of l3kernel is v6111
\RequirePackage{luatexja-core,luatexja-compat}
```

```console
$ kpsewhich luatexja-core.sty | xargs cat | rg RequirePackage
\RequirePackage{infwarerr}
\RequirePackage{luatexbase}
\RequirePackage{luaotfload}
\RequirePackage{ltxcmds}    [2011/11/09] % v1.22
\RequirePackage{pdftexcmds} [2011/11/29] % v0.20
\RequirePackage{xkeyval}    [2012/10/14] % v2.6b
\RequirePackage{etoolbox}
\IfFileExists{everyhook.sty}{\RequirePackage{everyhook}\ltj@everyhook@availtrue}{}
\RequirePackage{ltj-base}
```
