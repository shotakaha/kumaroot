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

`\index{索引語}`コマンドで索引に登録したい用語を設定できます。
`\printindex`コマンド索引を出力できます。

:::{note}

索引は`article`形式のクラスでは生成できません。

:::
