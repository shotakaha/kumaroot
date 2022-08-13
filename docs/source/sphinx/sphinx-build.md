# ドキュメントの生成（``make BUILDER``）

ドキュメントを生成するには{command}`make`コマンドを使います。

```bash
$ cd docs
$ make             # ヘルプを表示
$ make html        # HTMLを生成
$ make latexpdf    # PDFを生成
```

## ウェブページを生成する

ウェブページを生成するときは``make html``を実行します。
生成したファイルは ``build/html/`` 以下に出力されます。

```bash
$ cd $KUMAROOT
$ make html
$ open build/html/index.html
```

## PDFを生成する


PDFを生成するときは``make latexpdf``を実行します。
生成したファイルは``build/latex/``以下に出力されます。

```
$ cd $KUMAROOT
$ make latexpdfja
$ open build/latex/KumaROOT.pdf
```

```{note}
PDFを生成する場合、ビルドするパソコンでLaTeX環境を整えておく必要があります。
詳しくは[](../latex/latex-usage.md)に整理することにします。
```

## 例：KumaROOTをビルドする

例として、この``KumaROOT``のドキュメントをビルドする方法を書いておきます。
開発環境のセットアップに ``poetry`` を使っているので、あらかじめインストールが必要です。

```bash
$ pip3 install poetry
```

```bash
$ git clone https://github.com/shotakaha/kumaroot.git
$ cd kumaroot
$ poetry install  # 開発環境のセットアップ
$ poetry shell    # 開発環境の立ち上げ
$ cd docs/
$ make html       # HTMLの生成
$ make latexpdf   # PDFの生成
```
