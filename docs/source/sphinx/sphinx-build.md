# ドキュメントの生成（``make BUILDER``）

ドキュメントを生成するには{command}`make`コマンドを使います。

```bash
$ cd docs
$ make             # ヘルプを表示
$ make html        # HTMLを生成
$ make latexpdf    # PDFを生成
$ make linkcheck   # リンクを確認
```

## ウェブページを生成する

ウェブページを生成するときは``make html``を実行します。
生成したファイルは ``build/html/`` 以下に出力されます。
URLはいわゆる``UglyURL``の形式で生成されます。

```bash
$ cd $KUMAROOT
$ make html
$ open build/html/index.html
```

``PrettyURL``にした場合は``dirhtml``ビルダーを使います。

```bash
$ cd $KUMAROOT
$ make dirhtml
$ open build/dirhtml/index.html
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
詳しくは[](../latex/latex-usage.md)を参照してください。
```

## 例：KumaROOTをビルドする

例として、この``KumaROOT``のドキュメントをビルドする方法を書いておきます。

```bash
$ git clone https://github.com/shotakaha/kumaroot.git
$ cd kumaroot
$ poetry install  # 開発環境のセットアップ
$ poetry shell    # 開発環境の立ち上げ
$ cd docs/
$ make html       # HTMLの生成
$ make latexpdf   # PDFの生成
```

```{note}
開発環境のセットアップに ``poetry`` を使っています。
あらかじめインストールが必要です。
詳しくは[](../python/python-poetry.md)を参照してください。
```
