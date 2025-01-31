# 依存パッケージしたい（`RequirePackage`）

```latex
% プリアンブル
\RequirePackage{パッケージ名}[リリース日]
```

`\RequirePackage`コマンドで依存パッケージを設定できます。

## 依存パッケージを確認したい

```console
$ kpsewhich パッケージ名.sty | xargs cat | rg RequirePackage
```

パッケージ内の`RequirePackage`で依存パッケージを確認できます。
依存関係をリストできるコマンドがないようなので、
いくつかのコマンドを組み合わせて確認しています。

```console
$ kpsewhich luatexja-fontspec | xargs cat | rg Require
\RequirePackage{l3keys2e,luatexja}
\RequirePackage{fontspec}[2019/03/15]% v2.7c
    \RequirePackage{luatexja-fontspec-29e} % v2.9e
    \RequirePackage{luatexja-fontspec-29c} % v2.9c
  \RequirePackage{luatexja-fontspec-27c} % v2.7c
```

[luatexja-fontspec](./latex-luatexja-fontspec.md)の中で
[luatexja](./latex-luatexja.md)と
[fontspec](./latex-fontspec.md)が読み込まれていることが確認できました。

```latex
\RequirePackage{iflang}
\RequirePackage{iftex}
  \RequirePackage{fontspec}
  \RequirePackage{unicode-math}
    \@ifpackagewith{fontsetup}{gfsdidotclassic}{\RequirePackage{ucharclasses}}{}
    \@ifpackagewith{fontsetup}{minion}{\RequirePackage{ucharclasses}}{}
    \@ifpackagewith{fontsetup}{msgaramond}{\RequirePackage{ucharclasses}}{}
    \@ifpackagewith{fontsetup}{palatino}{\RequirePackage{ucharclasses}}{}
    \RequirePackage{fourier-otf}
    \RequirePackage{xcharter-otf}
    \RequirePackage{libertinus-otf}
```

`fontsetup`の中で
[fontspec](./latex-fontspec.md)と
[unicode-math](./latex-unicode-math.md)が
読み込まれていることが確認できました。

:::{note}

依存パッケージを確認することで、パッケージ読み込みの重複を回避できます。
また、読み込む順番の間違いなどに気をつけることができます。

:::
