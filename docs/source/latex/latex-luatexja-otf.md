# 異字体したい（`latexja-otf`）

```latex
\usepackage{luatexja-otf}
```

`latexja-otf`は、異体字を扱えるようにするパッケージです。

**異体字**は同じ文字コードでも、字体が異なる文字のことです。
`\UTF{16進数4桁}`でUnicode番号や、
`\CID{10進数}`でOpenTypeのCID番号を指定して表示できるようになります。

## 異字体したい（`otf`）

```latex
\usepackage{otf}
\usepackage[deluxe]{otf}
\usepackage[deluxe, multi]{otf}    % 簡体字、繁体字、ハングル
```

(u)pLaTeXでは`otf`パッケージを利用します。

:::{note}

もともと、(u)pLaTeX用に`utf`パッケージが発展し、この`otf`パッケージになり、
さらに`luatexja-otf`がその機能の一部を実装した形です。

:::

## 多グリフ対応（簡体字、繁体字、ハングル）

``multi``オプションを有効にすると簡体字、繁体字、ハングルが使えるようになります。
コマンド名の末尾に``C(hina)``、``T(aiwan)``、``K(orea)``（だと思う）をつけることで切り替えることができます。

- ``\UTF`` → ``\UTFC{...}`` / ``\UTFT{...}`` / ``\UTFK{...}``
- ``\CID`` → ``\CIDC{...}`` / ``\CIDT{...}`` / ``\CIDK{...}``

また``\UTFM{...}``というコマンドもあり、日本語フォントにグリフががない場合に繁体字＞簡体字＞ハングルの順番でグリフを調べて表示します。
