# パッケージ管理したい（`npm`）

```console
$ npm list
$ npm install
$ npm uninstall
$ npm test
$ npm run
```

`npm`は、Node.jsのパッケージ管理ツールです。
プロジェクトの`package.json`をもとに、依存パッケージのインストールや削除、スクリプトの実行などを行えます。

## インストールしたい（`node`）

```console
$ brew install node

$ node --version
v26.7.0

$ npm --version
11.19.0

$ npx --version
11.19.0
```

`npm`はHomebrewでインストールできます。
フォーミュラ名は`node`です。
`node`をインストールすると、`npm`と`npx`も同時にインストールされます。

:::{note}

`npx`コマンドを使うにはネットワーク環境が必要です。

:::

## グローバル設定したい

```console
$ npm install -g all-the-package-names
$ npm install -g npm-check-updates
$ npm install -g @google/clasp
```

`-g`オプションでグローバルにインストールしたパッケージは、プロジェクトを問わずコマンドとして使えるようになります。
CLIツールなど、複数のプロジェクトで共通して使いたいパッケージは、はじめにグローバルへ入れておくと便利です。

```console
$ npm -g list --depth=0
```

`-g`オプションと`list`コマンドを組み合わせると、グローバルにインストール済みのパッケージを確認できます。

[all-the-package-names](https://www.npmjs.com/package/all-the-package-names)を追加すると、
`npm install`時にパッケージ名を補完してくれるようになります。

[npm-check-updates](https://www.npmjs.com/package/npm-check-updates)を追加すると、
`npm outdated`よりも簡単に、`package.json`ごと最新バージョンへ一括更新できるようになります。

```console
$ ncu
$ ncu -u
$ npm install
```

[clasp](https://github.com/google/clasp)は、Google Apps Scriptのプロジェクトをローカルで開発するためのCLIツールです。
パッケージ名は`@google/clasp`です。

## パッケージ設定したい（`package.json`）

```json
{
    "name": "my-project",
    "version": "0.0.1",
    "private": true,
    "type": "module",
    "engines": {
        "node": ">=20"
    },
    "packageManager": "npm@11.19.0",
    "dependencies": {},
    "devDependencies": {}
}
```

`package.json`は、プロジェクトの設定と依存パッケージをまとめて管理するファイルです。
`npm init`を実行すると自動生成され、以降の`npm install`はこのファイルを更新します。

`name`と`version`はプロジェクトの名前とバージョンです。
npmパッケージとして公開する予定がなければ、あまり気にしなくてよい項目です。

`private: true`は、誤って`npm publish`で公開してしまわないようにするための安全装置です。

`type: "module"`は、`.js`ファイルをESModule（`import`/`export`）として扱う指定です。
省略した場合はCommonJS（`require`）として扱われます。

:::{note}

比較的新しいNode.jsでは、`type`を省略していても`.js`ファイルの中身が`import`/`export`構文であれば、
警告を出しつつ自動的にESModuleとして解釈し直してくれる場合があります（`require`構文のファイルはそのままCommonJSとして動きます）。
ただし、この自動判定には実行時のオーバーヘッドがあるため、警告にしたがって`type: "module"`を明示しておくのが安全です。

:::

`dependencies`には`npm install`（オプションなし）でインストールしたパッケージ、
`devDependencies`には`npm install --save-dev`でインストールしたパッケージが記録されます。
`npm install`だけを実行すると、これらの一覧をもとに`node_modules`が再現されます。

`engines`は、動作確認済みのNode.jsバージョンを示すための項目です。

:::{caution}

`engines`はデフォルトでは警告が出るだけで、インストール自体は止まりません。
バージョン違反時に`npm install`を失敗させたい場合は、`.npmrc`に`engine-strict=true`を追加する必要があります。

:::

`packageManager`は、`npm`（や`yarn`/`pnpm`）自体のバージョンを固定するための項目です。
`corepack enable`を実行しておくと、`corepack`がこのバージョンを見て自動的にダウンロード・切り替えしてくれます。

:::{note}

`corepack`はNode.js 20/22 LTSには同梱されていますが、
Node.js 25以降は同梱されなくなったため、`npm install -g corepack`で別途インストールが必要になる場合があります。

:::

:::{hint}

`package.json`は手で編集してもよいですが、
`npm install`・`npm uninstall`のようなコマンド経由で更新していくほうが、
書き間違いも減り安全です。

:::

## スクリプト設定したい（`package.json`）

```json
{
    "name": "my-project",
    "scripts": {
        "build": "tsc",
        "test": "vitest run",
        "lint": "eslint .",
        "start": "node index.js"
    }
}
```

`scripts`フィールドに、よく使うコマンドを短い名前で登録しておけます。
登録したスクリプトは`npm run <スクリプト名>`で実行できます。

```console
$ npm run build
$ npm run test
$ npm run lint
```

:::{note}

`test`、`start`、`stop`、`restart`の4つは特別扱いされていて、
`npm run`を省略して`npm test`、`npm start`のように実行できます。
それ以外のスクリプト名は`npm run`が必須です。

:::

`&&`でつなげると、複数のスクリプトを順番に実行するスクリプトも作れます。

```json
{
    "scripts": {
        "build": "tsc",
        "test": "vitest run",
        "ci": "npm run build && npm run test"
    }
}
```

:::{hint}

同じコマンドを何度も打つより、目的ごとに`scripts`へ登録しておくと、
チームメンバー間でも実行方法を揃えやすくなります。
プロジェクトによって内部の実装（`tsc`か`babel`か、`jest`か`vitest`か）が違っても、
`npm run build`・`npm test`という呼び出し方だけ覚えておけば済むようになります。

:::

## パッケージを探したい（`npm search`）

```console
$ npm search キーワード
```

`search`コマンドで、npmレジストリからパッケージ名や説明にキーワードを含むパッケージを検索できます。

## パッケージの詳細を調べたい（`npm view`）

```console
$ npm view パッケージ名
$ npm info パッケージ名
```

`npm view`（`npm info`はそのエイリアス）で、パッケージのバージョンや依存関係、リポジトリのURLなどの詳細情報を確認できます。
インストール前にパッケージの中身を確認しておきたいときに使います。

:::{caution}

npmエコシステムでは、既存の人気パッケージの認証情報が乗っ取られたり、
タイポスクワッティング（似た名前の偽パッケージを紛れ込ませる手口）によって、
悪意のあるコードが配布されるサプライチェーン攻撃がたびたび発生しています。

見覚えのないパッケージや依存関係で入ってくるマイナーなパッケージを導入する前に、
`npm view パッケージ名 maintainers time.created`などでメンテナーや公開時期を確認するとよいです。
リポジトリのURLを開いて、実際のソースやスター数・Issueの様子を見ておくのも有効です。
`npm audit`で、既知の脆弱性が報告されているかも合わせて確認できます。

:::

## パッケージを追加したい（`npm install`）

```console
$ npm install パッケージ名
$ npm -g install パッケージ名
```

`install`コマンドでパッケージを追加できます。
追加したパッケージは`package.json`にも追記され、プロジェクト内の管理に利用できます。

`-g`オプションを使ってグローバルにインストールできます。
グローバルにインストールしたパッケージはPCのどこからでもコマンドとして使えるようになり、
プロジェクトごとにインストールしなおす必要がなくなります。
一方、プロジェクトごとにバージョンを固定したいパッケージ（`typescript`や`rollup`など）は、
`-g`を付けずにローカルへインストールするのが基本です。

:::{note}

`-g`オプションをつける位置は、`npm`のあとでも、`install`のあとでもよいです。

```console
$ npm -g install パッケージ名
$ npm install -g パッケージ名
```

:::

## 開発用としてインストールしたい（`--save-dev`）

```console
$ npm install --save-dev typescript
$ npm install --save-dev rollup
$ npm install --save-dev vitest
$ npm install --save-dev @biomejs/biome
```

`--save-dev`（`-D`）で、開発用の依存パッケージとしてインストールできます。
パッケージ名は`package.json`の`devDependencies`に記録されます。

テストツールやビルドツールなど、開発時にだけ必要でプロジェクトの実行には不要なパッケージに使います。

```console
$ npx tsc --version
$ npx rollup --version
$ npx vitest --version
$ npx biome --version
```

上記はGoogle Apps Scriptの開発でよく使うツールです。
ローカルにインストールしたパッケージは`npx`経由で実行できます。

## パッケージを削除したい（`npm uninstall`）

```console
$ npm uninstall パッケージ名
$ npm -g uninstall パッケージ名
```

`uninstall`コマンドでパッケージを削除できます。
`install`と同じように`-g`を付けると、グローバルにインストールしたパッケージを削除できます。

## インストール済みのパッケージを確認したい（`npm list`）

```console
$ npm list
$ npm list --depth=0
$ npm -g list --depth=0
```

`list`コマンドで、インストール済みのパッケージを確認できます。
依存関係も含めてすべて表示されるため、直接インストールしたパッケージだけを見たい場合は`--depth=0`を付けます。

## パッケージの更新を確認したい（`npm outdated`）

```console
$ npm outdated
```

`outdated`コマンドで、インストール済みのパッケージに新しいバージョンがあるかを確認できます。
現在のバージョン・`package.json`が許容する最新バージョン・実際の最新バージョンが一覧表示されます。
