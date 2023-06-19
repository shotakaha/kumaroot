```{eval-rst}
.. index::
    pair: ヘッダーしたい; LaTeX
```

# ヘッダー／フッターしたい（``fancyhdr``）

```latex
\usepackage[オプション]{fancyhdr}
\pagestyle{fancy}
\fancyhead[L]{ヘッダー・左}  % = \lhead{ヘッダー・左}
\fancyhead[C]{ヘッダー・中}  % = \chead{ヘッダー・中央}
\fancyhead[R]{ヘッダー・右}  % = \rhead{ヘッダー・右}

\fancyfoot[L]{フッター・左}  % = \lfoot{フッター・左}
\fancyfoot[C]{フッター・中}  % = \cfoot{フッター・中央}
\fancyfoot[R]{フッター・右}  % = \rfoot{フッター・右}
```

``fancyhdr``パッケージを使うと、文書の柱（ヘッダーやフッター）をいい感じに装飾できます。
読み込む順番に気をつける必要があります。

:::{note}

``\lhead``などのこれまで使っていた短いコマンド名の利用は**非推奨**となっています。
文字数が増えますが``\fancyhead[L]``などを使いましょう。

:::

## 現在のページに設定したい

```latex
\thispagestyle{fancy}
\fancyhead[L]{ヘッダー・左}
\fancyhead[C]{ヘッダー・中央}
\fancyhead[R]{ヘッダー・右}
\fancyfoot[L]{フッター・左}
\fancyfoot[C]{フッター・中央}
\fancyfoot[R]{フッター・右}
```

現在のページに設定する場合は``\thispagestyle``コマンドを使います。
改ページ（``\newpage``）でリセットされます。

## ノンブルしたい

```latex
\pagestyle{fancy}
\fancyfoot{}
\fancyfoot[R]{\thepage}
```

デフォルトで、ページ中央に表示されるノンブル（＝ページ番号）を右下に変更する方法です。
``\fancyfoot{}``でデフォルト設定を一度削除した後に、右フッターのみ再設定しています。

## ロゴしたい

```latex
\usepackage{graphincx}
\usepackage{geometry}
\geometry{
    headheight=4\zh,
    headsep=1\zh,
    includehead=true,
}

\pagestyle{fancy}
\fancyhead[R]{\includegraphics[height=5\zh]{ロゴ画像のパス}}
\addtolength{\headheight}{\baselineskip}
```

ページの右上にロゴを挿入する方法です。
画像の挿入なので``graphicx``パッケージを使っています。
高さを指定して右ヘッダーに追加しています。

画像の高さに合わせて、ヘッダーの高さも調整したほうがよいので``geometry``パッケージを使っていろいろ変更しています。

## 線の幅を変更したい

```latex
\renewcommand{\headrulewidth}{1mm}
\renewcommand{\footrulewidth}{1mm}
```

``\headrulewidth``と``\footrulewidth``を``\renewcommand``して、境界線の幅を変更できます。

## 線の色を変更したい

```latex
\usepackage{xcolor}
\definecolor{Green}{HTML}{006E4F}

\renewcommand{\headrule}{\textcolor{Green}{\hrule width\headwidth height\headrulewidth \vskip-\headrulewidth}}
\renewcommand{\footrule}{\textcolor{Green}{\hrule width\headwidth height\footrulewidth \vskip\footrulewidth}}
```

``\headrule``と``\footrule``を``\renewcommand``して、ヘッダー／フッターの色を変更できます。
色は[xcolorパッケージ](./latex-xcolor.md)を使ってカスタムカラーを定義し、``\textcolor``コマンドを使って変更します。
