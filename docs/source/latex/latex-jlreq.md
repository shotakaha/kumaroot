# ``jlreq``パッケージ

``jlreq``はLuaLaTeX、upLaTeX、pLaTeXに対応したドキュメントクラスです。
これから新しく文書を作成する場合は、迷わず使うとよいと思います。

JLReqはW3Cワーキンググループで議論されている「[日本語組版処理の要件](https://www.w3.org/TR/jlreq/)」です。
``jlreq``パッケージはこの要件の実装を試みたクラスファイルです。

```latex
\documentclass{jlreq}  % articleに相当
\documentclass[report]{jlreq}  % reportに相当
\documentclass[book]{jlreq}  % bookに相当
 ```



## 用紙のサイズを指定したい

```latex
\documentclass[paper=a4]{jlreq}  % A4サイズ
\documentclass[paper=a5]{jlreq}  % A5サイズ
\documentclass[paper=b4]{jlreq}  % B4サイズ
\documentclass[paper=b5]{jlreq}  % B5サイズ
```


## 1行あたりの文字数を指定したい

```latex
\documentclass[line_length=28zw]{jlreq}  % 全角28文字
```

## 1ページあたりの行数を指定したい

```latex
\documentclass[number_of_lines=27]{jlreq}  % 27行
```
