# ユニットテストしたい（`jest`）

```console
$ npx jest
$ npx jest --watch
```

`jest`はJavaScript用のユニットテストフレームワークです。
ゼロコンフィグに近い設定で使い始められます。

:::{note}

以前は本サイトの作例プロジェクト（`gaslamp`）でも`jest`（＋`ts-jest`）を使っていましたが、
現在は[`vitest`](./gas-vitest.md)に移行しています。
新しくTypeScriptのGASプロジェクトを始める場合は、
`vitest`のほうがTypeScriptにネイティブ対応していて設定も少なく済むためオススメです。
`jest`はまだ広く使われているツールなので、参考として本ページも残しています。

:::

## インストールしたい

```console
$ npm install --save-dev jest
```

`jest`本体を`devDependencies`として追加します。

## スクリプト設定したい（`package.json`）

```json
{
    "name": "...",
    "scripts": {
        "test": "jest",
        "test:watch": "jest --watch",
        "test:coverage": "jest --coverage",
        "...": "..."
    }
}
```

```console
$ npm test
$ npm run test:watch
$ npm run test:coverage
```

`test`は1回実行、`test:watch`はウォッチモード、`test:coverage`はカバレッジ計測付きで実行します。

## 設定したい（`jest.config.js`）

```js
/** @type {import('jest').Config} */
module.exports = {
    testEnvironment: "node",
    testMatch: ["**/__tests__/**/*.test.js"],
    setupFilesAfterEnv: ["<rootDir>/__tests__/setup.js"],
    collectCoverageFrom: [
        "src/**/*.js",
        "!**/node_modules/**",
        "!**/coverage/**",
    ],
};
```

`testEnvironment`は、テストを実行する環境の指定です。
GASにはブラウザDOMがないため、`node`を指定します。

`testMatch`で対象となるユニットテスト用のファイルを設定します。
指定を忘れると、テスト以外のファイル（`setup.js`など）まで
テストファイルとして扱われてエラーになることがあるので注意してください。

`setupFilesAfterEnv`で、Jest実行時に共通して読み込むファイルを設定できます。

`collectCoverageFrom`でカバレッジ測定の対象とするファイルを指定します。

## GASのグローバルをモックしたい（`__tests__/setup.js`）

```js
// GASのグローバルオブジェクトをモックする
global.Logger = {
  log: jest.fn(),
  clear: jest.fn(),
};
```

`DriveApp`や`SpreadsheetApp`、`Logger`のようなGASのグローバル変数は、
Node.js環境（`jest`の実行環境）には存在しません。
テストを実行する前に、`setupFilesAfterEnv`で指定したファイルの中で、
必要な分だけ`jest.fn()`でモックしておく必要があります。

## ユニットテストしたい

```js
const { Counter } = require("../src/counter");

describe("Counter", () => {
  describe("constructor", () => {
    test("should create counter with default settings", () => {
      const counter = new Counter();
      expect(counter.getValue()).toBe(0);
    });
  });

  describe("increment", () => {
    let counter;

    beforeEach(() => {
      counter = new Counter();
    });

    test("should increment the value", () => {
      expect(counter.increment()).toBe(1);
    });
  });
});
```

`describe`でテスト対象をグループ化し、`test`で個々のテストケースを書きます。
`describe`は入れ子にできるので、以下のような構造を意識して作成するとよいです。

- テストするクラス名
  - テストするメソッド1
    - 正常系テストたち
    - 異常系テストたち
  - テストするメソッド2
    - 正常系テストたち
    - 異常系テストたち

`beforeEach`で、各テストの実行前に共通のセットアップ処理を行えます。

:::{hint}

テストケースを自分で考えるのは大変です。
最近はClaudeに、アップロードしたソースコードを読み込んでもらい、
それに対するユニットテストを作ってもらうようにしています。

:::

## TypeScriptに対応したい（`ts-jest`）

```console
$ npm install --save-dev ts-jest @types/jest
```

`.ts`ファイルをそのままテストできるようにする`ts-jest`と、
`describe`・`test`・`expect`などの型定義を提供する`@types/jest`を追加します。

```js
const { createDefaultPreset } = require("ts-jest");

const tsJestTransformCfg = createDefaultPreset().transform;

/** @type {import('jest').Config} */
module.exports = {
    testEnvironment: "node",
    transform: {
        ...tsJestTransformCfg,
    },
    testMatch: ["**/__tests__/**/*.test.ts"],
    setupFilesAfterEnv: ["<rootDir>/__tests__/setup.ts"],
    collectCoverageFrom: [
        "src/**/*.ts",
        "!**/node_modules/**",
        "!**/coverage/**",
    ],
};
```

`transform`は、`.ts`ファイルをテスト実行前にコンパイルする設定です。
`ts-jest`が提供する`createDefaultPreset()`を使うのが現在の推奨方法です。
`testMatch`・`setupFilesAfterEnv`・`collectCoverageFrom`の拡張子を`.ts`に変えるだけで、
JS版の設定とほぼ同じ形になります。

:::{caution}

`ts-jest`の設定方法は`preset: "ts-jest"`と書く古い書き方をよく見かけますが、
最近のバージョンでは非推奨になっています。
`createDefaultPreset()`を使う書き方に変わっているので、
古い記事のサンプルをそのまま使うと警告が出ることがあります。

:::

:::{hint}

`tsconfig.json`の`types`を明示的に絞っている場合、
`"jest"`を含めておかないと`describe`や`test`、`expect`が型エラーになります。
また`setupFilesAfterEnv`内で`global`（Node.jsのグローバルオブジェクト）を使う場合は、
`"node"`も忘れずに含めてください（`"types": ["jest", "node"]`）。

:::

## リファレンス

- [Jest](https://jestjs.io/)
- [ts-jest](https://kulshekhar.github.io/ts-jest/)
