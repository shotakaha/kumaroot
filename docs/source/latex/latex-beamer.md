# スライドしたい（`beamer`）

```latex
% コンテンツを上揃え[t]
\documentclass[t]{beamer}
\usepackage{luatexja}

\begin{document}

\section{スライド1}
\begin{frame}
  \frametitle{スライド1}
\end{frame}

\section{スライド2}
\begin{frame}
  \frametitle{スライド2}
\end{frame}

\end{document}
```

`beamer`クラスでスライド形式の文書を作成できます。
コンテンツはデフォルトで中央揃えになっているので、
`[t]`オプションで、上揃えにしています。

`beamer`の基本単位は`frame`環境です。

[luatexjaパッケージ](./latex-luatexja.md)で日本語を扱えるようになります。

## スライドしたい（`frame`）

```latex
% 目次のための \section
\section{タイトル}
\begin{frame}
  \frametitle{タイトル}

  \begin{itemize}
    \item 箇条書き
  \end{itemize}

\end{frame}
```

`frame`環境の中にスライドを作成します。
この中で`itemize`や`enumerate`、`equation`などの環境を
使ってコンテンツを整理できます。

## ブロックしたい（`block`）

```latex
\begin{block}{ブロックの見出し}
ブロックの内容
\end{block}
```

`block`環境で、枠付きのコンテンツ領域を作成できます。
他にも
`alertblock`、
`exampleblock`、など
目的別のブロック環境が用意されています。
それぞれの表示形式は選択したテーマに依存します。

## 段組したい（`columns`

```latex
\begin{frame}
  \frametitle{段組}

  \begin{columns}
  \column{0.5\textwidth}
  左段のコンテンツ

  \column{0.5\textwidth}
  右段のコンテンツ
  \end{columns}
\end{frame}
```

`columns`環境と`\column`コマンドで段組できます。
段組した中に、コンテンツを配置します。
ブロック環境も配置できます。

:::{note}

[minipage環境](./latex-minipage.md)も使えますが、
`columns`環境のほうが少しだけ簡単に記述できます。

:::

## モード設定（`\mode`）

```latex
\mode<presentation>
\mode<beamer>
\mode<second>
\mode<handout>
\mode<trans>
\mode<article>
\mode<all>
```

`\mode`コマンドで動作モードを変更できます。
デフォルトは`beamer`です。


## 併用不可のパッケージ

以下のパッケージは併用しないほうがよさそうです。

| パッケージ名 | 理由 |
|---|---|
| [](./latex-markdown.md) | コンパイルエラー |
| [](./latex-enumitem.md) | 箇条書き記号が消えた |

## テーマ設定したい（`\usetheme`）

```latex
% プリアンブル

% 全体テーマの設定
\usetheme[オプション]{テーマ名}

% 個別のスタイル
\usecolortheme[オプション]{スタイル名}
\usefonttheme[オプション]{スタイル名}
\useinnertheme[オプション]{スタイル名}
\useoutertheme[オプション]{スタイル名}
```

`\usetheme`コマンドでスライド全体のテーマを変更できます。

また、
`\usecolortheme`でカラーパレット、
`\usefonttheme`でフォントセット、
`\useinnertheme`で箇条書きやブロック表示の表示スタイル
`\useoutertheme`で見出しやヘッダー／フッターの表示スタイル
を個別に変更できます。

テーマ用ファイルはそれぞれ
`beamertheme<name>.sty`、
`beamercolortheme<name>.sty`、
`beamerfonttheme<name>.sty`、
`beamerinnertheme<name>.sty`、
`beameroutertheme<name>.sty`、
という命名規則になっています。

```console
$ mdfind beamertheme | rg .sty
$ mdfind beamercolortheme | rg .sty
$ mdfind beamerfonttheme | rg .sty
$ mdfind beamerinnertheme | rg .sty
$ mdfind beameroutertheme | rg .sty
```

[mdfind](../command/command-mdfind.md)などの検索コマンドで
パスを確認できます。
以下に、設定できる名前の一覧を書き出してみました。

### テーマ名の一覧（`\usetheme`）

27種類あります。

| テーマ名 |
|---|
| AnnArbor |
| Antibes |
| Bergen |
| Berkeley |
| Berlin |
| Boadilla |
| CambridgeUS |
| Copenhagen |
| Darmstadt |
| Dresden |
| EastLansing |
| Frankfurt |
| Goettingen |
| Hannover |
| Ilmenau |
| JuanLesPins |
| Luebeck |
| Madrid |
| Malmoe |
| Marburg |
| Montpellier |
| PaloAlto |
| Pittsburgh |
| Rochester |
| Singapore |
| Szeged |
| Warsaw |

### カラーパレット名の一覧（`\usecolortheme`）

`default`を含めて19種類あります。

1. default
2. albatross
3. beaver
4. beetle
5. crane
6. dolphin
7. dove
8. fly
9. lily
10. onarca
11. orchid
12. rose
13. gull
14. seahorse
15. sidebartab
16. spruce
17. structure
18. whale
19. wolverine

### フォントセット名の一覧

`default`を含めて6種類あります。

1. default
2. professionalfonts
3. serif
4. structurebold
5. structureitalicserif
6. structuresmallcapsserif

### インナーテーマ名の一覧（`\useinnertheme`）

`default`を含めて5種類あります。

1. default
2. circles
3. inmargin
4. rectangles
5. rounded

### アウターテーマ名の一覧（`\useoutertheme`）

`default`を含めて9種類あります。

1. default
2. infolines
3. miniframes
4. shadow
5. sidebar
6. smoothbars
7. smoothtree
8. split
9. tree
