# ドキュメントを生成したい（``make BUILDER``）

ドキュメントの生成には{command}`make`コマンドを使います。

```bash
$ cd docs
$ make             # ヘルプを表示
$ make html        # HTMLを生成
$ make latexpdf    # PDFを生成
$ make linkcheck   # リンクを確認
```

## ウェブページを生成したい（``make html``）

ウェブページを生成するときは{command}`make html`を実行します。
生成したファイルは{file}`build/html/`以下に出力されます。
URLはいわゆる``UglyURL``の形式で生成されます。

```bash
$ cd $KUMAROOT
$ make html
$ open build/html/index.html
```

``PrettyURL``にした場合は{command}``make dirhtml``を使います。

```bash
$ cd $KUMAROOT
$ make dirhtml
$ open build/dirhtml/index.html
```

## PDFを生成したい（``make latexpdf``）


PDFを生成するときは{command}`make latexpdf`を実行します。
生成したファイルは{file}`build/latex/`以下に出力されます。

```
$ cd $KUMAROOT
$ make latexpdf
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
