# ドキュメントを生成したい（``sphinx-build``）

```bash
$ make help
```
d
ドキュメントの生成には[sphinx-build](https://www.sphinx-doc.org/ja/master/man/sphinx-build.html)を使いますが、
{file}`Makefile`が用意されているので、``make``コマンドを使います。
``make help``コマンドで、利用可能なビルダーを確認できます。
それぞれのビルダーの基本設定はすべて{file}`conf.py`にまとめて記述します。

```bash
# Makefileがあるディレクトリに移動する
$ cd $MyPROJECT/docs/

# ヘルプを表示する
$ make

# HTMLを作成する
$ make html

# PDFを作成する
$ make latexpdf

# リンクを確認する
$ make linkcheck
```

## 例：KumaROOTをビルドする

```bash
# GitHubにあるリポジトリをクローンする
$ git clone https://github.com/shotakaha/kumaroot.git
$ cd kumaroot

# 仮想環境を立ち上げる
$ poetry shell

# 必要なパッケージをインストールする
(.venv) $ poetry install
(.venv) $ cd docs/

# HTMLの生成
(.venv) $ make html

# PDFの生成
(.venv) $ make latexpdf
```

例として、この``KumaROOT``のドキュメントをビルドする方法を書いておきます。

```{note}
開発環境を整えるのに``poetry``を使っています。
あらかじめインストールが必要です。
詳しくは[](../python/python-poetry.md)を参照してください。
```
