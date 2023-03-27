# ドキュメント作成をはじめたい（``sphinx-quickstart``）

ドキュメント作成をはじめる場合は、Sphinxに付属している``sphinx-quickstart``を使います。
既存のプロジェクト内にドキュメント作成用として追加するケースが多いと思いますが、
{file}`MyPROJECT/docs/`のようにドキュメント用ディレクトリを用意するとよいです。

```bash
$ cd MyPROJECT
$ sphinx-quickstart docs
> Separate source and build directories (y/n) [n]:  # n でOK
> Project name: # プロジェクト名を入力する
> Author name(s): # 作成者名を入力する
> Project release []: # リリース番号を入力する（空欄でもOK）
> Project language [en]: ja # 日本語に設定
```

``sphinx-quickstart docs``を実行すると、
ドキュメントの初期化に必要な基本情報を入力するためのプロンプトが表示されます。
プロンプトに応じて必要な情報を入力します。
設定した内容は{file}`docs/conf.py`であとから書き換えればよいので、
適当に入力してしまっても大丈夫です。

すべてのプロンプトを入力し終えると``docs/``ディレクトリが作成されます。
ディレクトリの構造は次のようになっています。

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
``sphinx-quickstart``で最初に聞かれる「（ドキュメントの）ソース用とビルド用のディレクトリを分割するか？」だけは、あらかじめ検討しておくとよいと思います。
ディレクトリ構成に関することなので、後から変更するのが難しい（＝めんどくさい）です。
:::
