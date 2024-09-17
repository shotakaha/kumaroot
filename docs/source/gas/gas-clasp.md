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

## プロジェクトしたい

```console
$ clasp create --title PROJECT_NAME
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
./appsscript.json
```

`clasp create`でプロジェクトを新規作成できます。
``--title`でプロジェクトのタイトルを設定できます。
``--type``でプロジェクトの種類を選択できます。

:::{note}

GASには、Google Sheetなどのアプリに紐づいた状態のものと、どのアプリとも紐づいていない`standalone`のものがあります。（それぞれ呼び方があった気がするので、あとで確認する）

:::

## リファレンス

- [google/clasp - GitHub](https://github.com/google/clasp)
