# トランスパイルしたい（`tsc`）

```console
$ npx tsc
$ npx tsc src/main.ts
$ npx tsc --watch
```

`tsc`コマンドで、TypeScriptファイル（`.tx`）をトランスパイルできます。
設定ファイル（`tsconfig.json`）がある場合は、自動でよみこまれます。

`npx`で実行することが多いです。

## インストールしたい（`typescript`）

```console
$ npm install --save-dev typescript @types/google-apps-script
```

`typescript`パッケージを`devDependencies`として追加します。

`@types/google-apps-script`はGASの型チェックができるようになるパッケージです。

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

## 設定したい（`tsconfig.json`）

```json
{
    "compilerOptions": {
        "target": "ES2015",    // GAS V8対応
        "module": "ESNext",    // rollupでバンドル前提
        "moduleResolution": "bundler",
        "noUnusedLocals": true,    // 未使用の変数でエラー
        "noUnusedParameters": true,    // 未使用の引数でエラー
        "strict": true,    // 厳格な型チェック
        "outDir": "dist",    // 出力先ディレクトリ
        "rootDir": "src",    // ソースコードのルート
        "sourceMap": true,    // デバッグ用にソースマップを生成
        "removeComments": true    // コメントを除去
    },
    "include": [
        // トランスパイル対象
        "src/**/*"
    ],
    "exclude": [
        // トランスパイル対象外
        "node_modules",
        "coverage",
    ]
}
```

`tsconfig.json`でTypeScriptのトランスパイルの設定ができます。
GASのV8ランタイムはECMAScript2015（ES6 / ES2015）相当の機能しかサポートしていないため、それに合わせた設定が必要です。
ここでは`rollup`でモジュールをバンドルし、
`clasp`でデプロイする前提でサンプルを作成しました。

`target`は、トランスパイルして出力されるJavaScriptのECMAScriptバージョンを指定するオプションです。
GAS V8の場合は`"ES2015"`もしくは以降のバージョンを指定します。

`module`は、トランスパイルするときに利用するモジュール形式を指定するオプションです。
`rollup`などでバンドルする場合は`"ESNext"`を指定しておけばよさそうです。

:::{note}

モダンブラウザ向けにESModuleを使う場合は、`"ES2015"`や`"ES2020"`などを指定します。
Node.jsを使う場合は`"CommonJS"`を指定します。GASでは非対応です。

:::

`moduleResolution`は、`import`や`require`で指定されたモジュールの探し方を指定するオプションです。
`rollup`などのバンドラーを使う場合は`"bundler"`を指定します。
