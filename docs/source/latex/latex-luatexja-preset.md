# luatexja-preset

```latex
% プリアンブル
\usepackage[haranoaji]{luatexja-preset}    % TeXLive 2020のデフォルト
\usepackage[ipaex]{luatexja-preset}
\usepackage[sourcehan]{luatexja-preset}
\usepackage[hiragino-pro, hiragino-pron]{luatexja-preset}
```

和文フォントのプリセットを切り替えるパッケージです。
よく使われている和文フォント設定を1行で指定できます。

## jlreqのフォントメトリックを使いたい

```latex
\usepackage[haranoaji, deluxe, match, jfm_yoko=jlreq, jfm_tate=jlreqv]{luatexja-preset}
```

jlreqは独自のフォントメトリックを使っているので、
源ノフォントを使って、多書体化したい場合、
jlreqの横組（``jlreq``）・縦組（``jlreqv``）の
フォントメトリックを指定する必要があります。

## リファレンス

- {command}`luatexja`
