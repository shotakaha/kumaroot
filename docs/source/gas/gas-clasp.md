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

`@google/clasp`は2022年9月の2.4.2の公開以降、開発が停滞していましたが、2025年1月から開発が再開されました。
2025年10月に3.1.0がリリースされ、使い勝手が大きく変わりました。
本ページは3.3.0（2026年時点の最新版）を基準にしています。
コマンド名が2系から大きく変わっているので、迷ったら`clasp --help`で確認してください。

:::

:::{hint}

3系ではコマンドに`〇〇-script`や`〇〇-deployment`のような正式名と、
`clasp create`や`clasp deploy`のような短いエイリアスの両方が用意されています。
本ページでは正式名（エイリアス）の形式で表記します。

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

## 新規プロジェクトしたい（`clasp create-script`）

```console
$ clasp create-script --title PROJECT_NAME --type standalone --rootDir dist
```

`clasp create-script（create）`でプロジェクトを新規作成できます。
`--title`でプロジェクトのタイトルを設定できます。
このオプションは、新しいディレクトリを作成するものではなく、ブラウザの編集ページのタイトルです。

また`--type`でプロジェクトの種類を選択できます。
省略した場合は`standalone`になります。

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
$ clasp create-script --title PROJECT_NAME --rootDir .
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

## 既存プロジェクトしたい（`clasp clone-script`）

```console
// ディレクトリを作成する
$ mkdir PROJECT_NAME
$ cd PROJECT_NAME

// 既存プロジェクトをクローンする
$ clasp clone-script スクリプトID
$ clasp clone-script スクリプトID --rootDir .
Cloning files...
Cloned 2 files.

$ ls -la
.clasp.json
appsscript.json
testDoGet.js     # ウェブ上で作成済みのスクリプト
```

`clasp clone-script（clone）`でGAS上にある既存のプロジェクト（スクリプト）をローカルにクローンできます。
スクリプトIDはURLに含まれているランダムな文字列です。

:::{note}

スクリプトIDがよくわからない、もしくは、
URLからわざわざ抜き出すのがめんどくさい、という場合は、
コピペしたURLをそのまま貼り付けてもOKみたいです。

:::

## ブラウザで開きたい（`clasp open-script`）

```console
// プロジェクト情報（.clasp.json）を参照
$ clasp open-script

// スクリプトIDを指定
$ clasp open-script スクリプトID
```

`clasp open-script`で、ブラウザでGASエディターを開くことができます。
`.clasp.json`がある場合はスクリプトIDが自動で補完されます。

## プロジェクトを更新したい（`clasp pull` / `clasp push`）

```console
// ウェブからプロジェクトを取得
$ clasp pull
$ clasp pull --versionNumber バージョン    # バージョン指定
$ clasp pull -d    # --deleteUnusedFiles: リモートにないローカルファイルを削除

// プロジェクトを更新
$ clasp push
$ clasp push -w    # --watch: ファイル変更を監視して自動push
$ clasp push -f    # --force: マニフェスト（appsscript.json）を強制上書き
```

`pull`と`push`を使って、ローカルとリモートのプロジェクトをやりとりします。
`clasp pull -d, --deleteUnusedFiles`は、リモートに存在しないファイルをローカルからも削除するので注意して使ってください。

## バージョン管理したい（`clasp create-version` / `clasp list-versions`）

```console
// バージョンを確認
$ clasp list-versions    # エイリアス: clasp versions
~ 4 Versions ~
1 - v0.1.1
2 - v0.1.2
3 - v0.1.3
4 - v0.1.4

// アノテーションをつけてバージョン管理
$ clasp create-version "v0.1.5"    # エイリアス: clasp version

$ clasp list-versions
~ 5 Versions ~
1 - v0.1.1
2 - v0.1.2
3 - v0.1.3
4 - v0.1.4
5 - v0.1.5
```

`clasp create-version（version）"アノテーション"`でバージョン管理できます。
GAS内のバージョン番号は自動でインクリメントされます。
あとで確認しやすいようにアノテーションにGitのタグ番号を含めておくとよさそうです。

`clasp list-versions（versions）`で、これまでに作成したバージョンを確認できます。
一度作成したバージョンは削除できません。

## デプロイ管理したい（`clasp create-deployment` / `clasp list-deployments`）

```console
// デプロイIDを確認
$ clasp list-deployments    # エイリアス: clasp deployments
1 Deployments.
- AKfycb...9Qm8gE @HEAD

// 作成済みバージョン番号を指定してデプロイ
$ clasp create-deployment --versionNumber 1 --description "v0.1.1"    # エイリアス: clasp deploy

// デプロイIDを確認
$ clasp list-deployments
2 Deployments.
- AKfycb...9Qm8gE @HEAD
- AKfycb...LH8l3z @1 - v0.1.1

// デプロイを削除
$ clasp delete-deployment AKfycb...LH8l3z    # エイリアス: clasp undeploy

// 既存のデプロイを新しいバージョンに更新
$ clasp update-deployment AKfycb...LH8l3z --versionNumber 2    # エイリアス: clasp redeploy
```

