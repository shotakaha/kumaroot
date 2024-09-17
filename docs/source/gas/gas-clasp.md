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

::

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
認証に成功すると、認証情報が`~/.clasprc.json`に保存されます。

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
``--title`でプロジェクトのタイトルを設定できます。
``--rootDir``でプロジェクトのパスを設定できます。
デフォルトは、カレントディレクトリまでの絶対パスになってしまうので、`.`を指定するとよいと思います。

また``--type``でプロジェクトの種類を選択できます。
省略するとプロンプトで聞かれます。

スクリプトID（プロジェクトID）と、
`rootDir`の情報は`.clasp.json`に保存されます。

:::{note}

GASには、Google Sheetなどのアプリに紐づいた状態のものと、どのアプリとも紐づいていない`standalone`のものがあります。（それぞれ呼び方があった気がするので、あとで確認する）

:::

## 既存プロジェクトしたい（`clasp clone`）

```console
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
URLから抜き出すのがめんどくさい、という場合、
URLをそのまま貼り付けてもOKみたいです。

:::

## ブラウザで開きたい（``clasp open``）

```console
$ clasp open
// ブラウザが起動する
```

`clasp open`でブラウザが起動します。
`.clasp.json`に保存されているスクリプトIDの編集ページを開くことができます。

## Git管理したい

```console
// リポジトリを作成する
$ mkdir PROJECT_NAME
$ git init
$ mkdir GASCRIPT
$ cd GASCRIPT
$ clasp clone スクリプトID --rootDir .
$ ls -la
.clasp.json
appsscript.json
既存スクリプト.js
$ git add appsscript.json
$ git add 既存スクリプト.js
$ git add .clasp.json  // 場合による
```

既存のスクリプトをGit管理するための
セットアップ手順を整理しました。

ポイントは、プロジェクトの中に、
GASを管理するためのサブディレクトリ（`GASCRIPT`）を作成し、
その中でGASスクプトを`clasp`管理することにしました。
こうすることで`clasp`周りで自動で生成されるファイルが、
プロジェクトルートに散らばることを防ぐことができます。

## リファレンス

- [google/clasp - GitHub](https://github.com/google/clasp)
