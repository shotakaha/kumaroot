# パッケージ管理したい（``npm``）

```console
$ brew install node

$ node --version
v20.9.0

$ npm --version
10.2.5

$ npx --version
10.2.5
```

``npm``コマンドを使ってNodeパッケージを管理できます。
一時的にパッケージを利用するための``npx``コマンドもあります。

:::{note}

``npx``コマンドを使うにはネットワーク環境が必要です。

:::

## パッケージを追加する（``install``）

```console
$ npm install パッケージ名
$ npm -g install パッケージ名
```

``install``コマンドでパッケージを追加できます。
追加したパッケージは``package.json``にも追記され、プロジェクト内の管理に利用できます。

``-g``オプションを使ってグローバルにインストールできます。

:::{note}

``-g``オプションをつける位置は、``npm``のあとでも、``install``のあとでもよいです。

```console
$ npm -g install パッケージ名
$ npm install -g パッケージ名
```

:::

## オススメのパッケージ

```console
$ npm -g install all-the-package-names
$ npm -g install npm-check-updates
```

[all-the-package-names](https://www.npmjs.com/package/all-the-package-names)を追加すると、
インストール時にパッケージ名を補完してくれるようになります。
[npm-check-updates](https://www.npmjs.com/package/npm-check-updates)を追加すると、
パッケージ更新の有無を簡単に確認できます。

これらのパッケージは、グローバルに追加しておくとよいです。
