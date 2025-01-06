# 自前のコマンドを定義したい（`\newcommand`）

```latex
\newcommand{\コマンド名}{やりたいこと}
\newcommand{\コマンド名}[引数の数]{やりたいこと。引数1=#1。引数2=#1。...引数9=#9。}
```

`\newcommand`で自前コマンドを定義できます。

:::{hint}

既存のコマンドを少し変えたい場合は、コマンド名を大文字にする方法もあります。
以下のサンプルでは、水平線の太さを変えたコマンドを新しく作成しています。
``hrule``を``\renewcommand``する代わりに``\HRule``というコマンド名にしています。

```latex
\newcommand{\HRule}{\rule{\linewidth}{0.5mm}}
```

:::

## コードしたい

```latex
\newcommand{\code}[1]{\texttt{#1}}
```

`\code`を`\texttt`コマンドのエイリアスとして定義しました。
本文中にコードを入力する際に便利です。
