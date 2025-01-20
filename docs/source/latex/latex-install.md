```{eval-rst}
.. index::
    pair: LaTeX; install
```

# インストールしたい

```console
$ brew install --cask mactex

// MacTeXを更新
$ brew reinstall --cask mactex
```

Homebrewで`MacTeX`をインストールできます。
また、[MacTeX](https://tug.org/mactex/)からダウンロードできます。
年1回のTeXLiveの更新に合わせて、MacTeXも更新されます。

MacTeXには、LaTeX環境の本体であるTeXLiveと一緒に、統合開発環境であるTeXShopやTeXworks、文献管理のBibDesk、スペルチェックのExcalibur、そしてKeynoteに数式を貼り付けるのに必要なLaTeXiTなどのアプリが付属されています。

## トッピングしたい

```console
// TeXShop.appなどが不要な場合
$ brew install --cask mactex-no-gui

// 必要なアプリだけ追加
$ brew install --cask latexit
$ brew install --cask texshop
$ brew install --cask bibdesk
$ brew install --cask tex-live-utility
```

`mactex-no-gui`で、コアパッケージだけをインストールできます。
MacTeXに付属しているいくつかのアプリは、それぞれのフォーミュラがあります。
必要なパッケージだけをあとから追加することもできます。

## コマンドしたい

```console
$ which -a tlmgr
/Library/TeX/texbin/tlmgr

$ which -a latexmk
/Library/TeX/texbin/latexmk

$ which -a biber
/Library/TeX/texbin/biber

$  which -a chktex
/Library/TeX/texbin/chktex

$ which -a detex
/Library/TeX/texbin/detex
```

`/Library/TeX/texbin/`に主要なコマンドがあります。
あまりウェブに情報が落ちていないコマンドもあるので、一度眺めてみるとよいと思います。


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
