# 和文クラスしたい（`jlreq`）

```latex
\documentclass{jlreq}  % articleに相当
\documentclass[report]{jlreq}  % reportに相当
\documentclass[book]{jlreq}  % bookに相当
```

`jlreq`はLuaTeX-jaコミュニティが開発している和文クラスです。
W3Cワーキンググループで議論されている
「[日本語組版処理の要件](https://www.w3.org/TR/jlreq/)」
の実装を試しているクラスです。

美文書LaTeXも第9版からこのクラスに移行したそうなので、
これからの日本語標準クラスといってよいと思います。
これから作成する文書は、迷わず`jlreq`でよいと思います。

## 1行あたりの文字数を指定したい（`line_length`）

```latex
% 全角40文字（デフォルト）
\documentclass[line_length=40zw]{jlreq}

% 全角28文字に変更
\documentclass[line_length=28zw]{jlreq}
```

## 1ページあたりの行数を指定したい（`number_of_lines`）

```latex
% 30行（デフォルト）
\documentclass[number_of_lines=30]{jlreq}

% 27行に変更
\documentclass[number_of_lines=27]{jlreq}
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
