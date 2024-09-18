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

## プロジェクトの更新（``clasp pull`` / ``clasp push``）

```console
// ウェブからプロジェクトを取得
$ clasp pull
$ clasp pull --versionNumber バージョン  # バージョン指定

// プロジェクトを更新
$ clasp push
$ clasp push -w    # --watchモード
```

``pull``と``push``を使って、ローカルとリモートのプロジェクトをやりとりします。

## Git管理したい

```console
// リポジトリ用のディレクトリを作成する
$ mkdir REPOS_NAME
$ git init

// スクリプト用のディレクトリを作成する
$ mkdir PROJECT_NAME
$ cd PROJECT_NAME

// claspをローカルに追加
$ npm install @google/clasp
// node_modules などは .gitignoreに追加

// 既存プロジェクトをクローンする
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
```

既存のGASプロジェクトをGitで管理するための
セットアップ手順を整理しました。

ポイントとして、
リポジトリの中にGASプロジェクトごとのサブディレクトリ（`PROJECT_NAME`）を作成し、
その中で`clasp clone --rootDir .`しています。

こうすることで、1つの`.clasp.json`とプロジェクトの対応をキープすることができ、関連するプロジェクトが複数個に増加した場合にも対応できます。

## リファレンス

- [google/clasp - GitHub](https://github.com/google/clasp)
