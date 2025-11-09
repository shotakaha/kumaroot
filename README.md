# KumaROOT

**くまのためのROOT入門 ／ ROOT for Bearginner**

ROOTなどの高エネルギー物理学分野で使っているツールの使い方をまとめているドキュメントです。
もともとは古巣の研究室に設置した[ShotakahaDokuWiki](https://www-he.scphys.kyoto-u.ac.jp/member/shotakaha/dokuwiki/doku.php)（アクセス不可）でまとめていた内容で、
現在は[KumaROOT - Read the Docs](https://kumaroot.readthedocs.io/ja/latest/)で公開&更新しています。

## 「くまROOT」：プロジェクト名の由来？

僕が研究室に入りROOTを使いはじめたときに、先輩から最初に渡されたのが「猿にも使えるROOT」（通称：さるROOT）でした。
そのタイトルを意識して「くま」にしました。
「さるROOT」の次は「くまROOT」を読んでもらえるように頑張りたいと思います。

想定している読者は、ちょっとだけROOTを使ったことがある学生／研究者です。
パッケージやクラスの網羅的な説明は公式ドキュメントに任せ、
こでは「〇〇したい」という目的ベースで整理することで、
「逆引き辞典」として使えるものを目指したいと思います。

## 公開版（Read the Docs）

- [HTML](https://kumaroot.readthedocs.org)
- [PDF](https://readthedocs.org/projects/kumaroot/downloads/)
- [GitHub Pages](https://shotakaha.github.io/kumaroot/)

### Read the Docsで公開する方法

- Read the Docsににログインして[dashboard](https://readthedocs.org/dashboard/)を開く
- プロジェクトの``KumaROOT``を選択
- ``ビルド``タブを開く
- ``ビルドバージョン:``をクリックする

### 個人ページで公開する方法

- ``make latexpdf``してPDFを作成する
- 作成したPDFを``source/_static/``にコピーする
- ``make html``してウェブページを作成する
- リモートサーバーに``rsync --delete -auvz``でアップロードする

```console
$ poetry run bash deploy.sh
```

## このドキュメントについて

このドキュメントは
[Sphinx](https://sphinx-users.jp)というドキュメト作成ソフトを使っています。
文書本体には``reStructuredText（reST）``と``Markdown（md）``という軽量マークアップ言語を使っています。

### セットアップ

```console
$ git clone git@github.com:shotakaha/kumaroot.git
$ cd kumaroot
$ poetry install --no-root
$ poetry shell
```

1. GitHubのリポジトリをクローンする
2. ``poetry``を使って依存パッケージをインストールする

### 新規にコンテンツを作成する場合

```console
$ cd kumaroot
$ git branch ブランチ名
$ git switch ブランチ名
$ code .
// docs/source/ツール名/ツール名-usage.mdを編集する
// docs/source/ツール名/ツール名-コンテンツ名.mdを新規作成する
$ git add 編集したファイル
$ git commit
$ git push
// GitHub上：Pull Requestを作成する
// GitHub上：テストをパスしたら即マージする
```

1. ``main``リポジトリからブランチを作成する
2. ``ツール名/ツール名-usage.md``の``toctree``にファイル名を追加する
3. ``ツール名/ツール名-コンテンツ名.md``を作成する
4. 変更箇所を``git add`` & ``git commit``
5. GitHubに``git push``し、プルリクエストを作成する
6. 自動テストをパスしたら即マージする

## ライブプレビューする場合

```console
$ cd kumaroot
$ poetry shell
(.venv) $ cd docs
(.venv) $ make livehtml  # 自動でブラウザが開く
```

1. ``poetry shell``で仮想環境を立ち上げる
2. ``make livehtml``でライブリロードしながら編集内容を確認する

### VS Codeを使ってライブプレビューする場合

```console
$ cd kumaroot
$ code .
```

1. Poetry設定で ``virtualenvs.in-project = true`` が前提
2. KumaROOTのリポジトリでVS Codeを起動する
3. VS Code内でターミナルを開く（``command + j``）

```console
(.venv) $ cd docs
(.venv) $ make livehtml
```

3. ``make livehtml``でライブリロードしながら編集する

## バージョン管理

バージョン番号は
[カレンダーバージョニング](https://calver.org/)と
[セマンティックバージョニング](https://semver.org/lang/ja/)を
組み合わせて使うことにしました。

- `Major` : 年
- `Minor` : 月
- `Patch (feat / fix)` : 文章を修正した場合

バージョンアップするタイミングは気まぐれです。
とりあえず月1回くらいにしようかな。

### バージョン管理タスク

```bash
task bump:patch
```

変更がある程度貯まったらパッチバージョンを更新してください。

```bash
task bump:minor
```

毎月1度、マイナーバージョンを更新してください。

```bash
task changelog
```

バージョンをバンプしたあとは`CHANGELOG.md`を更新してください。

## 依存パッケージの管理

```bash
$ poetry export -f requirements.txt --output requirements.txt
```

Read the Docsでビルドする際に、``requirements.txt``を使って必要なパッケージを取得しています。
なので、パッケージを更新したら``requirements.txt``も更新する必要があります。
``poetry export``のサブコマンドで生成し、Gitにコミットします。

## ファイルの命名規則

コンテンツのファイル名は、次のような命名規則で管理することにしています。

```text
docs/source/ツール名/ツール名-内容.md
```

### 例：ツールのインデックス

ツールのインデックスは``ツール名/ツール名-usage.md``にします。
このファイルに``toctree``を記載しています。

```md
root/root-usage.md
sphinx/sphinx-usage.md
python/pyhton-usage.md
pandas/pandas-usage.md
```

### 例：ツールのインストール方法

ツールのインストール方法は``ツール名/ツール名-install.md``としています。

```md
root/root-install.md
sphinx/sphinx-install.md
python/python-install.md
pandas/pandas-install.md
```

### 例：ツールの使い方

ツールの使い方は「やりたいこと」を軸にファイルを分けることにします。
とりあえず作成してみて、あとで分割／統合して整理しなおすこともあります。

```md
sphinx/sphinx-theme.md
python/python-pathlib.md
command/command-find.md
```

### 例：ツールの説明画像

ごくまれにツールの使い方を説明した画像やスクリーンショットを使っています。
ツールの中に``fig``とう画像用のディレクトリを作成し、その中で管理するようにしています。

```md
emacs/fig/mac-key01.png
emacs/fig/mac-key02.png
git/fig/git-status.png
```
