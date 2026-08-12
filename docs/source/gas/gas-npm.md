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
$ npm install --save-dev typescript
$ npm install --save-dev rollup @rollup/plugin-node-resolve @rollup/plugin-typescript
$ npm install --save-dev @google/clasp
$ npm install --save-dev vitest
$ npm install --save-dev @biomejs/biome
$ npm install --save-dev typedoc
```

`npm install`で、プロジェクトごとにパッケージをインストールできます。
インストールしたパッケージは`package.json`に記録されます。
`--save-dev`オプションをつけると、開発用の依存パッケージとして記録されます。
ローカルにインストールしたコマンドは、`npm run`や`npx`経由で実行できます。

:::{note}
プロジェクトごとにバージョンを管理したいパッケージは、ローカルにインストールするのが基本です。
GAS開発でよく使う`typescript`、`rollup`、`clasp`などのツールは、ローカルにインストールすればOKです。
:::

## スクリプト設定したい（`package.json`）

```json
{
  "scripts": {
    "build": "npx tsc --noEmit",
    "bundle": "npx rollup -c",
    "bundle:watch": "npx rollup -c --watch",
    "push": "npx clasp push",
    "pull": "npx clasp pull",
    "deploy": "npm run build && npm run bundle && npm run push",
    "test": "npx vitest run",
    "test:watch": "npx vitest watch",
    "lint": "npx biome check",
    "lint:fix": "npx biome check --write",
    "docs:api": "npx typedoc"
  }
}
```

## リファレンス

- [パッケージ管理したい（`npm`）](../command/command-npm.md)
- [npm Docs](https://docs.npmjs.com/)
