# パッケージ管理したい（`npm`）

```console
$ npm run test    // npx vitest run
$ npm run lint    // npx biome lint .
$ npm run build   // npx tsc --noEmit
$ npm run bundle  // npx rollup -c
$ npm run push    // npx clasp push
```

GAS開発も`npm`を使ってパッケージ管理できます。
このページでは、GAS開発で利用する
`typescript`、`rollup`、`clasp`、`vitest`、`biome`、`typedoc`といったパッケージのインストール方法やスクリプト設定をまとめています。

:::{seealso}

それぞれのパッケージの詳しい使い方は、以下のページを参照してください。

- [](../command/command-npm.md)
- [](./gas-typescript.md)
- [](./gas-rollup.md)
- [](./gas-clasp.md)
- [](./gas-vitest.md)
- [](./gas-biome.md)
- [](./gas-typedoc.md)

:::

## インストールしたい（`npm install --save-dev`）

```console
$ npm install --save-dev typescript @types/google-apps-script
$ npm install --save-dev rollup @rollup/plugin-node-resolve @rollup/plugin-typescript
$ npm install --save-dev @google/clasp
$ npm install --save-dev vitest @vitest/coverage-v8
$ npm i -D --save-exact @biomejs/biome
$ npm install --save-dev typedoc
```

`--save-dev`オプションで、開発依存（`devDependencies`）としてパッケージを追加します。

## パッケージ設定したい（`package.json`）

```json
{
    "name": "my-gas-project",
    "version": "0.0.1",
    "private": true,
    "type": "module",
    "devDependencies": {
        "typescript": "^5.4.0",
        "@types/google-apps-script": "^1.0.0"
    }
}
```

`package.json`の各フィールドの意味は
[パッケージ管理したい（`npm`）](../command/command-npm.md)を参照してください。
GAS開発では、次の2点だけ意識しておくとよいです。

`private: true`は、誤って`npm publish`で公開してしまわないようにするための安全装置です。
GAS用のプロジェクトは公開する必要がないので、基本的に`true`にしておきます。

`type: "module"`は、`.js`ファイルをESModule（`import`/`export`）として扱う指定です。
`rollup.config.js`のように、設定ファイル自体がESModule形式で書かれている場合に必要になります。

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

`tsc` → `rollup` → `clasp`の3段階に、テスト（`vitest`）・フォーマッター／リンター（`biome`）・
APIドキュメント生成（`typedoc`）を組み合わせた、GAS開発一式の`scripts`設定例です。
各コマンドの意味や個別のオプションは、上記のリンク先ページで詳しく説明しています。

```console
$ npm run deploy
$ npm test
$ npm run lint:fix
```

## リファレンス

- [パッケージ管理したい（`npm`）](../command/command-npm.md)
- [npm Docs](https://docs.npmjs.com/)
