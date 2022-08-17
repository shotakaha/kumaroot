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

## 公開版

- Read the Docs : [HTML](https://kumaroot.readthedocs.org) / [PDF](https://kumaroot.readthedocs.io/_/downloads/ja/latest/pdf/)
- KEKの個人ページ : [HTML](https://research.kek.jp/people/shotakah/kumaroot/html/) / PDF（準備中）

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

```bash
poetry run bash deploy.sh
```

## このドキュメントについて

このドキュメントは
[Sphinx](https://sphinx-users.jp)というドキュメト作成ソフトを使っています。
文書本体には``reStructuredText（reST）``と``Markdown（md）``という軽量マークアップ言語を使っています。

## バージョン管理

なんとなく[セマンティックバージョニング](https://semver.org/lang/ja/)を使おうとしています。

- ``Major (feat)`` : 新しい章を追加した場合
- ``Minor (feat)`` : 新しい節を追加した場合
- ``Patch (fix)`` : 文章を修正した場合

## ファイルの命名規則

次のような命名規則でコンテンツを管理しています

### ツールのインデックス

- ``ツール名/ツール名-usage.md``にする

例

```md
root/root-usage.md
sphinx/sphinx-usage.md
python/pyhton-usage.md
pandas/pandas-usage.md
```

### ツールのインストール方法

- ``ツール名/ツール名-install.md``にする

例

```md
root/root-install.md
sphinx/sphinx-install.md
python/python-install.md
pandas/pandas-install.md
```

### ツールの詳細

- ``ツール名/ツール名-[章タイトル].md``にする
- ``[章タイトル]``はパッケージ名やメソッド名、クラス名などを想定している

例

```md
sphinx/sphinx-theme.md
python/python-pathlib.md
command/command-find.md
```

### ツールの説明画像

- ``ツール名/fig/ツール名-[章タイトル]-[連番].png``にする
- ツールの説明に必要なスクリーンショットは、ツールごとに作成した``fig``ディレクトリの中で管理する

```md
emacs/fig/mac-key01.png
emacs/fig/mac-key02.png
git/fig/git-status.png
```
