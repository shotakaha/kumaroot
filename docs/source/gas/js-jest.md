# ユニットテストしたい（`jest`）

```console
$ npm install --save-dev jest
$ jest --help
```

`jest`はゼロコンフィグで利用できるJavaScript用のユニットテストです。
ユニットテスト用なので開発環境（`--save-dev`）のみにインストールします。
JSの機能だけであれば、GASプロジェクトにも導入できます。

## ディレクトリしたい（`__tests__`）

```console
$ tre -l 2
.
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
├── __tests__
│   ├── dataframe.constuctor.test.js
│   ├── dataframe.setup.js
│   ├── dataframe.static.test.js
│   ├── dataframe.test.js
│   ├── dataframe.to_arrays.test.js
│   ├── setup.js
│   └── typechecker.test.js
├── gaslamp/
│   ├── .clasp.json
│   ├── appsscript.json
│   ├── dataframe.js
│   ├── typechecker.js
│   └── warnings.js
├── jest.config.js
├── package-lock.json
├── package.json
```

個人で作成を進めている`gaslamp`プロジェクトにJestを導入しました。
メインのソースは`gaslamp/`に作成し、
ユニットテストは`__tests__/`に作成します。
また、`jest.config.js`でJestの設定や
`package.json`で`npm test`の動作を設定します。

## 設定したい（`jest.config.js`）

```js
module.exports = {
    preset: 'ts-jest',
    testEnvironment: 'node',
    testMatch: ['**/__tests__/**/*.test.js', '**/__tests__/**/*.test.ts'],
    setupFilesAfterEnv: ['<rootDir>/__tests__/setup.js'],
    collectCoverageFrom: [
        '**/*.{js,ts}',
        '!**/node_modules/**',
        '!**/coverage/**',
        '!**/jest.config.js'
    ],
    moduleFileExtensions: ['js', 'ts']
};
```

`gaslamp`の`jest.config.js`です。
`testMatch`で対象となるユニットテスト用のファイルを設定しています。
`setupFilesAfterEnv`で、Jest実行時に共通して読み込むファイルを設定できます。

`collectCoverageFrom`でカバレッジ測定の対象とするファイルを指定しています。
`node_modules/`や`coverage/`が保存されるディレクトリなどは除外しています。

## ユニットテストしたい

```js
describe('Test for モジュール名', () => {
    // 正常系
    describe('with normal cases', () => {
        test('正常系テスト1の内容', () => {
            // テストを書く
        });

        test('正常系テスト2の内容', () => {
            // テストを書く
        });

    });

    // 異常系
    describe('with edge cases', () => {
        test.todo('異常系テスト1の予定');
    });
})
```

ユニットテストには`describe(...)`でテストの説明を設定できます。
また`describe(...)`は入れ子にできます。
そのため、以下のような入れ子構造を意識して作成するとよいと思います。

- テストするモジュール名1
  - テストする関数1
    - 正常系テストたち
    - 異常系テストたち
  - テストする関数2
    - 正常系テストたち
    - 異常系テストたち
- テストするクラス名1
  - テストするメソッド1
    - 正常系テストたち
    - 異常系テストたち
  - テストするメソッド2
    - 正常系テストたち
    - 異常系テストたち

正常系テストと異常系テストのセクションを作成することで、
網羅的にテストを作成することがもできます。

:::{hint}

テストケースを自分で考えるのは大変です。
最近はClaudeに、アップロードしたソースコードを読み込んでもらい、
それに対するユニットテストを作ってもらうようにしています。

:::
