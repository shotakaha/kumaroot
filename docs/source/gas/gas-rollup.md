# バンドルしたい（`rollup`）

```console
$ rollup -c
$ rollup -c --watch
```

`rollup`は、JavaScript/TypeScriptをひとつのファイルにまとめるツールです。
GAS本体はモジュール化した構造を扱うことができません。
ローカルでモジュール開発し、GASにデプロイする前に`rollup`でひとつにまとめるという作業フローになります。

## インストールしたい（`rollup`）

```console
// devDependenciesに追加
$ npm install --save-dev rollup @rollup/plugin-node-resolve @rollup/plugin-typescript
```

`rollup`本体と関連するパッケージは`devDependencies`（`--save-dev`）としてプロジェクトに追加すればOKです。

`@rollup/plugin-node-resolve`は`node_modules`内のパッケージを解決するプラグイン、
`@rollup/plugin-typescript`はTypeScriptを直接読み込んでバンドルするプラグインです。

## スクリプト設定したい（`package.json`）

```json
{
    "name": "...",
    "...": "...",
    "scripts": {
        "bundle": "rollup -c",
        "bundle:watch": "rollup -c --watch",
        "...": "..."
    }
}
```

`npm scripts`の`bundle`と`bundle:watch`を設定したサンプルです。

```console
$ npm run bundle
$ npm run bundle:watch
```

それぞれ`npm run bundle`、`npm run bundle:watch`で実行できます。
`tsc`による型チェック（[`tsc --noEmit`](./gas-typescript.md)）と役割が分かれるように、
`build`ではなく`bundle`という名前にしています。

## 設定したい（`rollup.config.js`）

```js
import { nodeResolve } from "@rollup/plugin-node-resolve";
import typescript from "@rollup/plugin-typescript";

export default {
    input: "src/index.ts",
    output: {
        file: "gas/code.bundle.js",    // .clasp.jsonと同じディレクトリに出力
        format: "iife",    // GAS向けにIIFE形式でまとめる
        name: "myLib",
        sourcemap: true,
    },
    plugins: [
        nodeResolve(),
        typescript({ declaration: false, outDir: undefined }),
    ],
};
```

`rollup.config.js`で`rollup`を設定できます。

`typescript()`プラグインが、`tsconfig.json`の設定を読みつつ`.ts`ファイルを直接読み込んでバンドルします。
`tsc`を別途実行してJavaScriptに変換しておく必要はありません。

:::{note}

`tsconfig.json`側で`outDir`や`declaration`（型定義ファイルの出力）を指定していても、
`rollup`でバンドルする際は不要になるため、プラグインのオプションで打ち消しておくと安全です。

:::
