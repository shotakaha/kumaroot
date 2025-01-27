# 両面印刷したい（`twoside` / `oneside`）

```latex
% レポート形式で両面印刷
\documentclass[twoside]{ltjsreport}
```

`twoside`オプションで両面印刷用のレイアウトに変更できます。

## 片面印刷したい（`oneside`）

```latex
% ブック形式で片面印刷
\documentclass[oneside]{ltjsbook}
```

`oneside`で片面印刷用のレイアウトに変更できます。

## 余白を調整したい（`geometry`）

```latex
\documentclass[twoside]{ltjsreport}
\usepackage{geometry}
\geometry{inner=25mm, outer=15mm}
```

両面印刷の場合、
奇数ページと偶数ページで左右の余白サイズを調整したくなるかもしれません。
その場合は[geometryパッケージ](./latex-geometry.md)を使います。
`inner`でノド側の余白、`outer`で小口側の余白を設定できます。

適切な余白サイズについては、どのように綴じるかでも変わります。
詳しくはネット印刷会社の入稿ガイド／マニュアルなどを読んでみるとよいです。
