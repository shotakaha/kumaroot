# シェープしたい（`\textsc`）

```latex
{\upseries ...} または \textup{...}    % Upright（デフォルト）
{\itseries ...} または \textit{...}    % Italic
{\slseries ...} または \textsl{...}    % Slanted
{\scseries ...} または \textsc{...}    % Small Caps
```

本文中で局所的にシェープを切り替えることができます。

欧文では、強調する場合にイタリック体を使うことがあります。
和文では、シェープを切り替えることはほとんどないかもしれません。

| シェープ | コマンド形式 | 切り替え形式 | 数式 |
|---|---|---|---|
| イタリック体 | `\textit{...}` | `\itshape` | `\mathit{...}` |
| スラント体 | `\textsl{...}` | `\slshape` | - |
| スモールキャピタル体 | `\textsc{...}` | `\scshape` | `\mathsc{...}` |
| アップライト体（直立体） | `\textup{...}` | `\upshape` | `\mathup{...}` |
