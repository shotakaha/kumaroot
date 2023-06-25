# ダミー画像したい（``mwe``）

```latex
%% プリアンブル
\usepackage{mwe}  % graphicx と blindtext が読み込まれる


%% 本文
\begin{figure}
  \centering
  \includegraphics[width=0.8\linewidth]{example-image-16x9.pdf}
  \caption{16:9の横画像をテスト表示}
\end{figure}
```

``mwe``はMinimum Working Examplesの略です。
LaTeXのQ&Aフォーラムで、デバッグ用サンプル共有を簡単にするためのパッケージです。
ダミーのテキスト（``blindtext``）や画像の挿入ができます。

- 汎用素材 : ``example-image``（``.pdf`` / ``.png`` / ``.jpg`` / ``.eps``）
- 文字入り : ``example-image-a`` / ``example-image-b`` / ``example-image-c``
- 文字なし : ``example-image-plain`` / ``example-image-empty``
- 16:10画像 : ``example-image-16x10`` / ``example-image-10x16``
- 16:9画像 : ``example-image-16x9`` / ``example-image-9x16``
- 黄金比 : ``example-image-golden`` / ``example-image-golden-upright``
- 1:1画像 : ``example-image-1x1``
- テスト画像 : ``example-grid-100x100pt``

他にも利用可能な画像は``$ texdoc mwe``で確認してください。
