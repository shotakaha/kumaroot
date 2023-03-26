# ドキュメントを新規作成したい（``sphinx-quickstart``）

ドキュメントを新規作成するには{command}`sphinx-quickstart`を使います。
既存のプロジェクト内に追加することが多いと思いますが、
{file}`MyPROJECT/docs/`のようなドキュメント用ディレクトリを用意して、
その中で管理するとよいです。

```bash
$ cd MyPROJECT
$ sphinx-quickstart docs
> Separate source and build directories (y/n) [n]:  # n でOK
> Project name: # プロジェクト名を入力する
> Author name(s): # 作成者名を入力する
> Project release []: # リリース番号を入力する（空欄でもOK）
> Project language [en]: ja # 日本語に設定
```

{command}`sphinx-quickstart docs`を実行すると、
ドキュメントの基本情報を入力するためのプロンプトが表示されるので、
必要な情報を入力します。
設定した内容は{file}`docs/conf.py`であとから書き換えればよいので、
適当に入力してしまっても問題はありません。

すべてのプロンプトを入力し終えると``docs/``ディレクトリが作成されます。
ディレクトリの中は次のようになっています。

```bash
$ tree docs/
docs/
├── Makefile
├── _build/
├── _static/
├── _templates/
├── conf.py
├── index.rst
└── make.bat

3 directories, 4 files
```

この``docs/``直下にドキュメント用のファイルを作成します。
ビルドしたファイルは``_build/ビルダー名/``に作成されるので、
該当ファイルを開いてローカルで直接確認できます。

:::{tip}
``sphinx-quickstart``で最初の聞かれる「（ドキュメントの）ソース用とビルド用のディレクトリを分割するか？」だけは、あらかじめ検討しておくとよいと思います。
ディレクトリ構成に関することなので、後から変更するのが難しい（＝めんどくさい）です。
:::
