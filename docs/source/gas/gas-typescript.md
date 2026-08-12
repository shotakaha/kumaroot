# トランスパイルしたい（`tsc`）

```console
$ npx tsc
$ npx tsc src/main.ts
$ npx tsc --watch
```

`tsc`コマンドで、TypeScript（`.ts`）をJavaScript（`.js`）に変換するコマンドです。
`npx`経由で実行することが多いです。

設定ファイル（`tsconfig.json`）がある場合は、自動で読み込まれます。

## インストールしたい（`typescript`）

```console
$ npm install --save-dev typescript @types/google-apps-script
```

`typescript`パッケージを`devDependencies`として追加します。

`@types/google-apps-script`は、GASの型情報を使うための型定義パッケージです。
明示的なインポートは必要ありません（というか不可です）。

:::{note}

`devDependencies`にある`@types`パッケージはVS Codeが自動で認識して、補完／チェックしてくれるようです。

:::

`@types/google-apps-script`の中身は、`DriveApp`や`SpreadsheetApp`などのサービスごとに分かれた`.d.ts`ファイルの集まりです。
それぞれのファイルの中では、`GoogleAppsScript.Drive`や`GoogleAppsScript.Spreadsheet`のように、
サービス名の名前空間（`namespace`）の中に`File`や`Sheet`といった型が定義されています。

```ts
// GoogleAppsScript.Drive.File 型が返る
const files: GoogleAppsScript.Drive.FileIterator = DriveApp.getFiles();

// 変数に型注釈をつけたいときは GoogleAppsScript.<サービス名>.<型名> の形式で書く
function processFile(file: GoogleAppsScript.Drive.File): void {
  Logger.log(file.getName());
}
```

`DriveApp`や`SpreadsheetApp`のようなグローバル変数自体も、
`declare var DriveApp: GoogleAppsScript.Drive.DriveApp;`のように、
この名前空間の型を指す形でグローバルに宣言されています。
そのため`import`しなくても、`DriveApp.createFile(...)`のように直接呼び出すだけで型補完が効きます。

:::{hint}

具体的な型名がわからないときは、VS Codeで`DriveApp.getFiles()`のような呼び出しにカーソルを合わせ、
「定義へ移動」（Go to Definition）を使うと、対応する`.d.ts`ファイルと型名を直接確認できます。

:::

## 型チェックだけしたい（`tsc --noEmit`）

```console
$ npx tsc --noEmit
```

[`rollup`](./gas-rollup.md)を使う構成では、実際のトランスパイル・バンドルは`@rollup/plugin-typescript`が担当するため、
`tsc`単体でファイルを出力する必要はありません。
`--noEmit`を付けると、ファイル出力をせずに型チェックだけを実行できます。
`rollup`実行前のCIやコミット前のチェックとして使うと便利です。

## 型をつけたい

```ts
// 変数の定義
const 変数名: 型名 = 値

// 関数の定義
function 関数名(引数名: 型名): 戻り値の型名 {...}
```

`: 型名`で変数や関数の型を指定できます。
この型を使って、トランスパイルや静的解析で潜在的なエラーを検出します。

:::{note}

トランスパイルしたあとのJavaScriptには型の情報は残りません。

:::

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
        "...": "..."
    }
}
```

`build`で型チェックのみ、`bundle`で実際のトランスパイル・バンドルを行います。
紛らわしいですが、GASの世界では「ビルド＝型チェック」「バンドル＝1ファイルへのまとめ」と役割を分けるのが定番のようです。
`deploy`では、型チェック→バンドル→GASへのアップロードの順に実行しています。

## 設定したい（`tsconfig.json`）

```json
{
    "compilerOptions": {
        "target": "ES2020",    // GAS V8対応
        "module": "ESNext",    // rollupでバンドル前提
        "moduleResolution": "bundler",
        "lib": ["ES2020"],
        "rootDir": "src",    // ソースコードのルート
        "outDir": "gas",    // 出力先ディレクトリ（型チェックのみなら未使用）
        "esModuleInterop": true,
        "forceConsistentCasingInFileNames": true,
        "strict": true,    // 厳格な型チェック
        "skipLibCheck": true    // 依存パッケージの型チェックをスキップ
    },
    "include": [
        // トランスパイル対象
        "src/**/*"
    ],
    "exclude": [
        // トランスパイル対象外
        "node_modules",
        "gas"
    ]
}
```

`tsconfig.json`でTypeScriptのトランスパイルの設定ができます。
GASのV8ランタイムはECMAScript2020相当の機能までサポートしているため、それに合わせた設定にしています。
ここでは`rollup`でモジュールをバンドルし、
`clasp`でデプロイする前提でサンプルを作成しました。

`target`は、トランスパイルして出力されるJavaScriptのECMAScriptバージョンを指定するオプションです。
GAS V8ランタイムでは`"ES2020"`程度まで指定できます。

`module`は、トランスパイルするときに利用するモジュール形式を指定するオプションです。
`rollup`などでバンドルする場合は`"ESNext"`を指定しておけばよさそうです。

:::{note}

モダンブラウザ向けにESModuleを使う場合は、`"ES2015"`や`"ES2020"`などを指定します。
Node.jsを使う場合は`"CommonJS"`を指定します。GASでは非対応です。

:::

`moduleResolution`は、`import`や`require`で指定されたモジュールの探し方を指定するオプションです。
`rollup`などのバンドラーを使う場合は`"bundler"`を指定します。

:::{note}

`outDir`を省略すると、`.js`は各`.ts`ファイルと同じ場所に出力されます。
慣習的に`outDir`には`dist`がよく使われますが、
本ページでは`clasp`の`.clasp.json`を置くディレクトリと合わせる意図で、あえて`gas`という名前にしています。

`rollup`でバンドルする構成では`tsc`自体はファイルを出力しない（前述の`tsc --noEmit`）ので、
`outDir`はほとんど意味を持ちません。

:::

`skipLibCheck`は、`node_modules`にある型定義ファイル（`.d.ts`）の型チェックを省略するオプションです。
`@types/google-apps-script`など、サードパーティの型定義に問題があっても自分のコードのチェックを止めないために有効にしておくと安心です。
