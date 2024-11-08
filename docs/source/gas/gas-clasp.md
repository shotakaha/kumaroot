# CLASPしたい

```console
$ clasp pull
$ clasp run 関数名
$ clasp push
```

`clasp`は、Google Apps Scriptをローカル環境で管理できるコマンドです。
また、`clasp run`でコマンドラインからGASを操作できます。

ブラウザ上で編集していたGASのソースコードを
ローカルに持ってくることができるため、
Gitによるバージョン管理と組み合わせることも
できるようになります。

## インストールしたい（``clasp``）

```console
$ npm install -g @google/clasp
```

`npm`を使って`clasp`をインストールします。

:::{note}

`@google/clasp`は2022年9月26日の2.4.2の公開以降、開発が停滞しているようです。

:::

## ログインしたい（``clasp login``）

```console
$ clasp login
Logging in globally...
Authorize clasp by visiting this url:
// => ブラウザが起動する
// => ログインするGoogleアカウントを選択する
// => claspによるアクセス権限を選択する
// => （すべて）を選択して「続行」

Authorization successful.
Default credentials saved to: ~/.clasprc.json
```

GASを操作するために、Googleアカウントへのログインが必要です。
`clasp login`でブラウザが起動したら、
ログインするGoogleアカウントの選択と、
`clasp`に与えるアクセス権限を選択します。
認証に成功すると、認証トークンが`~/.clasprc.json`に保存されます。

## 新規プロジェクトしたい（``clasp create``）

```console
$ clasp create --title PROJECT_NAME --rootDir .
? Create which script?
❯ standalone
  docs
  sheets
  slides
  forms
  webapp
  api
Creating new script: PROJECT_NAME
Created new standalone script: https://script.google.com/d/スクリプトID/edit/
Cloned 1 file.

$ ls -la
.clasp.json
appsscript.json
```

`clasp create`でプロジェクトを新規作成できます。
`--title`でプロジェクトのタイトルを設定できます。
このオプションは、新しいディレクトリを作成するものではなく、ブラウザの編集ページのタイトルです。

`--rootDir`でプロジェクトのパスを設定できます。
デフォルトは、カレントディレクトリまでの絶対パスになってしまうので、`.`を指定するとよいと思います。

また``--type``でプロジェクトの種類を選択できます。
省略するとプロンプトが表示されるので矢印キーで選択します。

`.clasp.json`にスクリプトID（プロジェクトID）と、
`rootDir`の情報が保存されます。
基本的に1つのプロジェクトに1つの`.clasp.json`が対応します。

:::{note}

GASには、Google Sheetなどのアプリに紐づいた状態のものと、どのアプリとも紐づいていない`standalone`のものがあります。（それぞれ呼び方があった気がするので、あとで確認する）

:::

:::{caution}

1つの`.clasp.json`に複数のプロジェクトを追加することはできないみたいです。

:::

## 既存プロジェクトしたい（`clasp clone`）

```console
// ディレクトリを作成する
$ mkdir PROJECT_NAME
$ cd PROJECT_NAME

// 既存プロジェクトをクローンする
$ clasp clone スクリプトID
$ clasp clone スクリプトID --rootDir .
Cloning files...
Cloned 2 files.

$ ls -la
.clasp.json
appsscript.json
testDoGet.js     # ウェブ上で作成済みのスクリプト
```

`clasp clone`でGAS上にある既存のプロジェクト（スクリプト）をローカルにクローンできます。
スクリプトIDはURLに含まれているランダムな文字列です。

:::{note}

スクリプトIDがよくわからない、もしくは、
URLからわざわざ抜き出すのがめんどくさい、という場合は、
コピペしたURLをそのまま貼り付けてもOKみたいです。

:::

## ブラウザで開きたい（``clasp open``）

```console
// プロジェクト情報（.clasp.json）を参照
$ clasp open

// スクリプトID
$ clasp open スクリプトID
```

`clasp open`でブラウザが起動します。
`.clasp.json`に保存されているスクリプトIDの編集ページを開くことができます。

## プロジェクトを更新したい（``clasp pull`` / ``clasp push``）

```console
// ウェブからプロジェクトを取得
$ clasp pull
$ clasp pull --versionNumber バージョン  # バージョン指定

// プロジェクトを更新
$ clasp push
$ clasp push -w    # --watchモード
```

``pull``と``push``を使って、ローカルとリモートのプロジェクトをやりとりします。

## バージョン管理したい（`clasp version` / `clasp versions`）

