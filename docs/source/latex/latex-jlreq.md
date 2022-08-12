# 日本語でLaTeXしたい（``jlreq``）

``jlreq``はLuaLaTeX、upLaTeX、pLaTeXに対応したドキュメントクラスです。
これから新しく文書を作成する場合は、迷わず使うとよいと思います。

```latex
\documentclass{jlreq}  % articleに相当
\documentclass[report]{jlreq}  % reportに相当
\documentclass[book]{jlreq}  % bookに相当
 ```

## 用紙のサイズを指定したい

```latex
\documentclass[papersize=a5]{jlreq}  % A5サイズ
```

## 一行あたりの文字数を指定したい

```latex
\documentclass[line_length=28zw]{jlreq}  % 全角28文字
```

## 一ページあたりの行数を指定したい

```latex
\documentclass[number_of_lines=27]{jlreq}  % 27行
```
