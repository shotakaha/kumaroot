# 和文クラスしたい（`jlreq`）

```latex
\documentclass{jlreq}  % articleに相当
\documentclass[report]{jlreq}  % reportに相当
\documentclass[book]{jlreq}  % bookに相当

% オプション
\jlreqsetup{
    % keyval形式
    paper=a4paper,
}
```

`jlreq`はLuaTeX-jaコミュニティが開発している和文クラスです。
W3Cワーキンググループで議論されている
「[日本語組版処理の要件](https://www.w3.org/TR/jlreq/)」
の実装を試しているクラスです。

美文書LaTeXも第9版からこのクラスに移行したそうなので、
これからの日本語標準クラスといってよいと思います。
これから作成する文書は、迷わず`jlreq`でよいと思います。

`\jlreqsetup`でクラスオプションを設定できます。

## クラスオプションしたい

| オプション名 | 値 | デフォルト値 | 説明 |
|---|---|---|---|
| `paper` | サイズ名 or {横, 縦} | `a4paper` | 用紙のサイズ |
| `fontsize` | 寸法 | `10pt` | 欧文フォントのサイズ |
| `jafontsize` | 寸法 | - | 和文フォントのサイズ |
| `jafontscale` | 実数 | `1` | 和文／欧文のサイズ比 |
| `line_length` | 長さ | `40zw` | 1行の長さ |
| `number_of_lines` | 自然数 | `30` | 1ページの行数 |
| `gutter` | 寸法 | | ノドの余白の大きさ |
| `fore-edge` | 寸法 | | 小口の余白の大きさ |
| `head_space` | 寸法 | | 天のアキの大きさ |
| `foot_space` | 寸法 | | 地のアキの大きさ |
| `baselineskip` | 寸法 | `jafontsize`の1.7倍 | 行送り |
| `linegap` | 寸法 | - | 行間 |
| `headfoot_sidemargin` | 寸法 | | 柱やノンブルの左右のアキ |
| `column_gap` | 寸法 | | 段間 |
| `sidenote_length` | 寸法 | | 傍注の幅 |

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
