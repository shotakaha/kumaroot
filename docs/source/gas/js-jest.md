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
