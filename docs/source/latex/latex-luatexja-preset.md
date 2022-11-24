# 和文フォントを設定したい（``luatexja-preset``）

```latex
% プリアンブル
\usepackage[haranoaji]{luatexja-preset}    % TeXLive 2020のデフォルト
\usepackage[ipaex]{luatexja-preset}
\usepackage[sourcehan]{luatexja-preset}
\usepackage[hiragino-pro, hiragino-pron]{luatexja-preset}
```

和文フォントのプリセットを切り替えるパッケージです。
よく使われている和文フォント設定を1行で指定できます。

## プリセットに含まれる和文書体

1. ``haranoaji``: 原ノ味フォント
2. ``ipaex``: IPAexフォント
3. ``sourcehan``: 源ノ明朝・源ノ角ゴシックフォント
4. ``hiragino-pro``: ヒラギノフォント
5. ``jis90``: できるだけJIS90字形（JIS X 0208:1990）
6. ``jis2004``: できるだけJIS2004字形（JIS X 0213:2004）
7. ``deluxe``: 明朝3ウェイト（l/m/b）、ゴシック3ウェイト（m/b/eb）、丸ゴシック1ウェイト（mg）の7書体
8. ``bold``: デフォルトのゴシック体を太字

などなどあります。

## リファレンス

- {command}`texdoc luatexja-preset`
- {command}`texdoc luatexja`
