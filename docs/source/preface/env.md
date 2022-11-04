# 開発環境

Sphinxをビルドしている環境は、以下のとおりです。

## Python環境

[Poetry](https://python-poetry.org/)を使って管理しています。

```bash
$ poetry env info
Virtualenv
Python:         3.10.7
Implementation: CPython
Path:           ~/repos/github/kumaroot/.venv
Executable:     ~/repos/github/kumaroot/.venv/bin/python
Valid:          True

System
Platform:   darwin
OS:         posix
Python:     3.10.7
Path:       /usr/local/opt/python@3.10/Frameworks/Python.framework/Versions/3.10
Executable: /usr/local/opt/python@3.10/Frameworks/Python.framework/Versions/3.10/bin/python3.10
```

## LaTeX環境

``Homebrew``を使ってMacTeXをインストールしています。

```bash
$ brew info mactex
==> mactex: 2022.0321
https://www.tug.org/mactex/
/usr/local/Caskroom/mactex/2022.0321 (4.6GB)
From: https://github.com/Homebrew/homebrew-cask/blob/HEAD/Casks/mactex.rb
==> Name
MacTeX
==> Description
Full TeX Live distribution with GUI applications
==> Artifacts
mactex-20220321.pkg (Pkg)
```

## Docker環境（予定）

（sphinxのイメージにpoetryを追加したものが作れたらいいのかもしれない）
