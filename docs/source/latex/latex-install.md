```{eval-rst}
.. index::
    pair: LaTeX; install
```

# インストール

つい最近までは「Mac LaTeX インストール」などでググると、なんだかまとまりのない情報で溢れていました。
しかし、現在はそれらを取りまとめようということで開発が進んでいるようで、これからはTeXLive一択で良いみたいです。
TeXLiveは年1回更新されます。

## MacTeX

macOSでLaTeXを使う場合は、これで決まりです。
[MacTeX](https://tug.org/mactex/)からダウンロードできます。

LaTeX環境の本体であるTeXLiveと一緒に、LaTeX編集の統合環境であるTeXShopやTeXworks、
LaTeX関連のパッケージ管理ツールであるTeX Live Utilityがついてきます。
他にも、文献管理のBibDesk、スペルチェックのExcalibur、そして、
Keynoteに数式を貼り付けるのに必要なLaTeXiTがついてきます。

## MacTeX (Homebrew)

```console
$ brew install --cask mactex
```

TeXLiveはHomebrew（{command}`brew`コマンド）を使ってインストールできます。

## TeXのディレクトリ構造

```text
/usr/local/texlive/2022/texmf-config
/usr/local/texlive/2022/texmf-var
/usr/local/texlive/2022/texmf-dist
/usr/local/texlive/texmf-local    # ユーザー設定
```

TeXLiveのバージョンごとの設定は、バージョンアップすると上書きされます。
自分用にカスタマイズした設定は{file}`/usr/local/texlive/texmf-local`に保存できます。

## パッケージを更新したい（``tlmgr``）

```console
$ tlmgr update --list
$ sudo tlmgr update --all
```

LaTeXパッケージを管理するコマンドです。
詳しくは[tlmgrコマンドの使い方](../command/command-tlmgr.md)を参照してください。
