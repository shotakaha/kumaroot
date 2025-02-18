```{eval-rst}
.. index::
    pair: LaTeX; 索引したい
```

# 索引したい（`makeidx`）

```latex
% プリアンブル
\usepackage{makeidx}
\makeindex  % 索引を作成（idxファイルを作成）

% 本文
索引語\index{索引語}  % 索引に載せたい単語
索引語\index{よみかた@索引語}  % 漢字の読み方

\printindex  % 索引を表示
```

`makeidx`で索引を作成できます。
サンプルのような構成のLaTeXファイルを作成し、
[makeindex](./latex-makeindex.md)コマンドで索引をタイプセットします。

## 索引に追加したい（`\index`）

```latex
単語\index{単語}
```

`\index{索引語}`コマンドで索引に登録したい用語を設定できます。

```latex
単語\index{よみかた@単語}
```

`よみかた@単語`で読み方を指定できます。

## 索引を出力したい（`\printindex`）

```latex
% 本文
\printindex
```

本文中の`\printindex`の位置に索引を出力できます。
通常、巻末に出力します。

## 索引ファイルを出力したい（`\makeindex`）

```latex
% プリアンブル
\makeindex
```

プリアンブルに`\makeindex`と書いておくと、
コンパイルしたときに索引ファイル（`.idx`）が生成されます。
