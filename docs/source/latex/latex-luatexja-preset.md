# 和文フォントしたい（`luatexja-preset`）

```latex
% プリアンブル
\usepackage[haranoaji]{luatexja-preset}    % TeXLive 2020のデフォルト
\usepackage[ipaex]{luatexja-preset}
\usepackage[sourcehan]{luatexja-preset}
\usepackage[hiragino-pro, hiragino-pron]{luatexja-preset}
```

`luatexja-preset`で、プリセットされた和文フォントを設定できます。
[luatex-fontspecパッケージ](./latex-luatexja-fontspec.md)の設定を1行で指定できます。

## 多書体したい（`deluxe`）

```latex
% プリアンブル
\usepackage[deluxe]{luatexja-preset}
\usepackage[deluxe,フォント名]{luatexja-preset}
```

`deluxe`オプションで、明朝3ウェイト（l/m/b）、ゴシック3ウェイト（m/b/eb）、丸ゴシック1ウェイト（mg）の7書体を設定できます。

## 原ノ味フォントしたい（`haranoaji`）

```latex
% プリアンブル
\usepackage[haranoaji]{luatexja-preset}

% TeXLive2020以降はデフォルト
\usepackage{luatexja-preset}
```

`haranoaji`オプションで原ノ味フォント（2004字形）を設定できます。
TeXLive2020以降はデフォルトのフォントになっているため、省略できます。

## IPAexフォントしたい（`ipaex`）

```latex
% プリアンブル
\usepackage[ipaex]{luatexja-preset}
```

## ヒラギノしたい（`hiragino-pron`）

```latex
% プリアンブル
\usepackage[deluxe, hiragino-pron]{luatexja-preset}
```

`hiragino-pron`オプションでヒラギノフォント（2004字形）を設定できます。
ヒラギノフォントはmacOSにプリインストールされています。

## BIZ UDしたい（`bizud`）

```latex
% プリアンブル
\usepackage[bizud]{luatexja-preset}
```

`bizud`オプションでBIZ UDゴシック／明朝を設定できます。
BIZ UDはWindows 10のデフォルトフォントです。

## 字形したい（`jis2004` / `jis90`）

```latex
% JIS2004字形（JIS X 0213:2004）
\usepackage[jis2004]{luatexja-preset}

% JIS90字形（JIS X 0208:1990）
\usepackage[jis90]{luatexja-preset}
```

`jis2004`、`jis90`オプションで字形を変更できます。
とくに理由がなければ`jis90`を選ぶ必要はありません。

## 依存パッケージ

```console
$ kpsewhich luatexja-preset.sty | xargs cat | rg RequirePackage
\RequirePackage{expl3,l3keys2e}
\RequirePackage{luatexja}
  \RequirePackage{luatexja-fontspec}
```
