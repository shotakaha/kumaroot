# ``jlreq``したい

```latex
\documentclass{jlreq}  % articleに相当
\documentclass[report]{jlreq}  % reportに相当
\documentclass[book]{jlreq}  % bookに相当
```

## 1行あたりの文字数を指定したい

```latex
\documentclass[line_length=40zw]{jlreq}  % 全角40文字（デフォルト）
\documentclass[line_length=28zw]{jlreq}  % 全角28文字
```

## 1ページあたりの行数を指定したい

```latex
\documentclass[number_of_lines=30]{jlreq}  % 30行（デフォルト）
\documentclass[number_of_lines=27]{jlreq}  % 27行
```

## 余白を調整したい

```latex
\documentclass[head_space=25.4mm]{jlreq}    % 天の空き
\documentclass[foot_space=25.4mm]{jlreq}    % 地の空き
\documentclass[gutter=25.4mm]{jlreq}        % ノドの空き
\documentclass[headfoot_sidemargin=0pt]{jlreq}  % 柱やノンブルの左右の空き
```

**ノド**
:   ページを綴じる側の余白です。左右ページが同じデザインの場合、横組なら左マージン、縦組なら右マージンです。

**ノンブル**
:   各ページに振るページ番号です。

**柱**
:   各ページの上か下に出力する章や節の名前です。





## リファレンス

- {command}`jlreq`
