# ドキュメントを生成したい（``make BUILDER``）

```bash
$ make help
```

ドキュメントの生成には{command}`make`コマンドを使います。
{command}`make help`コマンドで、利用可能なビルダーを確認できます。
それぞれのビルダーの基本設定はすべて{file}`conf.py`にまとめて記述します。

```bash
$ cd $MyPROJECT/docs/
$ make             # ヘルプを表示
$ make html        # HTMLを生成
$ make latexpdf    # PDFを生成
$ make linkcheck   # リンクを確認
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
