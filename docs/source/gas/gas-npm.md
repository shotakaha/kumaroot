# npmを使いたい（`npm`）

```console
$ brew install node

$ node --version
v20.9.0

$ npm --version
10.2.5
```

`npm`はNodeパッケージの管理ツールです。
Homebrewで`node`をインストールすると使えるようになります。
このとき`npx`コマンドもインストールされます。

本ページでは、GASの開発環境という文脈での使い方に絞って説明します。

## 一時的に実行したい（`npx`）

```console
$ npx @google/clasp create-script --title "My Project"
```

`npx`は、ローカルまたはグローバルにインストールされていないパッケージを一時的に実行するコマンドです。
実行時にはネットワーク接続が必要です。

:::{note}
はじめて使うパッケージなど、「まず動かしてみたい」ときに`npx`を使ってみるとよいです。
:::

## グローバルにインストールしたい（`npm install -g`）

```console
$ npm -g install all-the-package-names
$ npm -g install npm-check-updates
```

`npm install -g`で、グローバル（＝システム全体）にパッケージをインストールできます。

よく使うパッケージや、プロジェクトごとにバージョン管理が必要ないパッケージは、グローバルにインストールしておくと便利です。

## ローカルにインストールしたい（`npm install`）

```console
// ローカルにインストール
$ npm install --save-dev typescript @types/google-apps-script
$ npm install --save-dev rollup @rollup/plugin-node-resolve @rollup/plugin-typescript
$ npm install --save-dev @google/clasp
$ npm install --save-dev vitest @vitest/coverage-v8
$ npm install --save-dev @biomejs/biome
$ npm install --save-dev typedoc
```

`npm install`で、プロジェクトごとにパッケージをインストールできます。
インストールしたパッケージは`package.json`に記録されます。
`--save-dev`（`-D`）オプションをつけると、開発用の依存パッケージとして記録されます。
ローカルにインストールしたコマンドは、`npm run`や`npx`経由で実行できます。

:::{note}
プロジェクトごとにバージョンを管理したいパッケージは、ローカルにインストールするのが基本です。
GAS開発でよく使う`typescript`、`rollup`、`clasp`などのツールは、ローカルにインストールすればOKです。
:::

## パッケージ設定したい（`package.json`）

```json
{
    "name": "my-gas-project",
    "version": "0.0.1",
    "private": true,
    "type": "module",
    "engines": {
        "node": ">=20"
    },
    "packageManager": "npm@10.2.5",
    "devDependencies": {
        "typescript": "^5.4.0",
        "@types/google-apps-script": "^1.0.0"
    }
}
```

`package.json`は、プロジェクトの設定と依存パッケージをまとめて管理するファイルです。
`npm install`（`npx create...`系のコマンドを含む）を実行すると自動生成され、
以降の`npm install パッケージ名`はこのファイルを更新します。

`name`と`version`はプロジェクトの名前とバージョンです。
GASスクリプトをnpmパッケージとして公開する予定がなければ、あまり気にしなくてよい項目です。

`private: true`は、誤って`npm publish`で公開してしまわないようにするための安全装置です。
GAS用のプロジェクトは公開する必要がないので、基本的に`true`にしておきます。

`type: "module"`は、`.js`ファイルをESModule（`import`/`export`）として扱う指定です。
`rollup.config.js`のように、設定ファイル自体がESModule形式で書かれている場合に必要になります。

`devDependencies`には、`npm install --save-dev`でインストールしたパッケージとバージョンが記録されます。
`npm install`だけを実行すると、この一覧をもとに`node_modules`が再現されます。

:::{hint}

`package.json`は手で編集してもよいですが、
`npm install`・`npm uninstall`のようなコマンド経由で更新していくほうが、
書き間違いも減り安全です。

:::

`engines`は、動作確認済みのNode.jsバージョンを示すための項目です。

:::{caution}

`engines`はデフォルトでは警告が出るだけで、インストール自体は止まりません。
バージョン違反時に`npm install`を失敗させたい場合は、`.npmrc`に`engine-strict=true`を追加する必要があります。

:::

`packageManager`は、`npm`（や`yarn`/`pnpm`）自体のバージョンを固定するための項目です。
`corepack enable`を実行しておくと、`corepack`がこのバージョンを見て自動的にダウンロード・切り替えしてくれます。

:::{note}

`corepack`はNode.js 20/22 LTSには同梱されていますが、
Node.js 25以降は同梱されなくなる予定のため、`npm install -g corepack`で別途インストールが必要になる場合があります。

:::

## スクリプト設定したい（`package.json`）

```json
{
    "name": "...",
    "scripts": {
        "build": "tsc --noEmit",
        "bundle": "rollup -c",
        "bundle:watch": "rollup -c --watch",
        "push": "clasp push",
        "pull": "clasp pull",
        "deploy": "npm run build && npm run bundle && npm run push",
        "test": "vitest run",
        "test:watch": "vitest",
        "test:coverage": "vitest run --coverage",
        "format:check": "biome format .",
        "format:write": "biome format --write .",
        "lint:check": "biome lint .",
        "lint:fix": "biome lint --fix .",
        "docs:api": "typedoc"
    }
}
```

`npm scripts`に登録しておくと、`npx`や個別のコマンド名を直接打たなくても、
`npm run <スクリプト名>`（または`npm <スクリプト名>`）だけで実行できます。

```console
$ npm run deploy
$ npm test
$ npm run lint:fix
```

## リファレンス

- [パッケージ管理したい（`npm`）](../command/command-npm.md)
- [npm Docs](https://docs.npmjs.com/)
