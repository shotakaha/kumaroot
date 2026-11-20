# 書体したい（`\textrm` / `\textsf` / `\texttt`）

```latex
% 本文
\textrm{...}  % セリフ体（ローマン体）/ 欧文デフォルト
\textsf{...}  % サンセリフ体
\texttt{...}  % タイプライター体

\textmc{...}  % 明朝体 / 和文デフォルト
\textgt{...}  % ゴシック体
\textmg{...}  % 丸ゴシック体（deluxeオプションが必要）
```

`\textファミリー{}`で、局所的に本文の書体（ファミリー）を変更できます。

## 切り替えたい（`\rmfamily` / `\sffamily` / `\ttfamily`）

```latex
\rmfamily  % 以降のフォントがセリフ体
\sffamily  % 以降のフォントがサンセリフ体
\ttfamily  % 以降のフォントがタイプライター体
```

## 数式したい（`\mathrm` / `\mathsf` / `\mathtt` / `\text`）

```latex
% 数式環境
\mathrm{...}  % 数式フォントのセリフ体
\mathsf{...}  % 数式フォントのサンセリフ体
\mathtt{...}  % 数式フォントのタイプライター体
\text{...}    % 数式環境で本文フォント（のセリフ体）
```

`\mathファミリー{}`で、数式フォントのファミリーを変更できます。
`\text{}`は数式環境で本文フォントを表示するコマンドです。

| ファミリー | コマンド形式 | 環境形式 | 数式環境 | `fontspec` | `luatexja-fontspec` |
|---|---|---|---|---|---|
| セリフ体 | `\textrm{...}` | `\rmfamily` | `\mathrm{...}` | `\setmainfont{...}` | - |
| サンセリフ体 | `\textsf{...}` | `\sffamily` | `\mathsf{...}` | `\setsansfont{...}` | - |
| タイプライター体 | `\texttt{...}` | `\ttfamily` | `\mathtt{...}` | `\setmonofont{...}` | `\setmonojfont{...}`（和文） |
| （和文）明朝体 | `\textmc{...}` | `\mcfamily` | - | - | `\setmainjfont{...}` |
| （和文）ゴシック体 | `\textgt{...}` | `\gtfamily` | - | - | `\setsansjfont{...}` |
| （和文）丸ゴシック体 | `\textmg{...}` | `\mgfamily` | - | - | `deluxe`オプションで設定 |

`\ttfamily`は、和文もタイプライター体（`\jttdefault`）に切り替えます。
