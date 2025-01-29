# スライドしたい（`beamer`）

```latex
% コンテンツを上揃え[t]
\documentclass[t, aspectratio=169]{beamer}
\usepackage[no-math, deluxe]{luatexja-preset}
\renewcommand{\kanjifamilydefault}{\gtdefault}
\renewcommand{\emph}[1]{{\upshape\bfseries #1}}

\title{タイトル}
\author{名前}
\institute[省略形]{所属}
\date[省略形]{\today}

\begin{document}

% 表紙
\begin{frame}
  \titlepage
\end{frame}

% 目次
\section*{目次}
\begin{frame}
  \frametitle{もくじ}
  \tableofcontents
\end{frame}

% 本文
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
`[t]`オプションで上揃えにしています。

## スライドサイズしたい（`aspectratio`）

```latex
\documentclass[aspectratio=169]{beamer}
```

`aspectratio`オプションで、スライドのサイズを変更できます。
デフォルトは`43`（4:3）です。

## 日本語したい（`luatexja-preset`）

```latex
\usepackage[no-math, deluxe]{luatexja-preset}
% ゴシック体に変更
\renewcommand{\kanjifamilydefault}{\gtdefault}
% \gtdefault: ゴシック体
% \mcdefault: 明朝体
% \rmdefault: ローマン体
% 強調を太字（デフォルトは斜体）
\renewcommand{\emph}[1]{{\upshape\bfseries #1}}
% \upshape: 立体フォント
% \bfseries: 太字
```

[luatexja-presetパッケージ](./latex-luatexja-preset.md)で、
和文フォントを使えるようにします。
`deluxe`オプションで多書体を使えるようにしておきます。

また、`\kanjifamilydefault`のデフォルト値は明朝体になっているため
ゴシック体（`\gtdefault`）に変更しています。
`\emph`コマンドも斜体ではなく**太字の立体**に変更しています。

## スライドしたい（`frame`）

```latex
% 目次のための \section
\section{タイトル}
\begin{frame}
  \frametitle{タイトル}
  内容
\end{frame}
```

`frame`環境の中にスライドを作成します。
この中で`itemize`や`enumerate`、`equation`などの環境を
使ってコンテンツを整理できます。

## 表紙したい（`titlepage`）

```latex
% プリアンブル
\title[短いタイトル]{タイトル}
\author{名前}
\institute{所属}
\date{報告日}

% 本文
\begin{frame}
  \titlepage
\end{frame}
```

`\titlepage`で表紙を出力できます。
出力する情報はプリアンブルで設定します。

## 目次したい（`\tableofcontents`）

```latex
\section*{目次}
\begin{frame}
  \frametitle{もくじ}
  \tableofcontents
\end{frame}
```

[\tableofcontentsコマンド](./latex-tableofcontents.md)でもくじを出力できます。
目次は`\section{}`や`\subsection{}`で設定します。
`\frametitle{}`は目次に自動追加されません。

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

## 段組したい（`columns`）

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

| テーマ名 | 基本色 | サイドバー | ヘッダー |
|---|---|---|---|
| AnnArbor | 黄と青 | - | - |
| Antibes | 青 | - | あり |
| Bergen | 青 | left | - |
| Berkeley | 青 | left | - |
| Berlin | 青 | - | left |
| Boadilla | 白と青 | - | - |
| CambridgeUS | 白と赤 | - | あり |
| Copenhagen | 青 | - | tree |
| Darmstadt | 青 | - | nav |
| Dresden | 青 | - | nav |
| EastLansing | 緑 | - | split |
| Frankfurt | 青 | - | nav |
| Goettingen | 薄青 | right | - |
| Hannover | 薄青 | left | - |
| Ilmenau | 青 | - | nav |
| JuanLesPins | 青 | - | section |
| Luebeck | 青 | - | tree |
| Madrid | 青 | - | - |
| Malmoe | 青 | - | split/tree |
| Marburg | 白と青 | right | - |
| Montpellier | 白 | - | section |
| PaloAlto | 青 | left | - |
| Pittsburgh | 白 | - | - |
| Rochester | 青 | - | - |
| Singapore | 白 | - | nav |
| Szeged | 白 | - | nav |
| Warsaw | 青 | - | tree |

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
10. monarca
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
