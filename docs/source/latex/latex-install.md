```{eval-rst}
.. index::
    pair: LaTeX; install
```

# インストール

```console
$ brew install --cask mactex
```

TeXLiveはHomebrew（{command}`brew`コマンド）を使ってインストールできます。
TeXLiveは年1回更新されるので、新しいバージョンが公開されたら``brew reinstall --cask mactex``します。

:::{hint}

LaTeXは歴史があるため「Mac LaTeX インストール」などでググっても、なんだかまとまりのない情報で溢れています。
しかし、これからは**TeXLive一択**でよさそうです。

:::

## MacTeX

[MacTeX](https://tug.org/mactex/)からダウンロードできます。

LaTeX環境の本体であるTeXLiveと一緒に、LaTeX編集の統合環境であるTeXShopやTeXworks、LaTeX関連のパッケージ管理ツールであるTeX Live Utilityがついてきます。
他にも、文献管理のBibDesk、スペルチェックのExcalibur、そして、Keynoteに数式を貼り付けるのに必要なLaTeXiTがついてきます。

## カスタマイズしたい

```text
/usr/local/texlive/2022/texmf-config
/usr/local/texlive/2022/texmf-var
/usr/local/texlive/2022/texmf-dist
/usr/local/texlive/texmf-local    # ユーザー設定
```

上のディレクトリは、TeXLiveの設定関係のファイルが配置されています。
ディレクトリ名に**年**が含まれていることからわかるように、TeXLiveのバージョンごとに基本設定があります。
自分用の設定は{file}`/usr/local/texlive/texmf-local`に保存するとよいでしょう。

## パッケージを更新したい（``tlmgr``）

```console
$ tlmgr update --list
$ sudo tlmgr update --all
```

LaTeXパッケージを管理するコマンドです。
コマンドを途中でキャンセルすると、パッケージが中途半端な状態となるためか``skipping forcibly removed package``と表示されることがあります。
意図的に削除したパッケージでなければ``--reinstall-forcibly-removed``オプションで解決できます。

```console
$ sudo tlmgr update --all --reinstall-forcibly-removed
```

パッケージは[CTAN（Comprehensive TeX Archive Network）](https://www.ctan.org/)のリポジトリで公開されています。
詳しくは[tlmgrコマンドの使い方](../command/command-tlmgr.md)を参照してください。
パッケージの詳細を確認する方法は[texdocの使い方](../command/command-texdoc.md)を参照してください。