```console
// バージョンを確認
$ clasp versions
~ 4 Versions ~
1 - v0.1.1
2 - v0.1.2
3 - v0.1.3
4 - v0.1.4

// アノテーションをつけてバージョン管理
$ clasp version "v0.1.5"

$ clasp versions
~ 5 Versions ~
1 - v0.1.1
2 - v0.1.2
3 - v0.1.3
4 - v0.1.4
5 - v0.1.5
```

`clasp version "アノテーション"`でバージョン管理できます。
GAS内のバージョン番号は自動でインクリメントされます。
あとで確認しやすいようにアノテーションにGitのタグ番号を含めておくとよさそうです。

`clasp versions`で、これまでに作成したバージョンを確認できます。
一度作成したバージョンは削除できません。

## デプロイ管理したい（`clasp deploy` / `clasp deployments`）

```console
// デプロイIDを確認
$ clasp deployments
1 Deployments.
- AKfycb...9Qm8gE @HEAD

// 作成済みバージョン番号を指定してデプロイ
$ clasp deploy --version 1 --description "v0.1.1"

// デプロイIDを確認
$ clasp deployments
2 Deployments.
- AKfycb...9Qm8gE @HEAD
- AKfycb...LH8l3z @1 - v0.1.1

// デプロイを削除
$ clasp undeploy AKfycb...LH8l3z
```

`clasp deploy`でデプロイするバージョンを管理できます。
`--version`には、`clasp version`で作成したバージョン番号を指定します。
`--description`でアノテーションを追加できます。

`clasp deployments`でデプロイIDを確認できます。
またバージョン管理と異なり`clasp undeploy`でデプロイを削除できます。

:::{note}

`--version`によるバージョン指定を省略した場合は、
自動インクリメントされたバージョン番号が追加され、割り当てられます。
バージョンが追加されたことは`clasp versions`で確認できます。

:::

## Git管理したい

- ディレクトリ構成

```text
リポジトリ名
|-- プロジェクト名
|    |-- main.js
|    |-- module1.js
|    |-- module2.js
|-- .git/
|-- node_modules/
|-- package.json
```

リポジトリの中にGASプロジェクト用のディレクトリを作成すると、
リポジトリ内を散らけずに管理できます。
また、関連するGASプロジェクトが増えた場合も、簡単に追加できます。

- ワークフロー

```console
//////////////////////////////////////////////////
// 初回の準備
//////////////////////////////////////////////////

// ディレクトリを作成する
$ mkdir リポジトリ名
$ mkdir リポジトリ名/プロジェクト名

// claspをローカルに追加
$ cd リポジトリ名
$ npm install @google/clasp
// --> package.jsonやnode_modulesが作成される

// Gitする
$ git init
$ touch .gitignore
// node_modules などを追加する

// 既存プロジェクトをクローンする
$ cd プロジェクト名
$ clasp clone スクリプトID --rootDir .
$ ls -la
.clasp.json
appsscript.json
既存スクリプト.js

// スクリプトをGitに追加する
$ git add appsscript.json
$ git add 既存スクリプト.js

// プロジェクト情報は場合によりけり
$ git add .clasp.json

//////////////////////////////////////////////////
// 編集
// - 普段どおり開発しGit管理する
// - 編集したファイルの同期を忘れないようにする
//////////////////////////////////////////////////

// ブラウザで編集した内容を取り込む
$ clasp pull

// ローカルで編集した内容を反映させる
$ clasp push

//////////////////////////////////////////////////
// バージョン管理
// - Gitでタグ管理する
// - GASのバージョン（のアノテーション）はGitタグを基準にする
// - GASのデプロイはオプションでもよい
//////////////////////////////////////////////////

// タグを作成
$ git tag "0.1.2"
$ git push origin --tags
$ git tag -l
0.1.1
0.1.2

// GASのバージョン管理
$ clasp version "v0.1.2"
$ clasp versions
~ 2 Versions ~
1 - v0.1.1
2 - v0.1.2

// （オプション）GASのデプロイ管理
$ clasp deploy --version 2 --description "v0.1.2"
$ clasp deployments
3 Deployments.
- AKfycb...9Qm8gE @HEAD
- AKfycb...LH8l3z @1 - v0.1.1
- AKfycb...itf33M @2 - v0.1.2
```

既存のGASプロジェクトをGitで管理するためのセットアップ手順を整理しました。

ポイントとして、
リポジトリの中にGASプロジェクトごとのサブディレクトリ（`PROJECT_NAME`）を作成し、
その中で`clasp clone --rootDir .`しています。

こうすることで、1つの`.clasp.json`とプロジェクトの対応をキープすることができ、関連するプロジェクトが複数個に増加した場合にも対応できます。

## リファレンス

- [google/clasp - GitHub](https://github.com/google/clasp)
