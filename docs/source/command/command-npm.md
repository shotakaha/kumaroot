# パッケージ管理したい（`npm`）

```console
$ brew install node

$ node --version
v26.7.0

$ npm --version
11.19.0

$ npx --version
11.19.0
```

`npm`コマンドを使ってNodeパッケージを管理できます。
一時的にパッケージを利用するための`npx`コマンドもあります。

:::{note}

`npx`コマンドを使うにはネットワーク環境が必要です。

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
$ npm install --save-dev パッケージ名
$ npm install -D パッケージ名
```

`--save-dev`（`-D`）オプションを付けると、`package.json`の`devDependencies`にパッケージが記録されます。
テストツールやビルドツールなど、開発時にだけ必要でプロジェクトの実行には不要なパッケージに使います。

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

## オススメのパッケージ

```console
$ npm -g install all-the-package-names
$ npm -g install npm-check-updates
```

[all-the-package-names](https://www.npmjs.com/package/all-the-package-names)を追加すると、
インストール時にパッケージ名を補完してくれるようになります。

[npm-check-updates](https://www.npmjs.com/package/npm-check-updates)を追加すると、
`npm outdated`よりも簡単に、`package.json`ごと最新バージョンへ一括更新できるようになります。

```console
$ ncu
$ ncu -u
$ npm install
```

これらのパッケージは、グローバルに追加しておくとよいです。
