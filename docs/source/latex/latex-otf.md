# 和文フォントを設定したい（``otf``）

```latex
\usepackage{otf}
\usepackage[deluxe]{otf}
\usepackage[deluxe, multi]{otf}    % 簡体字、繁体字、ハングル
```

(u)pLaTeXでOpenTypeフォントを使えるようにするパッケージです。
``\UTF{16進数4桁}``でUnicode番号や、``\CID{10進数}``でOpenTypeのCID番号を指定して表示できるようになります。

## 多グリフ対応（簡体字、繁体字、ハングル）

``multi``オプションを有効にすると簡体字、繁体字、ハングルが使えるようになります。
コマンド名の末尾に``C(hina)``、``T(aiwan)``、``K(orea)``（だと思う）をつけることで切り替えることができます。

- ``\UTF`` → ``\UTFC{...}`` / ``\UTFT{...}`` / ``\UTFK{...}``
- ``\CID`` → ``\CIDC{...}`` / ``\CIDT{...}`` / ``\CIDK{...}``

また``\UTFM{...}``というコマンドもあり、日本語フォントにグリフががない場合に繁体字＞簡体字＞ハングルの順番でグリフを調べて表示します。

## リファレンス

- {command}`japanese-otf`
