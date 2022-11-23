# コードブロックしたい（``minted``）

```latex
\usepackage{minted}

\begin{minted}{言語名}
コード
\end{minted}
```

コードブロックをハイライトしたい場合、``minted``パッケージを使うとキレイに表示できます。

## Pygmentsのインストール

```bash
$ pip3 pygments
```

Pythonの``pygments``に依存したパッケージなので、文書を作成する環境にインストールされている必要があります。
``pip3``でインストールしたり、``poetry``でインストールしたり、作業環境に合わせて使い分けてください。

また、Pygments依存しているため、文書をコンパイルするときに``-shell-escape``が必要です。

```bash
$ latexmk -shell-escape
```

## スタイルを変更したい

```latex
\usemintedstyle{default}
\usemintedstyle{material}
\usemintedstyle{dracula}
\usemintedstyle{github-dark}
```

## Pythonをハイライトしたい

```latex
\begin{minted}{python}
if __name__ == "__main__":
    print("Hello Python")
\end{minted}
```
