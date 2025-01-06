# パッケージ検索したい（`kpsewhich`）

```console
$ kpsewhich -version
kpathsea version 6.4.0


$ kpsewhich パッケージ名.sty
$ kpsewhich クラス名.cls
```

`kpsewhich`コマンドで、TeX関係のファイルを検索できます。
`パッケージ名.sty`、`クラス名.cls`のように拡張子が必要です。

:::{note}

`kpse`は、TeX関連のファイル検索に使われている`Kpathsearch`というライブラリのことだそうです。

:::

## 基本設定を確認したい（`texmf.cnf`）

```console
$ kpsewhich -all texmf.cnf
/usr/local/texlive/2024/texmf.cnf
/usr/local/texlive/2024/texmf-dist/web2c/texmf.cnf

$ cat /usr/local/texlive/2024/texmf.cnf
% (Public domain.)
% This texmf.cnf file should contain only your personal changes from the
% original texmf.cnf (for example, as chosen in the installer).
%
% That is, if you need to make changes to texmf.cnf, put your custom
% settings in this file, which is .../texlive/YYYY/texmf.cnf, rather than
% the distributed file (which is .../texlive/YYYY/texmf-dist/web2c/texmf.cnf).
% And include *only* your changed values, not a copy of the whole thing!
%
TEXMFHOME = ~/Library/texmf
TEXMFVAR = ~/Library/texlive/2024/texmf-var
TEXMFCONFIG = ~/Library/texlive/2024/texmf-config
```

TeXの基本設定は`texmf.cnf`に保存されています。
`kpsewhich`でそのパスを確認できます。

:::{note}

`find`や`mdfind`でも同様に検索できますが、TeX関連のファイルであれば`kspewhich`が効率的です。

:::
