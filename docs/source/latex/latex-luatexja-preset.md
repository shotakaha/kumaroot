# 和文フォントしたい（`luatexja-preset`）

```latex
% プリアンブル（どれか1つを指定します）
\usepackage{luatexja-preset}
% \usepackage[haranoaji]{luatexja-preset}    % オプション省略時と同じ
% \usepackage[ipaex]{luatexja-preset}
% \usepackage[sourcehan]{luatexja-preset}
% \usepackage[hiragino-pro]{luatexja-preset}
```

`luatexja-preset`で、プリセットされた和文フォントを設定できます。
[luatexja-fontspecパッケージ](./latex-luatexja-fontspec.md)の設定を1行で指定できます。
デフォルトは`haranoaji`（原ノ味フォント・2004字形）です。

## 多書体したい（`deluxe`）

```latex
% プリアンブル
\usepackage[deluxe]{luatexja-preset}
\usepackage[deluxe, <プリセット名>]{luatexja-preset}
```

`deluxe`オプションで、明朝3ウェイト（l/m/b）、ゴシック3ウェイト（m/b/eb）、丸ゴシック1ウェイト（mg）の7書体を設定できます。
`<プリセット名>`には`haranoaji`、`hiragino-pron`などのプリセット名を指定します。
プリセットによっては明朝の細字（l）が用意されておらず、中字（m）で代用される場合があります。

## 原ノ味フォントしたい（`haranoaji`）

```latex
% プリアンブル
\usepackage[haranoaji]{luatexja-preset}
```

`haranoaji`オプションで原ノ味フォント（2004字形）を設定できます。
原ノ味フォントは`luatexja-preset`のデフォルトのフォントのため、オプションを省略できます。

## IPAexフォントしたい（`ipaex`）

```latex
% プリアンブル
\usepackage[ipaex]{luatexja-preset}
```

`ipaex`オプションでIPAexフォントを設定できます。
IPAexフォントは別途インストールが必要な場合があります。

## ヒラギノしたい（`hiragino-pro` / `hiragino-pron`）

```latex
% プリアンブル
\usepackage[deluxe, hiragino-pron]{luatexja-preset}
```

`hiragino-pro`はヒラギノ Pro、`hiragino-pron`はヒラギノ ProN（JIS2004対応）のフォントを設定します。
ヒラギノフォントはmacOSにプリインストールされています。
ただし、明朝体の細字（W2）はmacOSにバンドルされていないため、別途購入が必要です。

## BIZ UDしたい（`bizud`）

```latex
% プリアンブル
\usepackage[bizud]{luatexja-preset}
```

`bizud`オプションでBIZ UDゴシック／明朝を設定できます。
BIZ UDはWindows 10 October 2018 Update以降に付属しています。

## 字形したい（`jis2004` / `jis90`）

```latex
% JIS2004字形（JIS X 0213:2004）
\usepackage[jis2004]{luatexja-preset}

% JIS90字形（JIS X 0208:1990）
\usepackage[jis90]{luatexja-preset}
```

`jis2004`、`jis90`オプションで、パッケージが定義する明朝体・ゴシック体（丸ゴシック体を含む）の字形を切り替えます。
指定しない場合は、プリセットのデフォルトの字形になります。
両方を同時に指定した場合の動作は保証されていないため、どちらか一方だけを指定してください。
特別な理由がなければ、指定する必要はありません。

## 依存パッケージ

```console
$ kpsewhich luatexja-preset.sty | xargs cat | grep RequirePackage
\RequirePackage{expl3,l3keys2e}
\RequirePackage{luatexja}
  \RequirePackage{luatexja-fontspec}
```
