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
ここでは「〇〇したい」という目的ベースで整理することで、
「逆引き辞典」として使えるものを目指したいと思います。

## 公開版（Read the Docs）

- [HTML](https://kumaroot.readthedocs.io/ja/latest/)
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
$ uv run bash deploy.sh
```

## このドキュメントについて

このドキュメントは
[Sphinx](https://sphinx-users.jp)というドキュメント作成ソフトを使っています。
文書本体には``reStructuredText（reST）``と``Markdown（md）``という軽量マークアップ言語を使っています。

### セットアップ

```console
$ git clone git@github.com:shotakaha/kumaroot.git
$ cd kumaroot
$ uv sync --all-extras
$ source .venv/bin/activate
```

1. GitHubのリポジトリをクローンする
2. ``uv``を使って依存パッケージをインストールする

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

```bash
task docs:serve
```

`task docs:serve`は自動的にdocsディレクトリに移動し、ライブリロードでドキュメントのプレビューを開始します。

### VS Codeを使ってライブプレビューする場合

```console
$ task code
```

`task code`はVS Codeを起動します。
VS Code内でターミナルを開き（`command + j`）、`task docs:serve`を実行してライブプレビューを開始できます。

### ドキュメントビルドタスク

```bash
task docs:serve      # Preview docs locally with live reload
task docs:build      # Build docs as static HTML
task docs:pdf        # Build docs as PDF
```

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
task bump:check
```

次のバージョンバンプをプレビューします。実際には変更を行いません。

```bash
task bump:patch
```

変更がある程度貯まったらパッチバージョンを更新してください。
バージョンバンプ時に`CHANGELOG.md`が自動的に更新されます。

```bash
task bump:minor
```

毎月1度、マイナーバージョンを更新してください。
バージョンバンプ時に`CHANGELOG.md`が自動的に更新されます。

```bash
task bump:major
```

毎年、メジャーバージョンを更新してください。
通常は年が変わるときに実行します。

## Pre-commitフック

```bash
task pre-commit:setup
```

`task pre-commit:setup`でpre-commitフックをインストールします。

```bash
task pre-commit
```

`task pre-commit`で全ファイルに対してpre-commitフックを実行します。

```bash
task pre-commit:update
```

`task pre-commit:update`でpre-commitフックを最新バージョンに更新できます。

## 依存パッケージの管理

```bash
task deps:setup
```

`task deps:setup`でPython環境をセットアップできます。

```bash
task deps:check
```

`task deps:check`で更新が利用可能な依存パッケージを確認できます。

```bash
task deps:update
```

`task deps:update`で依存パッケージを更新できます。
更新された`uv.lock`をGitにコミットしてください。

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
python/python-usage.md
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
ツールの中に``fig``という画像用のディレクトリを作成し、その中で管理するようにしています。

```md
emacs/fig/mac-key01.png
emacs/fig/mac-key02.png
git/fig/git-status.png
```
