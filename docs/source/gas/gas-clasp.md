# アップロードしたい（`clasp`）

```console
$ clasp push    # ローカル -> GAS
$ clasp pull    # GAS -> ローカル
```

`clasp`は、Google Apps Scriptをローカル環境で管理できるコマンドです。
`clasp push`でローカルからGAS環境にアップロードできます。
反対に`clasp pull`でGAS環境からローカルにダウンロードできます。
これによりGitによるバージョン管理と組み合わせることが
できるようになります。

## インストールしたい（`clasp`）

```console
$ npm install -g @google/clasp
```

`npm`を使って`clasp`をインストールします。

:::{note}

`@google/clasp`は2022年9月の2.4.2の公開以降、開発が停滞していましたが、2025年1月から開発が再開されたようです。
2025年10月に3.1.0がリリースされ、使い勝手が大きく変わりました。
コマンド名も大きく変わっているようなので、`clasp --help`で確認してください。

:::

## スクリプト設定したい（`package.json`）

```json
{
    "name": "...",
    "...": "...",
    "scripts": {
        "push": "clasp push",
        "pull": "clasp pull",
        "...": "..."
    }
}
```

`npm scripts`の`push`と`pull`を設定シタサンプルです。

```console
$ npm run push
$ npm run pull
```

それぞれ`npm run push`と`npm run pull`で実行できます。


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

:::{note}

`.clasprc.json`は認証トークンが含まれるため、Gitなどに含めてはいけません。

:::

## 新規プロジェクトしたい（`clasp create`）

```console
$ clasp create --title PROJECCT_NAME --type standalone --rootDir dist
```

`clasp create`でプロジェクトを新規作成できます。
`--title`でプロジェクトのタイトルを設定できます。
このオプションは、新しいディレクトリを作成するものではなく、ブラウザの編集ページのタイトルです。

また`--type`でプロジェクトの種類を選択できます。
省略するとプロンプトが表示されるので矢印キーで選択します。

:::{note}

GASには、Google Sheetなどのアプリに紐づいた状態のものと、どのアプリとも紐づいていない`standalone`のものがあります。（それぞれ呼び方があった気がするので、あとで確認する）

:::

`--rootDir`でGASにアップロードするファイルのパスを設定できます。
デフォルトは、`.`です。

:::{note}

`clasp` 3系では、TypeScriptからJavaScriptへ自動変換（トランスパイル）されなくなりました。
代わりに`rollup`などのバンドラーツールを併用する必要があります。
バンドルされたファイルは`dist`に生成するのが慣例となっているようなので、
`--rootDir dist`を指定しています。

:::

`.clasp.json`にスクリプトID（プロジェクトID）と、
`rootDir`の情報が保存されます。
基本的に1つのプロジェクトに1つの`.clasp.json`が対応します。

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
$ clasp open-script

// スクリプトID
$ clasp open-script スクリプトID

// v2
$ clasp open
```

`clasp open-script`で、ブラウザでGASエディターを開くことができます。
`.clasp.json`がある場合はスクリプトIDが自動で補完されます。

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

## デプロイ管理したい（`clasp create-deployment` / `clasp list-deployments`）

```console
// デプロイIDを確認
$ clasp list-deployments    # v2: clasp deployments
1 Deployments.
- AKfycb...9Qm8gE @HEAD

// 作成済みバージョン番号を指定してデプロイ
$ clasp create-deployment --version 1 --description "v0.1.1"    # v2: clasp deploy

// デプロイIDを確認
$ clasp list-deployments
2 Deployments.
- AKfycb...9Qm8gE @HEAD
- AKfycb...LH8l3z @1 - v0.1.1

// デプロイを削除
$ clasp delete-deployment AKfycb...LH8l3z    # v2: clasp undeploy
```

`clasp create-deployment|deploy`でデプロイするバージョンを管理できます。
`--version`には、`clasp version`で作成したバージョン番号を指定します。
`--description`でアノテーションを追加できます。

`clasp list-deployments|deployments`でデプロイIDを確認できます。
またバージョン管理と異なり`clasp delete-deployments|undeploy`でデプロイを削除できます。

:::{note}

`--version`によるバージョン指定を省略した場合は、
自動インクリメントされたバージョン番号が追加され、割り当てられます。
バージョンが追加されたことは`clasp list-versions`で確認できます。

:::

## Git管理したい

```tree
リポジトリ名
|-- CHANGELOG.md
|-- README.md
|-- dist/           # .gitignoreに追加
|   |-- appsscript.json
|   |-- code.js     # rollupでバンドルしたファイル
|-- node_modules/   # .gitignoreに追加
|-- package.json
|-- rollup.config.js    # rollupの設定
|-- tsconfig.json       # tscの設定
|-- src/            # TypeScriptファイル
|   |-- index.ts    # 自作モジュールのエントリーポイント
|   |-- config.ts   # 自作モジュールの設定用モジュール
|   |-- ...
|
|-- pyproject.toml  # commitizen, mkdocs など
|-- mkdocs.yml
|-- docs/           # ドキュメント用（オプション）
```

ディレクトリ構成のサンプルです。
`src`の中にTypeScriptファイルを作成し、
`rollup`でバンドルして`dist/code.js`に出力します。
`clasp push`されるのは`dist/`にあるファイルです。

:::{hint}

ドキュメント関係のファイルはオプションです。
コード内にTSDoc形式でコメントしておくと、`typedoc`でAPIドキュメントをMarkdown形式で出力できます。

:::

:::{note}

`pyproject.toml`があるのは、
僕がPython周りのツールのほうが使い慣れているためです。
`commitizen`、`pre-commit`、`mkdocs`などを使っています。

:::

## リファレンス

- [google/clasp - GitHub](https://github.com/google/clasp)