`clasp create-deployment（deploy）`でデプロイするバージョンを管理できます。
`-V, --versionNumber`には、`clasp create-version`で作成したバージョン番号を指定します。
`-d, --description`でアノテーションを追加できます。

`clasp list-deployments（deployments）`でデプロイIDを確認できます。
またバージョン管理と異なり`clasp delete-deployment（undeploy）`でデプロイを削除できます。
`-a, --all`を付けるとすべてのデプロイを一括削除できます。

既存のデプロイをそのままに紐づくバージョンだけ差し替えたい場合は、
`clasp update-deployment（redeploy）`が使えます。

:::{note}

`--versionNumber`によるバージョン指定を省略した場合は、
自動インクリメントされたバージョン番号が追加され、割り当てられます。
バージョンが追加されたことは`clasp list-versions`で確認できます。

:::

## pushされるファイルを確認したい（`clasp show-file-status`）

```console
$ clasp show-file-status    # エイリアス: clasp status
└─ appsscript.json
└─ dist/code.js
```

`clasp show-file-status（status）`で、`clasp push`の対象になっているファイル一覧を確認できます。
`.claspignore`で除外したファイルは表示されないので、意図しないファイルが混ざっていないか事前にチェックできます。

## ログを確認したい（`clasp tail-logs`）

```console
// 直近のログを表示
$ clasp tail-logs    # エイリアス: clasp logs

// Cloud Loggingへの出力を有効化
$ clasp setup-logs
```

`clasp tail-logs（logs）`で、GAS実行時のログ（`Logger.log`や`console.log`の出力）を確認できます。
初回は`clasp setup-logs`でCloud Loggingとの連携設定が必要な場合があります。

## 関数を実行したい（`clasp run-function`）

```console
$ clasp run-function 関数名    # エイリアス: clasp run
```

`clasp run-function（run）`で、GASエディターを開かずにローカルから関数を実行できます。
初回実行時は`--use-project-scopes`付きで`clasp login`をやり直し、プロジェクトに必要な権限を認可する必要がある場合があります。

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

## コマンド名の新旧対応表

`clasp` 2系から3系でコマンド名が大きく変わりました。
2系の書き方が残っている記事も多いので、対応表としてまとめておきます。

| 2系 | 3系（正式名） | 3系（エイリアス） |
| --- | --- | --- |
| `clasp create` | `clasp create-script` | `clasp create` |
| `clasp clone` | `clasp clone-script` | `clasp clone` |
| `clasp delete` | `clasp delete-script` | `clasp delete` |
| `clasp open` | `clasp open-script` | - |
| `clasp deploy` | `clasp create-deployment` | `clasp deploy` |
| `clasp deployments` | `clasp list-deployments` | `clasp deployments` |
| `clasp undeploy` | `clasp delete-deployment` | `clasp undeploy` |
| （なし） | `clasp update-deployment` | `clasp redeploy` |
| `clasp version` | `clasp create-version` | `clasp version` |
| `clasp versions` | `clasp list-versions` | `clasp versions` |
| `clasp status` | `clasp show-file-status` | `clasp status` |
| `clasp logs` | `clasp tail-logs` | `clasp logs` |
| `clasp run` | `clasp run-function` | `clasp run` |
| `clasp login` | `clasp login` | - |
| `clasp logout` | `clasp logout` | - |
| `clasp push` | `clasp push` | - |
| `clasp pull` | `clasp pull` | - |

### 3系で追加された新しいコマンド

2系にはなかった、3系から追加されたコマンドです。

| コマンド（正式名） | エイリアス | 内容 |
| --- | --- | --- |
| `clasp open-credentials-setup` | - | スクリプトのGCPプロジェクトの認証情報ページを開く |
| `clasp enable-api <api>` | - | 指定したAPIを有効化する |
| `clasp disable-api <api>` | - | 指定したAPIを無効化する |
| `clasp list-apis` | `clasp apis` | 有効化されているAPI一覧を表示する |
| `clasp open-api-console` | - | GCPプロジェクトのAPIコンソールを開く |
| `clasp show-authorized-user` | - | 現在の認証状態を表示する |
| `clasp open-logs` | - | ブラウザでログ（開発者コンソール）を開く |
| `clasp setup-logs` | - | Cloud Loggingとの連携を設定する |
| `clasp open-container` | - | 紐づいたアプリ（Sheetsなど）のGASエディターを開く |
| `clasp open-web-app` | - | デプロイ済みのウェブアプリをブラウザで開く |
| `clasp list-scripts` | `clasp list` | Apps Scriptプロジェクトの一覧を表示する |
| `clasp start-mcp-server` | `clasp mcp` | Apps Script操作用のMCPサーバーを起動する |

:::{note}

これらは`clasp --help`で確認できるコマンドの一部です。
今後もバージョンアップで追加・変更される可能性があるので、迷ったら`clasp --help`で最新の一覧を確認してください。

:::

## リファレンス

- [google/clasp - GitHub](https://github.com/google/clasp)
