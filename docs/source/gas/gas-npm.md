# npmを使いたい（`npm`）

```console
$ brew install node

$ node --version
v20.9.0

$ npm --version
10.2.5
```

`TypeScript` → `rollup` → `clasp`という開発チェーンは、
すべて`npm`パッケージとして配布されています。
`brew install node`で`Node.js`をインストールすると、
`npm`（パッケージ管理コマンド）と`npx`（一時実行コマンド）が一緒に使えるようになります。

`npm`コマンド自体の詳しい使い方は[パッケージ管理したい（`npm`）](../command/command-npm.md)を参照してください。
本ページでは、GASの開発環境という文脈での使い方に絞って説明します。

## 一時的に実行したい（`npx`）

```console
$ npx @google/clasp create-script --title "My Project"
```

パッケージをグローバルにインストールせずに一度だけ実行したい場合は`npx`が使えます。
新規プロジェクトの作成のような、頻繁には使わないコマンドを試すときに便利です。
[`clasp`](./gas-clasp.md)自体は後述のとおりローカルまたはグローバルにインストールして使うことが多いですが、
「まず動かしてみたい」ときは`npx`から始めるのも手軽です。

:::{note}

`npx`コマンドを使うにはネットワーク環境が必要です。

:::

## グローバル or ローカル（プロジェクト）

```console
// グローバルにインストール（PCのどこからでも使える）
$ npm install -g typescript

// ローカルにインストール（このプロジェクトの中だけで使える）
$ npm install --save-dev typescript
```

GAS開発でよく使う`typescript`・`rollup`・`clasp`などのツールは、
プロジェクトごとにバージョンを固定したいことが多いため、
`--save-dev`（開発用の依存パッケージ）で**ローカル**にインストールするのが基本です。
ローカルにインストールしたコマンドは、`npm run`や`npx`経由で実行します。

```console
$ npx tsc --noEmit
$ npx rollup -c
$ npx clasp push
```

一方、後述する「補完・更新チェック用のツール」のように、
どのプロジェクトでも横断的に使う便利ツールは、**グローバル**にインストールしておくと使い勝手がよいです。

## グローバルにインストールしておくとよいツール

```console
$ npm -g install all-the-package-names
$ npm -g install npm-check-updates
```

[all-the-package-names](https://www.npmjs.com/package/all-the-package-names)を追加すると、
`npm install`時にパッケージ名を補完してくれるようになります。

[npm-check-updates](https://www.npmjs.com/package/npm-check-updates)を追加すると、
プロジェクトの`package.json`にあるパッケージの更新有無を簡単に確認できます。

```console
$ ncu
typescript  ^5.3.0  ->  ^5.4.0
rollup      ^4.9.0  ->  ^4.10.0

// package.jsonを一括更新
$ ncu -u
$ npm install
```

これらはGAS開発に限らず便利なツールなので、`-g`を付けてグローバルにインストールしておくとよいです。

## リファレンス

- [パッケージ管理したい（`npm`）](../command/command-npm.md)
- [npm Docs](https://docs.npmjs.com/)
