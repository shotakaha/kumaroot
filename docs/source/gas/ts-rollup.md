# バンドルしたい（`rollup`）

```console
$ rollup -c
$ rollup -c --watch
```

`rollup`は、JavaScript/TypeScriptをひとつのファイルにまとめるツールです。
GAS本体はモジュール化した構造を扱うことができません。
ローカルでモジュール開発し、GASにデプロイする前に`rollup`でひとつにまとめるという作業フローになります。

## 設定したい（`rollup.config.js`）

```console
// devDependenciesに追加
$ npm install --save-dev rollup @rollup/plugin-node-resolve @rollup/plugin-typescript
```

```js
import resolve from "@rollup/plugin-node-resolve";
import typescript from "@rollup/plugin-typescript";
import { defineConfig } from "rollup";

export default defineConfig({
    input: "src/index.ts",
    output: {
        file: "dist/code.js",
        format: "iife",
    }
    plugins: [resolve(), typescript()],
});
```

`rollup.config.js`で`rollup`を設定できます。
`rollup`本体と関連するパッケージは`devDepencencies`（`--save-dev`）としてプロジェクトに追加すればOKです。

## スクリプト設定したい（`package.json`）

```json
{
    "name": "...",
    "...": "...",
    "scripts": {
        "build": "rollup -c",
        "watch": "rollup -c --watch",
        "...": "..."
    }
}
```

`npm scripts`の`build`と`watch`を設定したサンプルです。

```console
$ npm run build
$ npm run watch
```

それぞれ`npm run build`、`npm run watch`で実行できます。
