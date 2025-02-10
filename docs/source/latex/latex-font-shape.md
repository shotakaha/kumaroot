# シェープしたい（`\textup` / `\textit` / `\textsl` / `\textsc`）

```latex
\textup{...}    % Upright（デフォルト）
\textit{...}    % Italic
\textsl{...}    % Slanted
\textsc{...}    % Small Caps
```

`\textシェープ{}`で、局所的に本文のシェープを変更できます。

欧文では、強調する場合にイタリック体を使うことがありますが、
和文ではシェープを切り替えることはほとんどないかもしれません。

## 環境したい（`\upshape` / `\itshape` / `\slshape` / `\scshape` / `\normalfont`）

```latex
\upseries  % 以降の文章をUpright体にする
\itseries  % 以降の文章をItalic体にする
\slseries  % 以降の文章をSlanted体にする
\scseries  % 以降の文章をSmall Caps体にする
\normalfont  % 以降の文章をデフォルトに戻す
```

## 数式したい（`\mathup` / `\mathit` / `\mathsl` / `\mathsc`）

```latex
\mathup{...}    % 数式フォントのUpright体
\mathit{...}    % 数式フォントのItalic体（デフォルト）
\mathsl{...}    % 数式フォントのSlanted体
\mathsc{...}    % 数式フォントのSmall Caps体
```

`\mathシェープ{}`で、数式フォントのシェープを変更できます。
数式フォントのデフォルトはイタリック体です。

| シェープ | コマンド形式 | 環境形式 | 数式環境 |
|---|---|---|---|
| アップライト体（直立体） | `\textup{...}` | `\upshape` | `\mathup{...}` |
| イタリック体 | `\textit{...}` | `\itshape` | `\mathit{...}` |
| スラント体 | `\textsl{...}` | `\slshape` | - |
| スモールキャピタル体 | `\textsc{...}` | `\scshape` | `\mathsc{...}` |
