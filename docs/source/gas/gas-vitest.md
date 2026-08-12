# ユニットテストしたい（`vitest`）

```console
$ npx vitest run
$ npx vitest
```

`vitest`はViteベースの高速なユニットテストフレームワークです。
TypeScriptにネイティブ対応しているため、`ts-jest`のような別プラグインなしでそのまま使えます。

`vitest run`は1回だけ実行して終了します。
引数なしの`vitest`はウォッチモードで起動し、ファイルの変更を検知して自動的に再実行します。

## インストールしたい

```console
$ npm install --save-dev vitest @vitest/coverage-v8
```

`vitest`本体と、カバレッジ計測用の`@vitest/coverage-v8`を`devDependencies`に追加します。

## スクリプト設定したい（`package.json`）

```json
{
    "name": "...",
    "scripts": {
        "test": "vitest run",
        "test:watch": "vitest",
        "test:coverage": "vitest run --coverage",
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
用途に応じて使い分けます。

## 設定したい（`vitest.config.ts`）

```ts
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    globals: true,
    environment: "node",
    include: ["**/__tests__/**/*.test.ts"],
    setupFiles: ["__tests__/setup.ts"],
    coverage: {
      provider: "v8",
      include: ["src/**/*.ts"],
    },
  },
});
```

`globals: true`にすると、`describe`・`test`・`expect`・`vi`などを
`import`せずにそのままグローバルに使えるようになります。
`jest`から移行する場合、書き方を大きく変えずに済むので便利です。

`environment: "node"`は、テストを実行する環境の指定です。
GASにはブラウザDOMがないため、`node`を指定します。

`include`でテスト対象のファイルパターンを、
`setupFiles`でテスト実行前に共通で読み込むファイルを指定します。

`coverage`でカバレッジ計測の設定ができます。
`provider: "v8"`は、Node.js（V8エンジン）に組み込まれたカバレッジ計測機能を使う設定です。

## GASのグローバルをモックしたい（`__tests__/setup.ts`）

```ts
// GASのグローバルオブジェクトをモックする
/// <reference types="google-apps-script" />

(global as any).Logger = {
  log: vi.fn(),
  clear: vi.fn(),
};

(global as any).console = {
  log: vi.fn(),
  info: vi.fn(),
  warn: vi.fn(),
  error: vi.fn(),
};
```

`DriveApp`や`SpreadsheetApp`、`Logger`のようなGASのグローバル変数は、
Node.js環境（`vitest`の実行環境）には存在しません。
テストを実行する前に、`setupFiles`で指定したファイルの中で、
必要な分だけ`vi.fn()`でモックしておく必要があります。

:::{hint}

すべてのGASサービスを一度にモックする必要はありません。
テスト対象のコードが実際に呼び出している範囲だけモックすれば十分です。

:::

## ユニットテストしたい

```ts
import { Counter } from "../src/counter";

describe("Counter", () => {
  describe("constructor", () => {
    test("should create counter with default settings", () => {
      const counter = new Counter();
      expect(counter.getValue()).toBe(0);
    });
  });

  describe("increment", () => {
    let counter: Counter;

    beforeEach(() => {
      counter = new Counter();
    });

    test("should increment the value", () => {
      expect(counter.increment()).toBe(1);
    });
  });
});
```

`describe`でテスト対象をグループ化し、`test`（`it`のエイリアス）で個々のテストケースを書きます。
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

## リファレンス

- [Vitest](https://vitest.dev/)
- [Vitest - Coverage](https://vitest.dev/guide/coverage.html)
