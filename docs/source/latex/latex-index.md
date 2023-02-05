# 索引したい（``\index``）

```latex
% プリアンブル
\usepackage{makeidx}
\makeindex  % 索引を作成（idxファイルを作成）

% ドキュメント
索引語\index{索引語}  % 索引に載せたい単語
索引語\index{よみかた@索引語}  % 漢字の読み方

\printindex  % 索引を表示
```
