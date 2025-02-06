# 部分フォントしたい（`\usefont` / `\usekanjifont`）

```latex
% 欧文フォントの変更
{\usefont{<エンコーディング>}{<ファミリー>}{<シリーズ>}{<シェープ>} テキスト}

{\usefont{T1}{ptm}{m}{it} これは Times Italic のテキスト}
{\usefont{T1}{phv}{b}{n} これは Helvetica Bold のテキスト}

% 和文フォントの変更
{\usekanjifont{<和文エンコーディング>}{<ファミリー>}{<シリーズ>}{<シェープ>} テキスト}

% 和文フォント
{\usekanji{和文エンコーディング}{ファミリー}{シリーズ}{シェープ} 文字列}
{\usekanji{JY1}{mc}{m}{n} これは（JY1 / 明朝体 / 標準 / upright） のテキスト} % pLaTeX
{\usekanji{JY2}{gt}{b}{n} これは（JY2 / ゴシック体 / 太字 / upright） のテキスト} % upLaTeX
{\usekanji{JY3}{gt}{bx}{n} これは（JY3 / ゴシック体 / 極太字 / upright） のテキスト} % LuaLaTeX
```

`\usefont`で欧文フォント、
`\usekanjifont`で和文フォントを
部分的に変更できます。

フォントの変更には次の5つの要素が必要です。

1. エンコーディング
1. ファミリー（＝書体）
1. シリーズ（＝ウェイト）
1. シェープ
1. サイズ

LaTeXの標準コマンドには、それぞれ変更できるコマンドもあります。

:::{note}

ドキュメント全体のフォント設定は、
[fontspecパッケージ](./latex-fontspec.md)や
[luatexja-fontspecパッケージ](./latex-luatexja-fontspec.md)を
使うのがお手軽です。

:::

## エンコーディング

フォントの**エンコーディング**とは**TeX内部の文字マッピング**のことです。
UTF-8やシフトJISのようなファイルのエンコーディングとはまったく別物です。

欧文エンコーディングには`TU`（TeX Unicode）、`T1`、`OT1`（Old T1）があります。
和文エンコーディングには`JY1`（pLaTeX）、`JY2`（upLaTeX）、`JY3`（LuaLaTeX）があります。

最近のLaTeXはUnicodeに対応しているので、
気にすることなく`TU`（と`JY3`）エンコーディングを利用すればよいです。

## フォントのファミリー

フォントの**ファミリー**とは**書体**のことです。

| コマンド名 | 書体 | 欧文／和文 |
|---|---|---|
| `\textrm{}` | ローマン体 / セリフ体 | 欧文 |
| `\textss{}` | サンセリフ体 | 欧文 |
| `\texttt{}` | タイプライタ体 / モノスペース体 | 欧文 |
| `\textmc{}` | 明朝体 | 和文 |
| `\textgt{}` | ゴシック体 | 和文 |
| `\textmg{}` | 丸ゴシック体 | 和文 |

## フォントのシリーズ

フォントの**シリーズ**は**太さ**のことです。
**ウェイト**と呼ぶこともあります。

| コマンド名 | シリーズ |
|---|---|
| `\textlt{}` | Light |
| `\textmd{}` | Medium （デフォルト） |
| `\textbf{}` | Bold |
| `\textbx{}` | Bold Extended |
| `\texteb{}` | Extra Bold |

## フォントのシェープ

フォントの**シェープ**とは**字体**のことです。

| コマンド名 | シェープ |
|---|---|
| `\textup{}` | upright体 / 立体 |
| `\textit{}` | italic体 / 斜体|
| `\textsl{}` | slanted体 |
| `\textsc{}` | SmallCaps体 |

[\emph{}コマンド](./latex-emph.md)のように、欧文では強調に*italic*を使用します。
和文フォントは*イタリック*に対応したものが少ないため、あまり使わないかもしれません。

:::{note}

指定したフォントがイタリックに対応していない場合は
通常フォントを強制的に斜めにした**擬似イタリック体**が使用されます。

[fontspecパッケージ](./latex-fontspec.md)で
`FakeSlant`オプションを使うことで擬似イタリックを明示的に適用できます。
:::
