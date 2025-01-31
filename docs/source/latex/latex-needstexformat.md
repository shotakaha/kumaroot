# フォーマット指定したい（`\NeedsTeXFormat`）

```latex
% パッケージ／クラスファイルの先頭
\NeedsTeXFormat{LaTeX2e}[バージョン]

% 2023-06-01以降のLaTeX2eを要求
\NeedsTeXFormat{LaTeX2e}[2023-06-01]
```

`\NeedsTeXFormat{}`で、パッケージやクラスファイルの先頭に記述するコマンドで、
LaTeXのフォーマットとバージョンを指定できます。
指定したLaTeXのバージョンより古い環境ではコンパイルエラーになります。
