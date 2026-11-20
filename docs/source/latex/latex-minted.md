# コードブロックしたい（``minted``）

```latex
% プリアンブル
\usepackage{xcolor}

\usepackage{minted}
\setminted{
    style=default,
    fontfamily=tt,
    fontshape=upright,
    frame=leftline,
    linenos=true,
    bgcolor=black!10,
}

% 本文
\begin{minted}[オプション]{言語名}
コード
\end{minted}

\begin{minted}[showspaces]{python}
if __name__ == "__main__":
    print("Hello Python")
\end{minted}
```

`minted`パッケージで、コードブロックをきれいに表示できます。
このパッケージはPythonの（`latexminted`を介して）`pygments`を利用したパッケージです。
利用可能な言語や表示スタイルなどは`pygments`のドキュメントも確認するとよいです。

:::{note}

`minted v3`になって`pygments`を直接インストールする必要がなくなりました。
また、文書をビルドする際の`-shell-escape`も不要になりました。
`minted v2`からの変更点の詳細はドキュメントを確認してください（`$ texdoc minted`）

:::

## スタイルを変更したい（`\usemintedstyle`）

```latex
% プリアンブル
\usemintedstyle{default}
% もしくは
\setminted{style=default}
```

`\usemintedstyle`で、シンタックス・ハイライトのテーマを変更できます。
そのほかの設定と一緒に`\setminted`する場合は`style`キーで変更できます。

```latex
% プリアンブル
\usemintedstyle{material}
\usemintedstyle{dracula}
\usemintedstyle{github-dark}
```

## 全体の設定したい（`\setminted`）

```latex
% プリアンブル
\setminted{
    style=default,
    fontfamily=tt,        % (font-family): [tt | courier | helvetica]
    fontshape=upright,    % (font shape): [auto]
    frame=leftline,       % [none | leftline | topline | bottomline | lines | single]
    linenos=true,         % (boolean): [false | true]
}
```

`\setminted`で文書全体の`minted`の設定を変更できます。
コードブロック内の欧文コメントが斜体で表示されるのが嫌なので、
`fontshape=upright`で字形を立体（upright）に指定しています。
コメントの斜体はスタイル側で指定されているため、変わらない場合は`style`を変更してください。

## 背景色したい（`bgcolor`）

```latex
\usepackage{xcolor}
\setminted{
    bgcolor=black!10,
}
```

`bgcolor`でコードブロックの背景色を変更できます。
デフォルトは地の色なので、背景色を追加すると見やすくなります。
色は[xcolorパッケージ](./latex-xcolor.md)にある色名を使えばOKです。

:::{note}

表示スタイル（`style`）を`material`や`dracula`に変更しても、背景色は無地のままでした。
`bgcolor`で別途設定が必要です。

:::

## 半角スペースを表示したい（`showspaces`）

```latex
\begin{minted}[showspaces]{python}
if __name__ == "__main__":
    print("Hello Python")
\end{minted}
```

`showspaces`オプションで、コード内の半角スペースを空白記号で表示できます。
PythonやMakefileなど、空白（やインデント）が意味をもつ言語で、曖昧さを避けたい場合に有効です。
ただし、すべてのコードブロックで空白が表示されると、かえってみにくくなります。
個別の環境オプションでピンポイントで使用するとよいと思います。
