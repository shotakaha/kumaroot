# 画像したい（``graphicx``）

```latex
%% プリアンブル
\usepackage{graphicx}

%% 本文
\begin{figure}[htbp]
    \centering
    \includegraphics[図のオプション]{図のファイル名}
    \caption{図の説明}
    \label{図の参照ラベル}
\end{figure}
```

画像を扱うために``graphicx``パッケージを使います。
このパッケージで文字列の変形もできるようになります。

画像ファイルは``JPEG``、``PNG``、``PDF``形式が使えます。
すこし前は``EPS``形式への変換が必要でしたが、いまは不要です。

レポートや論文などに画像を挿入する場合、図にキャプションをつけたり、本文から参照したりします。
``\includegraphics``コマンドで挿入し、``figure``環境を使ってページ内に配置するとよいです。
``\caption``コマンドで画像のキャプションを追加できます。

配置オプションは``h / t / b / p``から選択できます。
デフォルトは``[tbp]``になっています。

:::{seealso}

たくさんの図を挿入する場合は、次のような``\Figure``コマンドを作成しておくと便利です。

```latex
%% プリアンブル
%% \Figure{幅}{画像}{図キャプション}{図のラベル}
\newcommand{\Figure}[4]{
    \begin{figure}[htbp]
        \centering
        \includegraphics[#1\linewidth]{#2}
        \caption{#3}
        \label{#4}
    \end{figure}
}
```

:::

## 画像のサイズを指定したい（``width``）

```latex
\includegraphics[width=3cm]{図のファイル名}
\includegraphics[height=3cm]{図のファイル名}
\includegraphics[width=0.8\linewidth]{図のファイル名}
```

画像のサイズは``width``や``height``オプションなどを指定して拡大・縮小できます。
行幅（``\linewidth``）を基準にした相対値で指定すると簡単です。

## 画像ディレクトリを指定したい（``\graphicspath``）

```latex
\graphicspath{{images/}}
\graphicspath{{images/} {figures/}}
```

LaTeXで文書を作成していると、画像ファイルをひとつのディレクトリにまとめて管理することが多いと思います。
``\graphicspath``で画像ディレクトリのパスを指定しおくと、``\includgraphics``するときにちょっとだけ楽になります。

## ドラフト表示したい（``draft``）

```latex
%% プリアンブル
\usepackage[draft]{graphicx}
```

パッケージオプションに``[draft]``を指定すると、画像サイズの枠線とファイル名のみが表示されます。
画像をアテで入れているだけたったり、本文の推敲に集中したいときに使えます。

## ドライバーを指定したい

```latex
\documentclass[dvipdfmx]{jsarticle} % pLaTeX
\documentclass[dvipdfmx, uplatex]{jsarticle} % upLaTeX
%% \usepackage[dvipdfmx]{graphicx} % ← いまは昔；非推奨
```

ドライバーは**ドキュメントクラスのオプション**で指定します。
``graphicx``のオプションで指定する方法は非推奨です。

(u)pLaTeXの場合は、ドライバーに``dvipdfmx``を必ず指定する必要があります。
LuaLaTeXの場合は自動判断してくれるため、逆に、何も指定してはいけません。

## 色空間を変換したい

パソコンで作成した画像の色空間は``RGB``となっています。
これを印刷物にする場合、色空間を``CMYK``に変換する必要があります。
変換はAdobe PhotoshopやAdobe Illustratorなどを使うとよいです。
